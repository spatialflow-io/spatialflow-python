"""
SpatialFlow Python SDK Client

The main entry point for the SpatialFlow API.
"""

from typing import Optional, Union

# Import from bundled generated package (relative imports for self-contained wheel)
from ._generated.spatialflow_generated.api_client import ApiClient
from ._generated.spatialflow_generated.configuration import Configuration
from ._generated.spatialflow_generated.api.geofences_api import GeofencesApi
from ._generated.spatialflow_generated.api.workflows_api import WorkflowsApi
from ._generated.spatialflow_generated.api.webhooks_api import WebhooksApi
from ._generated.spatialflow_generated.api.devices_api import DevicesApi
from ._generated.spatialflow_generated.api.account_api import AccountApi
from ._generated.spatialflow_generated.api.storage_api import StorageApi
from ._generated.spatialflow_generated.api.public_location_ingest_api import (
    PublicLocationIngestApi,
)
from ._generated.spatialflow_generated.api.integrations_api import IntegrationsApi
from ._generated.spatialflow_generated.api.workspaces_api import WorkspacesApi
from ._generated.spatialflow_generated.api.authentication_api import AuthenticationApi
from ._generated.spatialflow_generated.api.admin_api import AdminApi
from ._generated.spatialflow_generated.api.billing_api import BillingApi
from ._generated.spatialflow_generated.api.subscriptions_api import SubscriptionsApi
from ._generated.spatialflow_generated.api.tiles_api import TilesApi

# Import resource wrappers for clean API
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

__all__ = ["SpatialFlow"]

# Host only - generated paths include /api/v1 prefix
DEFAULT_BASE_URL = "https://api.spatialflow.io"
DEFAULT_TIMEOUT = 30  # seconds
DEFAULT_MAX_RETRIES = 3
VERSION = "0.2.0"


class SpatialFlow:
    """
    SpatialFlow API client.

    Provides access to geofences, workflows, webhooks, and devices.

    The client provides two API surfaces:
    - Clean API: `client.geofences.list()`, `client.geofences.create(...)`, etc.
    - Raw API: `client.raw.geofences.apps_geofences_api_list_geofences()`, etc.

    Example (Clean API - Recommended):
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

    Example (Raw API - Full control):
        >>> async with SpatialFlow(api_key="sf_xxx") as client:
        ...     response = await client.raw.geofences.apps_geofences_api_list_geofences()

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

        # Initialize raw APIs (lazy initialization)
        self._raw_geofences: Optional[GeofencesApi] = None
        self._raw_workflows: Optional[WorkflowsApi] = None
        self._raw_webhooks: Optional[WebhooksApi] = None
        self._raw_devices: Optional[DevicesApi] = None
        self._raw_account: Optional[AccountApi] = None
        self._raw_storage: Optional[StorageApi] = None
        self._raw_locations: Optional[PublicLocationIngestApi] = None
        self._raw_integrations: Optional[IntegrationsApi] = None
        self._raw_workspaces: Optional[WorkspacesApi] = None
        self._raw_authentication: Optional[AuthenticationApi] = None
        self._raw_admin: Optional[AdminApi] = None
        self._raw_billing: Optional[BillingApi] = None
        self._raw_subscriptions: Optional[SubscriptionsApi] = None
        self._raw_tiles: Optional[TilesApi] = None

        # Initialize resource wrappers (lazy initialization)
        self._geofences: Optional[GeofencesResource] = None
        self._workflows: Optional[WorkflowsResource] = None
        self._webhooks: Optional[WebhooksResource] = None
        self._devices: Optional[DevicesResource] = None
        self._storage: Optional[StorageResource] = None
        self._locations: Optional[LocationsResource] = None
        self._integrations: Optional[IntegrationsResource] = None
        self._workspaces: Optional[WorkspacesResource] = None
        self._account_resource: Optional[AccountResource] = None

    # -------------------------------------------------------------------------
    # Clean API - Recommended for most use cases
    # -------------------------------------------------------------------------

    @property
    def geofences(self) -> GeofencesResource:
        """Access geofence operations with clean API.

        Methods: list(), create(), get(), update(), delete(), bulk_create(), upload()
        """
        if self._geofences is None:
            self._geofences = GeofencesResource(self._raw_geofences_api, self._timeout)
        return self._geofences

    @property
    def workflows(self) -> WorkflowsResource:
        """Access workflow operations with clean API.

        Methods: list(), create(), get(), update(), delete(), toggle()
        """
        if self._workflows is None:
            self._workflows = WorkflowsResource(self._raw_workflows_api, self._timeout)
        return self._workflows

    @property
    def webhooks(self) -> WebhooksResource:
        """Access webhook operations with clean API.

        Methods: list(), create(), get(), update(), delete(), rotate_secret()
        """
        if self._webhooks is None:
            self._webhooks = WebhooksResource(self._raw_webhooks_api, self._timeout)
        return self._webhooks

    @property
    def devices(self) -> DevicesResource:
        """Access device operations with clean API.

        Methods: list(), create(), get(), update(), delete(), update_location()
        """
        if self._devices is None:
            self._devices = DevicesResource(self._raw_devices_api, self._timeout)
        return self._devices

    @property
    def storage(self) -> StorageResource:
        """Access storage operations with clean API.

        Methods: create_presigned_url(), list_files(), get_download_url(), delete_file()
        """
        if self._storage is None:
            self._storage = StorageResource(self._raw_storage_api, self._timeout)
        return self._storage

    @property
    def locations(self) -> LocationsResource:
        """Access public location ingest operations with clean API.

        Methods: ingest(), ingest_batch(), get_stats()

        This uses the public ingest API which accepts any device_id
        without requiring the device to be pre-registered.
        """
        if self._locations is None:
            self._locations = LocationsResource(self._raw_locations_api, self._timeout)
        return self._locations

    @property
    def integrations(self) -> IntegrationsResource:
        """Access integration operations with clean API.

        Methods: list(), create(), get(), update(), delete(), test(), create_webhook()

        Integrations are reusable service connections (webhooks, Slack, SMS, etc.)
        that can be used as actions in workflows.
        """
        if self._integrations is None:
            self._integrations = IntegrationsResource(
                self._raw_integrations_api, self._timeout
            )
        return self._integrations

    @property
    def workspaces(self) -> WorkspacesResource:
        """Access workspace operations with clean API.

        Methods: get(), update(), get_usage()

        Workspaces are the top-level organizational unit containing all resources.
        """
        if self._workspaces is None:
            self._workspaces = WorkspacesResource(
                self._raw_workspaces_api, self._timeout
            )
        return self._workspaces

    # -------------------------------------------------------------------------
    # Raw API access - For advanced use cases
    # -------------------------------------------------------------------------

    @property
    def _raw_geofences_api(self) -> GeofencesApi:
        """Get raw GeofencesApi (internal use)."""
        if self._raw_geofences is None:
            self._raw_geofences = GeofencesApi(self._api_client)
        return self._raw_geofences

    @property
    def _raw_workflows_api(self) -> WorkflowsApi:
        """Get raw WorkflowsApi (internal use)."""
        if self._raw_workflows is None:
            self._raw_workflows = WorkflowsApi(self._api_client)
        return self._raw_workflows

    @property
    def _raw_webhooks_api(self) -> WebhooksApi:
        """Get raw WebhooksApi (internal use)."""
        if self._raw_webhooks is None:
            self._raw_webhooks = WebhooksApi(self._api_client)
        return self._raw_webhooks

    @property
    def _raw_devices_api(self) -> DevicesApi:
        """Get raw DevicesApi (internal use)."""
        if self._raw_devices is None:
            self._raw_devices = DevicesApi(self._api_client)
        return self._raw_devices

    @property
    def _raw_account_api(self) -> AccountApi:
        """Get raw AccountApi (internal use)."""
        if self._raw_account is None:
            self._raw_account = AccountApi(self._api_client)
        return self._raw_account

    @property
    def _raw_storage_api(self) -> StorageApi:
        """Get raw StorageApi (internal use)."""
        if self._raw_storage is None:
            self._raw_storage = StorageApi(self._api_client)
        return self._raw_storage

    @property
    def _raw_locations_api(self) -> PublicLocationIngestApi:
        """Get raw PublicLocationIngestApi (internal use)."""
        if self._raw_locations is None:
            self._raw_locations = PublicLocationIngestApi(self._api_client)
        return self._raw_locations

    @property
    def _raw_integrations_api(self) -> IntegrationsApi:
        """Get raw IntegrationsApi (internal use)."""
        if self._raw_integrations is None:
            self._raw_integrations = IntegrationsApi(self._api_client)
        return self._raw_integrations

    @property
    def _raw_workspaces_api(self) -> WorkspacesApi:
        """Get raw WorkspacesApi (internal use)."""
        if self._raw_workspaces is None:
            self._raw_workspaces = WorkspacesApi(self._api_client)
        return self._raw_workspaces

    @property
    def _raw_authentication_api(self) -> AuthenticationApi:
        """Get raw AuthenticationApi (internal use)."""
        if self._raw_authentication is None:
            self._raw_authentication = AuthenticationApi(self._api_client)
        return self._raw_authentication

    @property
    def _raw_admin_api(self) -> AdminApi:
        """Get raw AdminApi (internal use)."""
        if self._raw_admin is None:
            self._raw_admin = AdminApi(self._api_client)
        return self._raw_admin

    @property
    def _raw_billing_api(self) -> BillingApi:
        """Get raw BillingApi (internal use)."""
        if self._raw_billing is None:
            self._raw_billing = BillingApi(self._api_client)
        return self._raw_billing

    @property
    def _raw_subscriptions_api(self) -> SubscriptionsApi:
        """Get raw SubscriptionsApi (internal use)."""
        if self._raw_subscriptions is None:
            self._raw_subscriptions = SubscriptionsApi(self._api_client)
        return self._raw_subscriptions

    @property
    def _raw_tiles_api(self) -> TilesApi:
        """Get raw TilesApi (internal use)."""
        if self._raw_tiles is None:
            self._raw_tiles = TilesApi(self._api_client)
        return self._raw_tiles

    @property
    def raw(self) -> "RawApiAccess":
        """Access raw generated APIs for advanced use cases.

        Use this when you need full control over API calls or access to
        endpoints not covered by the clean API.

        Example:
            >>> response = await client.raw.geofences.apps_geofences_api_list_geofences()
        """
        return RawApiAccess(self)

    @property
    def account(self) -> AccountResource:
        """Access account operations with clean API.

        Methods: get_profile(), update_profile(), list_api_keys(), create_api_key(),
                 get_dashboard_metrics(), get_onboarding_progress(), etc.
        """
        if self._account_resource is None:
            self._account_resource = AccountResource(
                self._raw_account_api, self._timeout
            )
        return self._account_resource

    async def close(self) -> None:
        """Close the API client and release resources."""
        # The generated ApiClient uses urllib3 pool manager which doesn't need explicit closing
        # This method is kept for API compatibility and future async implementations
        pass

    async def __aenter__(self) -> "SpatialFlow":
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Async context manager exit."""
        await self.close()


class RawApiAccess:
    """Provides access to raw generated APIs.

    This class exposes the original generated API methods for cases where
    you need full control or access to endpoints not covered by the clean API.
    """

    def __init__(self, client: SpatialFlow):
        self._client = client

    @property
    def geofences(self) -> GeofencesApi:
        """Access raw GeofencesApi."""
        return self._client._raw_geofences_api

    @property
    def workflows(self) -> WorkflowsApi:
        """Access raw WorkflowsApi."""
        return self._client._raw_workflows_api

    @property
    def webhooks(self) -> WebhooksApi:
        """Access raw WebhooksApi."""
        return self._client._raw_webhooks_api

    @property
    def devices(self) -> DevicesApi:
        """Access raw DevicesApi."""
        return self._client._raw_devices_api

    @property
    def account(self) -> AccountApi:
        """Access raw AccountApi."""
        return self._client._raw_account_api

    @property
    def storage(self) -> StorageApi:
        """Access raw StorageApi."""
        return self._client._raw_storage_api

    @property
    def locations(self) -> PublicLocationIngestApi:
        """Access raw PublicLocationIngestApi."""
        return self._client._raw_locations_api

    @property
    def integrations(self) -> IntegrationsApi:
        """Access raw IntegrationsApi."""
        return self._client._raw_integrations_api

    @property
    def workspaces(self) -> WorkspacesApi:
        """Access raw WorkspacesApi."""
        return self._client._raw_workspaces_api

    @property
    def authentication(self) -> AuthenticationApi:
        """Access raw AuthenticationApi."""
        return self._client._raw_authentication_api

    @property
    def admin(self) -> AdminApi:
        """Access raw AdminApi."""
        return self._client._raw_admin_api

    @property
    def billing(self) -> BillingApi:
        """Access raw BillingApi."""
        return self._client._raw_billing_api

    @property
    def subscriptions(self) -> SubscriptionsApi:
        """Access raw SubscriptionsApi."""
        return self._client._raw_subscriptions_api

    @property
    def tiles(self) -> TilesApi:
        """Access raw TilesApi."""
        return self._client._raw_tiles_api
