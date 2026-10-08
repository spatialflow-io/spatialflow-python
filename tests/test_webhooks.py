import hashlib
import hmac
import json
import time

import pytest

from spatialflow import (
    verify_webhook_signature,
    verify_workflow_signature,
    WebhookSignatureError,
)


class TestVerifyWebhookSignature:
    def _create_signature(self, payload: bytes, secret: str) -> str:
        """Create a valid `sha256=<hex>` signature for testing.

        Mirrors the backend, which signs the raw request body with
        HMAC-SHA256 and prefixes the hex digest with `sha256=`.
        """
        digest = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
        return f"sha256={digest}"

    def test_valid_signature(self):
        secret = "test_secret_key"
        payload = {"type": "geofence.entered", "data": {"device_id": "123"}}
        payload_bytes = json.dumps(payload).encode()

        signature = self._create_signature(payload_bytes, secret)

        result = verify_webhook_signature(
            payload=payload_bytes,
            signature=signature,
            secret=secret,
        )

        assert result["type"] == "geofence.entered"
        assert result["data"]["device_id"] == "123"

    def test_valid_signature_string_payload(self):
        secret = "test_secret_key"
        payload_str = '{"type": "test.event"}'

        signature = self._create_signature(payload_str.encode(), secret)

        result = verify_webhook_signature(
            payload=payload_str,
            signature=signature,
            secret=secret,
        )

        assert result["type"] == "test.event"

    def test_valid_signature_without_prefix(self):
        secret = "test_secret_key"
        payload = b'{"type": "test.event"}'
        digest = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()

        result = verify_webhook_signature(
            payload=payload,
            signature=digest,
            secret=secret,
        )

        assert result["type"] == "test.event"

    def test_missing_signature(self):
        with pytest.raises(WebhookSignatureError, match="Missing signature"):
            verify_webhook_signature(
                payload=b"{}",
                signature="",
                secret="secret",
            )

    def test_empty_digest(self):
        with pytest.raises(WebhookSignatureError, match="Invalid signature format"):
            verify_webhook_signature(
                payload=b"{}",
                signature="sha256=",
                secret="secret",
            )

    def test_non_hex_signature(self):
        """A non-hex digest is rejected cleanly (not a ValueError leak)."""
        with pytest.raises(WebhookSignatureError, match="not valid hex"):
            verify_webhook_signature(
                payload=b"{}",
                signature="sha256=zzzz",
                secret="secret",
            )

    def test_non_ascii_signature(self):
        """A non-ASCII signature raises WebhookSignatureError, not TypeError."""
        with pytest.raises(WebhookSignatureError):
            verify_webhook_signature(
                payload=b"{}",
                signature="sha256=éé",
                secret="secret",
            )

    def test_wrong_secret(self):
        payload = b'{"type": "test"}'
        signature = self._create_signature(payload, "correct_secret")

        with pytest.raises(WebhookSignatureError, match="verification failed"):
            verify_webhook_signature(
                payload=payload,
                signature=signature,
                secret="wrong_secret",
            )

    def test_tampered_payload(self):
        secret = "test_secret"
        original_payload = b'{"type": "original"}'
        signature = self._create_signature(original_payload, secret)

        with pytest.raises(WebhookSignatureError, match="verification failed"):
            verify_webhook_signature(
                payload=b'{"type": "tampered"}',
                signature=signature,
                secret=secret,
            )

    def test_invalid_json_payload(self):
        secret = "test_secret"
        payload = b"not valid json"
        signature = self._create_signature(payload, secret)

        with pytest.raises(
            WebhookSignatureError, match="Failed to parse webhook payload"
        ):
            verify_webhook_signature(
                payload=payload,
                signature=signature,
                secret=secret,
            )

    def test_tolerance_kwarg_is_ignored(self):
        """The deprecated `tolerance` kwarg is accepted but has no effect."""
        secret = "test_secret"
        payload = b'{"type": "test"}'
        signature = self._create_signature(payload, secret)

        result = verify_webhook_signature(
            payload=payload,
            signature=signature,
            secret=secret,
            tolerance=0,
        )
        assert result["type"] == "test"


class TestVerifyWorkflowSignature:
    secret = "workflow_secret"  # pragma: allowlist secret

    def _sign(self, body: bytes, timestamp: str, secret: str = None) -> str:
        """Mirror the backend: HMAC-SHA256 over `<timestamp>.<body>`."""
        digest = hmac.new(
            (secret or self.secret).encode(),
            timestamp.encode() + b"." + body,
            hashlib.sha256,
        ).hexdigest()
        return f"sha256={digest}"

    def _verify(self, body, signature, timestamp, **kwargs):
        return verify_workflow_signature(
            payload=body,
            signature=signature,
            timestamp=timestamp,
            secret=self.secret,
            **kwargs,
        )

    def test_genuine_delivery_is_accepted_and_parsed(self):
        body = json.dumps({"alert": "geofence.enter", "device": "d1"}).encode()
        ts = str(int(time.time()))

        result = self._verify(body, self._sign(body, ts), ts)

        assert result == {"alert": "geofence.enter", "device": "d1"}

    def test_string_payload_and_non_object_body(self):
        body = "[1, 2]"
        ts = str(int(time.time()))

        assert self._verify(body, self._sign(body.encode(), ts), ts) == [1, 2]

    def test_forged_signature_is_rejected(self):
        body = b'{"a": 1}'
        ts = str(int(time.time()))
        forged = self._sign(body, ts, secret="wrong")

        with pytest.raises(WebhookSignatureError, match="verification failed"):
            self._verify(body, forged, ts)

    def test_tampered_body_is_rejected(self):
        ts = str(int(time.time()))
        signature = self._sign(b'{"a": 1}', ts)

        with pytest.raises(WebhookSignatureError):
            self._verify(b'{"a": 2}', signature, ts)

    def test_timestamp_is_part_of_the_signed_bytes(self):
        body = b'{"a": 1}'
        ts = str(int(time.time()))
        signature = self._sign(body, ts)

        with pytest.raises(WebhookSignatureError):
            self._verify(body, signature, str(int(ts) + 1))

    def test_subscription_signature_is_not_a_workflow_signature(self):
        body = b'{"a": 1}'
        digest = hmac.new(self.secret.encode(), body, hashlib.sha256).hexdigest()

        with pytest.raises(WebhookSignatureError):
            self._verify(body, f"sha256={digest}", str(int(time.time())))

    def test_stale_timestamp_is_rejected(self):
        body = b'{"a": 1}'
        ts = str(int(time.time()) - 301)

        with pytest.raises(WebhookSignatureError, match="tolerance"):
            self._verify(body, self._sign(body, ts), ts)

    def test_future_timestamp_is_rejected(self):
        body = b'{"a": 1}'
        ts = str(int(time.time()) + 301)

        with pytest.raises(WebhookSignatureError, match="tolerance"):
            self._verify(body, self._sign(body, ts), ts)

    def test_custom_tolerance(self):
        body = b'{"a": 1}'
        ts = str(int(time.time()) - 600)
        signature = self._sign(body, ts)

        assert self._verify(body, signature, ts, tolerance=900) == {"a": 1}

    @pytest.mark.parametrize("ts", [None, "", "abc", "12.5", "-5", "1e9", "١٢", "9" * 400, "9" * 5000])
    def test_missing_or_garbage_timestamp_is_rejected(self, ts):
        body = b'{"a": 1}'

        with pytest.raises(WebhookSignatureError, match="timestamp"):
            self._verify(body, self._sign(body, str(int(time.time()))), ts)

    @pytest.mark.parametrize("signature", [None, "", "sha256=", "sha256=zz", "sha256=é"])
    def test_missing_or_malformed_signature_is_rejected(self, signature):
        with pytest.raises(WebhookSignatureError):
            self._verify(b'{"a": 1}', signature, str(int(time.time())))

    def test_body_that_is_not_json_is_returned_as_text(self):
        body = b"alert=entered&zone=dock"
        ts = str(int(time.time()))

        assert self._verify(body, self._sign(body, ts), ts) == "alert=entered&zone=dock"

    def test_body_that_is_not_utf8_is_rejected(self):
        body = b"\xff\xfe"
        ts = str(int(time.time()))

        with pytest.raises(WebhookSignatureError, match="UTF-8"):
            self._verify(body, self._sign(body, ts), ts)


class TestSubscriptionVerifierUnchanged:
    def test_signs_the_body_only_and_ignores_tolerance(self):
        secret = "test_secret_key"
        body = b'{"id": "d1", "event": "webhook.test"}'
        digest = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()

        result = verify_webhook_signature(
            payload=body, signature=f"sha256={digest}", secret=secret, tolerance=0
        )

        assert result["event"] == "webhook.test"
