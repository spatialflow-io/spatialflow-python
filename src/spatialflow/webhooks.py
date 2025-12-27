"""
Webhook signature verification for SpatialFlow SDK.

Provides HMAC-SHA256 signature verification for webhook payloads.
"""

import hashlib
import hmac
import time
from typing import Union

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

    SpatialFlow webhooks include an HMAC-SHA256 signature in the
    `X-SF-Signature` header. This function verifies that signature
    and optionally checks the timestamp to prevent replay attacks.

    Args:
        payload: The raw webhook payload (request body as string or bytes)
        signature: The signature from X-SF-Signature header
        secret: Your webhook signing secret
        tolerance: Maximum age of the webhook in seconds (default 300 = 5 minutes).
                   Set to 0 to disable timestamp checking.

    Returns:
        The parsed webhook payload as a dict

    Raises:
        WebhookSignatureError: If signature is invalid or timestamp is too old

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
        ...         print(f"Event type: {event['type']}")
        ...         return {"status": "ok"}
        ...     except WebhookSignatureError as e:
        ...         return {"error": str(e)}, 400
    """
    import json

    # Normalize payload to bytes
    if isinstance(payload, str):
        payload_bytes = payload.encode("utf-8")
    else:
        payload_bytes = payload

    # Parse the signature header
    # Format: t=<timestamp>,v1=<signature>
    try:
        parts = dict(part.strip().split("=", 1) for part in signature.split(","))
        timestamp_str = parts.get("t")
        sig_hash = parts.get("v1")

        if not timestamp_str or not sig_hash:
            raise WebhookSignatureError(
                "Invalid signature format. Expected: t=<timestamp>,v1=<signature>"
            )

        timestamp = int(timestamp_str)
    except (ValueError, AttributeError) as e:
        raise WebhookSignatureError(f"Failed to parse signature header: {e}")

    # Check timestamp tolerance (replay attack prevention)
    if tolerance > 0:
        now = int(time.time())
        age = now - timestamp
        if age > tolerance:
            raise WebhookSignatureError(
                f"Webhook timestamp too old: {age}s (tolerance: {tolerance}s)"
            )
        if age < -tolerance:
            raise WebhookSignatureError(
                f"Webhook timestamp in future: {-age}s (tolerance: {tolerance}s)"
            )

    # Compute expected signature
    # The signed payload is: timestamp.payload
    signed_payload = f"{timestamp}.".encode("utf-8") + payload_bytes
    expected_sig = hmac.new(
        secret.encode("utf-8"),
        signed_payload,
        hashlib.sha256,
    ).hexdigest()

    # Constant-time comparison to prevent timing attacks
    if not hmac.compare_digest(expected_sig, sig_hash):
        raise WebhookSignatureError("Signature verification failed")

    # Parse and return the payload
    try:
        return json.loads(payload_bytes.decode("utf-8"))
    except json.JSONDecodeError as e:
        raise WebhookSignatureError(f"Failed to parse webhook payload as JSON: {e}")


# Convenience alias
verify_signature = verify_webhook_signature
