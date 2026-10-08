"""
Webhook signature verification for SpatialFlow SDK.

Provides HMAC-SHA256 signature verification for webhook payloads.
"""

import hashlib
import hmac
import json
import re
import time
from typing import Any, Union

from .exceptions import SpatialFlowError


class WebhookSignatureError(SpatialFlowError):
    """Raised when webhook signature verification fails."""

    pass


def verify_webhook_signature(
    payload: Union[str, bytes],
    signature: str,
    secret: str,
    tolerance: int = 300,
) -> dict:
    """
    Verify a webhook signature and return the parsed payload.

    SpatialFlow signs each delivery with an HMAC-SHA256 of the raw request
    body and sends it in the ``X-SF-Signature`` header, hex-encoded and
    prefixed with ``sha256=`` (for example ``sha256=5257a869...``). This
    function recomputes that HMAC and compares it in constant time.

    Args:
        payload: The raw webhook payload (request body as string or bytes).
        signature: The value of the ``X-SF-Signature`` header.
        secret: Your webhook signing secret.
        tolerance: Deprecated and ignored. The SpatialFlow signature does not
            include a timestamp, so there is no time-based replay window. To
            guard against replays, deduplicate on the signed ``id`` in the
            payload, recording it in the same transaction as the work and
            acknowledging only committed work; the
            ``X-Idempotency-Key`` and ``X-SF-Event-ID`` headers are not signed.
            The default payload has an ``id``; a custom payload template must
            include one.

    Returns:
        The parsed webhook payload as a dict.

    Raises:
        WebhookSignatureError: If the signature is missing, malformed, does
            not match, or the payload is not valid JSON.

    Example:
        >>> from spatialflow import verify_webhook_signature
        >>>
        >>> # In your webhook handler (e.g., Flask/FastAPI)
        >>> @app.post("/webhook")
        >>> async def handle_webhook(request):
        ...     payload = await request.body()
        ...     signature = request.headers.get("X-SF-Signature")
        ...
        ...     try:
        ...         event = verify_webhook_signature(
        ...             payload=payload,
        ...             signature=signature,
        ...             secret=WEBHOOK_SECRET,
        ...         )
        ...         # Process the verified event
        ...         print(f"Event type: {event['event']}")
        ...         return {"status": "ok"}
        ...     except WebhookSignatureError as e:
        ...         return {"error": str(e)}, 400
    """
    if isinstance(payload, str):
        payload_bytes = payload.encode("utf-8")
    else:
        payload_bytes = payload

    if not signature:
        raise WebhookSignatureError("Missing signature header")

    # The header is `sha256=<hex>`; tolerate a bare hex digest as well.
    sig_hash = signature.strip()
    if sig_hash.startswith("sha256="):
        sig_hash = sig_hash[len("sha256=") :]

    if not sig_hash:
        raise WebhookSignatureError(
            "Invalid signature format. Expected: sha256=<hex digest>"
        )

    # Decode the provided hex digest to bytes. Doing this first means a
    # malformed header (non-hex or non-ASCII) is rejected as a
    # WebhookSignatureError rather than letting hmac.compare_digest raise a
    # TypeError on non-ASCII strings, and it keeps the comparison on bytes.
    try:
        provided_digest = bytes.fromhex(sig_hash)
    except ValueError:
        raise WebhookSignatureError("Invalid signature: not valid hex")

    expected_digest = hmac.new(
        secret.encode("utf-8"),
        payload_bytes,
        hashlib.sha256,
    ).digest()

    # Constant-time comparison to prevent timing attacks.
    if not hmac.compare_digest(expected_digest, provided_digest):
        raise WebhookSignatureError("Signature verification failed")

    try:
        return json.loads(payload_bytes.decode("utf-8"))
    except json.JSONDecodeError as e:
        raise WebhookSignatureError(f"Failed to parse webhook payload as JSON: {e}")


verify_signature = verify_webhook_signature


def verify_workflow_signature(
    payload: Union[str, bytes],
    signature: str,
    timestamp: str,
    secret: str,
    tolerance: int = 300,
) -> Any:
    """
    Verify a workflow webhook action delivery and return the parsed body.

    A workflow Webhook action with a signing secret sends two headers:
    ``X-SpatialFlow-Timestamp`` (unix seconds) and ``X-SpatialFlow-Signature``
    (``sha256=<hex>``). The signature is an HMAC-SHA256 of
    ``"<timestamp>.<raw body>"``. This is a different contract from the
    workspace webhook header handled by :func:`verify_webhook_signature`.

    Args:
        payload: The raw request body (str or bytes), exactly as received.
        signature: The value of the ``X-SpatialFlow-Signature`` header.
        timestamp: The value of the ``X-SpatialFlow-Timestamp`` header.
        secret: The webhook signing secret.
        tolerance: Maximum age, in seconds, of the timestamp in either
            direction. Defaults to 300.

    Returns:
        The parsed JSON body, or the body as text when it is not JSON. The
        workflow action sends whatever body the workflow configures, so the
        shape is not normalized.

    Raises:
        WebhookSignatureError: If the signature or timestamp is missing or
            malformed, the timestamp is outside the tolerance, the signature
            does not match, or the body is not valid UTF-8.
    """
    if not signature:
        raise WebhookSignatureError("Missing signature header")

    timestamp = (timestamp or "").strip()
    if not re.fullmatch(r"[0-9]{1,15}", timestamp, re.ASCII):
        raise WebhookSignatureError("Missing or invalid timestamp header")
    sent_at = int(timestamp)

    if abs(time.time() - sent_at) > tolerance:
        raise WebhookSignatureError("Timestamp outside the tolerance window")

    sig_hash = signature.strip()
    if sig_hash.startswith("sha256="):
        sig_hash = sig_hash[len("sha256=") :]
    try:
        provided_digest = bytes.fromhex(sig_hash)
    except ValueError:
        raise WebhookSignatureError("Invalid signature: not valid hex")
    if not provided_digest:
        raise WebhookSignatureError(
            "Invalid signature format. Expected: sha256=<hex digest>"
        )

    payload_bytes = payload.encode("utf-8") if isinstance(payload, str) else payload
    expected_digest = hmac.new(
        secret.encode("utf-8"),
        timestamp.encode("ascii") + b"." + payload_bytes,
        hashlib.sha256,
    ).digest()

    if not hmac.compare_digest(expected_digest, provided_digest):
        raise WebhookSignatureError("Signature verification failed")

    try:
        text = payload_bytes.decode("utf-8")
    except UnicodeDecodeError as e:
        raise WebhookSignatureError(f"Webhook payload is not valid UTF-8: {e}")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text
