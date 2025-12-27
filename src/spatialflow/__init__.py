"""
SpatialFlow Python SDK

A Python client for the SpatialFlow API - real-time geospatial automation platform.

Example:
    >>> from spatialflow import SpatialFlow, models
    >>>
    >>> async with SpatialFlow(api_key="sf_xxx") as client:
    ...     # List geofences
    ...     response = await client.geofences.list()
    ...     for geofence in response.geofences:
    ...         print(geofence.name)
    ...
    ...     # Create a geofence
    ...     geofence = await client.geofences.create(
    ...         models.CreateGeofenceRequest(name="My Region", geometry={...})
    ...     )

"""

__version__ = "0.2.0"

# Main client (imported early to get DEFAULT_BASE_URL)
from .client import SpatialFlow, DEFAULT_BASE_URL

# Custom exceptions
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
    translate_exception,
)

# Webhook verification
from .webhooks import verify_webhook_signature, WebhookSignatureError, verify_signature

# Pagination helpers
from .pagination import (
    paginate,
    paginate_geofences,
    paginate_workflows,
    paginate_webhooks,
    paginate_users,
    paginate_files,
    AsyncPaginator,
    PaginatedResponse,
)

# Job polling helpers
from .jobs import poll_job, JobResult, JobTimeoutError, JobFailedError

# File upload helpers
from .uploads import upload_geofences

# Workflow builders
from .builders import (
    build_geofence_webhook_workflow,
    build_geofence_integration_workflow,
    TriggerType,
)

# Resource classes (for type hints and advanced usage)
from .resources import (
    AccountResource,
    GeofencesResource,
    WorkflowsResource,
    WebhooksResource,
    DevicesResource,
    StorageResource,
    LocationsResource,
    IntegrationsResource,
    WorkspacesResource,
)

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
    "translate_exception",
    # Webhooks
    "verify_webhook_signature",
    "verify_signature",
    "WebhookSignatureError",
    # Pagination
    "paginate",
    "paginate_geofences",
    "paginate_workflows",
    "paginate_webhooks",
    "paginate_users",
    "paginate_files",
    "AsyncPaginator",
    "PaginatedResponse",
    # Job polling
    "poll_job",
    "JobResult",
    "JobTimeoutError",
    "JobFailedError",
    # File uploads
    "upload_geofences",
    # Workflow builders
    "build_geofence_webhook_workflow",
    "build_geofence_integration_workflow",
    "TriggerType",
    # Resource classes
    "AccountResource",
    "GeofencesResource",
    "WorkflowsResource",
    "WebhooksResource",
    "DevicesResource",
    "StorageResource",
    "LocationsResource",
    "IntegrationsResource",
    "WorkspacesResource",
    # Generated (advanced)
    "ApiClient",
    "Configuration",
    "models",
]
