"""
SpatialFlow Python SDK Client

The main entry point for the SpatialFlow API.
"""

from typing import Optional

# Import from the generated package using relative imports
# The generated code now uses relative imports internally
from ._generated.spatialflow_generated.api_client import ApiClient
from ._generated.spatialflow_generated.configuration import Configuration
from ._generated.spatialflow_generated.api.geofences_api import GeofencesApi
from ._generated.spatialflow_generated.api.workflows_api import WorkflowsApi
from ._generated.spatialflow_generated.api.webhooks_api import WebhooksApi
from ._generated.spatialflow_generated.api.devices_api import DevicesApi
from ._generated.spatialflow_generated.api.account_api import AccountApi

__all__ = ["SpatialFlow"]

# Host only - generated paths include /api/v1 prefix
DEFAULT_BASE_URL = "https://api.spatialflow.io"
DEFAULT_TIMEOUT = 30  # seconds
DEFAULT_MAX_RETRIES = 3
VERSION = "0.1.0"


class SpatialFlow:
    """
    SpatialFlow API client.

    Provides access to geofences, workflows, webhooks, and devices.

    Example:
        >>> client = SpatialFlow(api_key="sf_xxx")
        >>> geofences = await client.geofences.apps_geofences_api_list_geofences()

    Args:
        api_key: SpatialFlow API key (starts with "sf_")
        access_token: JWT access token (alternative to api_key)
        base_url: API base URL (default: https://api.spatialflow.io)
        timeout: Request timeout in seconds (default: 30)
        max_retries: Maximum retry attempts for failed requests (default: 3)
    """

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        access_token: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        timeout: int = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        if not api_key and not access_token:
            raise ValueError("Either api_key or access_token must be provided")

        if api_key and access_token:
            raise ValueError("Provide either api_key or access_token, not both")

        # Build configuration
        config = Configuration(host=base_url)

        # Configure authentication
        if api_key:
            config.api_key = {"APIKeyBearer": api_key}
        elif access_token:
            config.access_token = access_token

        # Configure timeouts and retries
        config.retries = max_retries

        # Create API client
        self._api_client = ApiClient(configuration=config)

        # Set User-Agent
        self._api_client.user_agent = f"spatialflow-python/{VERSION}"

        # Store config for reference
        self._base_url = base_url
        self._timeout = timeout
        self._max_retries = max_retries

        # Initialize resource APIs (lazy initialization)
        self._geofences: Optional[GeofencesApi] = None
        self._workflows: Optional[WorkflowsApi] = None
        self._webhooks: Optional[WebhooksApi] = None
        self._devices: Optional[DevicesApi] = None
        self._account: Optional[AccountApi] = None

    @property
    def geofences(self) -> GeofencesApi:
        """Access geofence operations."""
        if self._geofences is None:
            self._geofences = GeofencesApi(self._api_client)
        return self._geofences

    @property
    def workflows(self) -> WorkflowsApi:
        """Access workflow operations."""
        if self._workflows is None:
            self._workflows = WorkflowsApi(self._api_client)
        return self._workflows

    @property
    def webhooks(self) -> WebhooksApi:
        """Access webhook operations."""
        if self._webhooks is None:
            self._webhooks = WebhooksApi(self._api_client)
        return self._webhooks

    @property
    def devices(self) -> DevicesApi:
        """Access device operations."""
        if self._devices is None:
            self._devices = DevicesApi(self._api_client)
        return self._devices

    @property
    def account(self) -> AccountApi:
        """Access account operations."""
        if self._account is None:
            self._account = AccountApi(self._api_client)
        return self._account

    async def close(self) -> None:
        """Close the API client and release resources."""
        if self._api_client:
            await self._api_client.close()

    async def __aenter__(self) -> "SpatialFlow":
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        await self.close()
