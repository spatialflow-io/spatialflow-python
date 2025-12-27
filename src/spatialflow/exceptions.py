"""
SpatialFlow SDK Exceptions

Provides a clean exception hierarchy for handling API errors.
These wrap the generated exceptions with more user-friendly interfaces.
"""

from typing import Any, Optional


class SpatialFlowError(Exception):
    """Base exception for all SpatialFlow SDK errors."""

    def __init__(
        self,
        message: str,
        *,
        status_code: Optional[int] = None,
        detail: Optional[str] = None,
        error_code: Optional[str] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.detail = detail
        self.error_code = error_code
        self.headers = headers or {}

    def __str__(self) -> str:
        parts = [self.message]
        if self.status_code:
            parts.insert(0, f"[{self.status_code}]")
        if self.detail and self.detail != self.message:
            parts.append(f"- {self.detail}")
        return " ".join(parts)


class AuthenticationError(SpatialFlowError):
    """
    Raised when authentication fails (401 Unauthorized).

    This typically means:
    - API key is invalid or expired
    - JWT token is invalid or expired
    - No authentication credentials provided
    """

    pass


class PermissionError(SpatialFlowError):
    """
    Raised when the authenticated user lacks permission (403 Forbidden).

    This typically means:
    - User doesn't have access to this resource
    - API key doesn't have the required scope
    - Organization limits exceeded
    """

    pass


class NotFoundError(SpatialFlowError):
    """
    Raised when a resource is not found (404 Not Found).

    Check that:
    - The resource ID is correct
    - The resource hasn't been deleted
    - You have access to the resource
    """

    pass


class ValidationError(SpatialFlowError):
    """
    Raised when request validation fails (400 Bad Request or 422 Unprocessable Entity).

    Check that:
    - Required fields are provided
    - Field values match expected types/formats
    - Geometry is valid GeoJSON
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: Optional[int] = None,
        detail: Optional[str] = None,
        error_code: Optional[str] = None,
        headers: Optional[dict[str, str]] = None,
        errors: Optional[list[dict[str, Any]]] = None,
    ) -> None:
        super().__init__(
            message,
            status_code=status_code,
            detail=detail,
            error_code=error_code,
            headers=headers,
        )
        self.errors = errors or []


class RateLimitError(SpatialFlowError):
    """
    Raised when rate limit is exceeded (429 Too Many Requests).

    The `retry_after` property indicates when you can retry.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int = 429,
        detail: Optional[str] = None,
        error_code: Optional[str] = None,
        headers: Optional[dict[str, str]] = None,
        retry_after: Optional[int] = None,
    ) -> None:
        super().__init__(
            message,
            status_code=status_code,
            detail=detail,
            error_code=error_code,
            headers=headers,
        )
        self.retry_after = retry_after or self._parse_retry_after(headers)

    def _parse_retry_after(self, headers: Optional[dict[str, str]]) -> Optional[int]:
        if not headers:
            return None
        retry_after = headers.get("Retry-After") or headers.get("retry-after")
        if retry_after:
            try:
                return int(retry_after)
            except ValueError:
                pass
        return None


class ServerError(SpatialFlowError):
    """
    Raised when the server encounters an error (5xx status codes).

    This is typically a temporary issue. Retry with exponential backoff.
    """

    pass


class ConflictError(SpatialFlowError):
    """
    Raised when there's a resource conflict (409 Conflict).

    This typically means:
    - Resource already exists with that name/identifier
    - Concurrent modification conflict
    """

    pass


class TimeoutError(SpatialFlowError):
    """Raised when a request times out."""

    pass


class ConnectionError(SpatialFlowError):
    """Raised when unable to connect to the API."""

    pass


def raise_for_status(
    status_code: int,
    message: str = "API request failed",
    *,
    detail: Optional[str] = None,
    error_code: Optional[str] = None,
    headers: Optional[dict[str, str]] = None,
    body: Optional[Any] = None,
) -> None:
    """
    Raise the appropriate exception based on HTTP status code.

    Args:
        status_code: HTTP status code
        message: Error message
        detail: Additional error detail
        error_code: Machine-readable error code
        headers: Response headers
        body: Response body (for extracting validation errors)
    """
    # Extract detail from body if not provided
    if body and not detail:
        if isinstance(body, dict):
            detail = body.get("detail")
            if isinstance(detail, list):
                # Django Ninja validation error format
                detail = "; ".join(str(e) for e in detail)
            error_code = error_code or body.get("error_code")

    kwargs = {
        "status_code": status_code,
        "detail": detail,
        "error_code": error_code,
        "headers": headers,
    }

    if status_code == 400 or status_code == 422:
        errors = []
        if isinstance(body, dict) and isinstance(body.get("detail"), list):
            errors = body["detail"]
        raise ValidationError(message, errors=errors, **kwargs)
    elif status_code == 401:
        raise AuthenticationError(message, **kwargs)
    elif status_code == 403:
        raise PermissionError(message, **kwargs)
    elif status_code == 404:
        raise NotFoundError(message, **kwargs)
    elif status_code == 409:
        raise ConflictError(message, **kwargs)
    elif status_code == 429:
        raise RateLimitError(message, **kwargs)
    elif 500 <= status_code < 600:
        raise ServerError(message, **kwargs)
    elif status_code >= 400:
        raise SpatialFlowError(message, **kwargs)


def translate_exception(exc: Exception) -> SpatialFlowError:
    """
    Translate generated OpenAPI exceptions to SDK exceptions.

    This provides a consistent exception interface for users, regardless
    of whether they use wrapper methods or call the generated API directly.

    Args:
        exc: The original exception from the generated client

    Returns:
        An appropriate SpatialFlowError subclass
    """
    # Import here to avoid circular imports
    from ._generated.spatialflow_generated.exceptions import (
        ApiException,
        UnauthorizedException,
        ForbiddenException,
        NotFoundException,
        BadRequestException,
        ServiceException,
    )

    # Extract message and details from the exception
    message = str(exc)
    status_code = None
    detail = None
    headers = None
    body = None

    if isinstance(exc, ApiException):
        status_code = exc.status
        message = exc.reason or message
        headers = dict(exc.headers) if exc.headers else None
        body = exc.body

    if isinstance(exc, UnauthorizedException):
        return AuthenticationError(
            message, status_code=status_code or 401, detail=detail, headers=headers
        )
    if isinstance(exc, ForbiddenException):
        return PermissionError(
            message, status_code=status_code or 403, detail=detail, headers=headers
        )
    if isinstance(exc, NotFoundException):
        return NotFoundError(
            message, status_code=status_code or 404, detail=detail, headers=headers
        )
    if isinstance(exc, BadRequestException):
        return ValidationError(
            message, status_code=status_code or 400, detail=detail, headers=headers
        )
    if isinstance(exc, ServiceException):
        return ServerError(
            message, status_code=status_code or 500, detail=detail, headers=headers
        )
    if isinstance(exc, ApiException):
        # Generic API exception - use raise_for_status logic
        if status_code:
            try:
                raise_for_status(status_code, message, headers=headers, body=body)
            except SpatialFlowError as e:
                return e
        return SpatialFlowError(message, status_code=status_code, headers=headers)

    # Non-API exceptions (connection errors, timeouts, etc.)
    # Handle Python built-in exceptions
    if isinstance(exc, TimeoutError):
        return TimeoutError(message)
    if isinstance(exc, ConnectionError):
        return ConnectionError(message)

    # Handle asyncio timeouts
    import asyncio

    if isinstance(exc, asyncio.TimeoutError):
        return TimeoutError(f"Request timed out: {message}")

    # Handle aiohttp-specific exceptions
    try:
        import aiohttp

        if isinstance(exc, aiohttp.ClientError):
            if isinstance(exc, aiohttp.ServerTimeoutError):
                return TimeoutError(f"Server timeout: {message}")
            if isinstance(exc, aiohttp.ClientConnectorError):
                return ConnectionError(f"Connection failed: {message}")
            if isinstance(exc, aiohttp.ClientResponseError):
                # Map HTTP status codes to SDK exceptions
                status = getattr(exc, "status", None)
                if status:
                    try:
                        raise_for_status(status, message)
                    except SpatialFlowError as e:
                        return e
            # Generic aiohttp client error
            return ConnectionError(f"HTTP client error: {message}")
    except ImportError:
        pass  # aiohttp not available

    # Fallback for unknown exceptions
    return SpatialFlowError(message)
