"""Tests for webhook signature verification."""

import hashlib
import hmac
import json
import time

import pytest

from spatialflow import verify_webhook_signature, WebhookSignatureError


class TestVerifyWebhookSignature:
    """Test webhook signature verification."""

    def _create_signature(self, payload: bytes, secret: str, timestamp: int) -> str:
        """Create a valid signature for testing."""
        signed_payload = f"{timestamp}.".encode() + payload
        signature = hmac.new(
            secret.encode(),
            signed_payload,
            hashlib.sha256,
        ).hexdigest()
        return f"t={timestamp},v1={signature}"

    def test_valid_signature(self):
        """Test verification with valid signature."""
        secret = "test_secret_key"
        payload = {"type": "geofence.entered", "data": {"device_id": "123"}}
        payload_bytes = json.dumps(payload).encode()
        timestamp = int(time.time())

        signature = self._create_signature(payload_bytes, secret, timestamp)

        result = verify_webhook_signature(
            payload=payload_bytes,
            signature=signature,
            secret=secret,
        )

        assert result["type"] == "geofence.entered"
        assert result["data"]["device_id"] == "123"

    def test_valid_signature_string_payload(self):
        """Test verification with string payload."""
        secret = "test_secret_key"
        payload_str = '{"type": "test.event"}'
        timestamp = int(time.time())

        signature = self._create_signature(payload_str.encode(), secret, timestamp)

        result = verify_webhook_signature(
            payload=payload_str,
            signature=signature,
            secret=secret,
        )

        assert result["type"] == "test.event"

    def test_invalid_signature_format(self):
        """Test that invalid signature format raises error."""
        with pytest.raises(WebhookSignatureError, match="Failed to parse signature header"):
            verify_webhook_signature(
                payload=b"{}",
                signature="invalid_format",
                secret="secret",
            )

    def test_missing_timestamp(self):
        """Test that missing timestamp raises error."""
        with pytest.raises(WebhookSignatureError, match="Invalid signature format"):
            verify_webhook_signature(
                payload=b"{}",
                signature="v1=abcd1234",
                secret="secret",
            )

    def test_missing_signature(self):
        """Test that missing signature raises error."""
        with pytest.raises(WebhookSignatureError, match="Invalid signature format"):
            verify_webhook_signature(
                payload=b"{}",
                signature="t=12345",
                secret="secret",
            )

    def test_expired_timestamp(self):
        """Test that expired timestamp raises error."""
        secret = "test_secret"
        payload = b'{"type": "test"}'
        old_timestamp = int(time.time()) - 600  # 10 minutes ago

        signature = self._create_signature(payload, secret, old_timestamp)

        with pytest.raises(WebhookSignatureError, match="too old"):
            verify_webhook_signature(
                payload=payload,
                signature=signature,
                secret=secret,
                tolerance=300,  # 5 minute tolerance
            )

    def test_custom_tolerance(self):
        """Test custom timestamp tolerance."""
        secret = "test_secret"
        payload = b'{"type": "test"}'
        old_timestamp = int(time.time()) - 400  # 6+ minutes ago

        signature = self._create_signature(payload, secret, old_timestamp)

        # Should fail with 5 minute tolerance
        with pytest.raises(WebhookSignatureError, match="too old"):
            verify_webhook_signature(
                payload=payload,
                signature=signature,
                secret=secret,
                tolerance=300,
            )

        # Should pass with 10 minute tolerance
        result = verify_webhook_signature(
            payload=payload,
            signature=signature,
            secret=secret,
            tolerance=600,
        )
        assert result["type"] == "test"

    def test_wrong_secret(self):
        """Test that wrong secret raises error."""
        payload = b'{"type": "test"}'
        timestamp = int(time.time())

        signature = self._create_signature(payload, "correct_secret", timestamp)

        with pytest.raises(WebhookSignatureError, match="verification failed"):
            verify_webhook_signature(
                payload=payload,
                signature=signature,
                secret="wrong_secret",
            )

    def test_tampered_payload(self):
        """Test that tampered payload raises error."""
        secret = "test_secret"
        original_payload = b'{"type": "original"}'
        timestamp = int(time.time())

        signature = self._create_signature(original_payload, secret, timestamp)

        with pytest.raises(WebhookSignatureError, match="verification failed"):
            verify_webhook_signature(
                payload=b'{"type": "tampered"}',
                signature=signature,
                secret=secret,
            )

    def test_invalid_json_payload(self):
        """Test that invalid JSON payload raises error."""
        secret = "test_secret"
        payload = b"not valid json"
        timestamp = int(time.time())

        signature = self._create_signature(payload, secret, timestamp)

        with pytest.raises(WebhookSignatureError, match="Failed to parse webhook payload"):
            verify_webhook_signature(
                payload=payload,
                signature=signature,
                secret=secret,
            )
