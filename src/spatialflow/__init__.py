"""
SpatialFlow Python SDK

A Python client for the SpatialFlow API - real-time geospatial automation platform.

Example:
    >>> from spatialflow import SpatialFlow
    >>>
    >>> async with SpatialFlow(api_key="sf_xxx") as client:
    ...     geofences = await client.geofences.apps_geofences_api_list_geofences()
    ...     for geofence in geofences.results:
    ...         print(geofence.name)

"""

__version__ = "0.1.0"

# Default base URL for the SpatialFlow API (host only, paths include /api/v1)
# Override in client configuration if using a different environment
DEFAULT_BASE_URL = "https://api.spatialflow.io"

# Custom exceptions (import before client to ensure they're available)
from .exceptions import (
    SpatialFlowError,
    AuthenticationError,
    PermissionError,
    NotFoundError,
    ValidationError,
    RateLimitError,
    ServerError,
    ConflictError,
    TimeoutError,
    ConnectionError,
)

# Main client
from .client import SpatialFlow

# Webhook verification
from .webhooks import verify_webhook_signature, WebhookSignatureError

# Pagination helpers
from .pagination import paginate, AsyncPaginator, PaginatedResponse

# Job polling helpers
from .jobs import poll_job, JobResult, JobTimeoutError, JobFailedError

# File upload helpers
from .uploads import upload_geofences

# Re-export generated client and models for advanced usage
from ._generated.spatialflow_generated.api_client import ApiClient
from ._generated.spatialflow_generated.configuration import Configuration
from ._generated.spatialflow_generated import models

__all__ = [
    # Version
    "__version__",
    "DEFAULT_BASE_URL",
    # Main client
    "SpatialFlow",
    # Exceptions
    "SpatialFlowError",
    "AuthenticationError",
    "PermissionError",
    "NotFoundError",
    "ValidationError",
    "RateLimitError",
    "ServerError",
    "ConflictError",
    "TimeoutError",
    "ConnectionError",
    # Webhooks
    "verify_webhook_signature",
    "WebhookSignatureError",
    # Pagination
    "paginate",
    "AsyncPaginator",
    "PaginatedResponse",
    # Job polling
    "poll_job",
    "JobResult",
    "JobTimeoutError",
    "JobFailedError",
    # File uploads
    "upload_geofences",
    # Generated (advanced)
    "ApiClient",
    "Configuration",
    "models",
]
