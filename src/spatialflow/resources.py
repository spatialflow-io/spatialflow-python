"""
Resource wrappers providing a cleaner API surface.

These wrappers provide:
- Simplified method names (list, create, get, update, delete)
- Default timeout applied to all calls
- Exception translation from generated exceptions to SDK exceptions
- Concrete return types for IDE autocomplete support
"""

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from .exceptions import translate_exception

if TYPE_CHECKING:
    from ._generated.spatialflow_generated.models import (
        # Account
        ApiKeyCreateRequest,
        ApiKeyCreateResponse,
        ApiKeyResponse,
        ApiKeyUpdateRequest,
        DashboardMetricsResponse,
        OnboardingProgressResponse,
        UpdateOnboardingProgressRequest,
        UpdateProfileRequest,
        UserProfileResponse,
        # Geofences
        AsyncUploadGeofencesResponse,
        BulkGeofenceRequest,
        CreateGeofenceRequest,
        GeofenceListResponse,
        GeofenceResponse,
        UpdateGeofenceRequest,
        UploadGeofencesRequest,
        UploadJobStatus,
        # Workflows
        ExecutionOut,
        WorkflowImportSchema,
        WorkflowIn,
        WorkflowListResponse,
        WorkflowOut,
        WorkflowRetryPolicyUpdateSchema,
        # Webhooks
        CreateWebhookRequest,
        TestWebhookRequest,
        UpdateWebhookRequest,
        WebhookDeliveryDetailResponse,
        WebhookDeliveryListResponse,
        WebhookDeliveryResponse,
        WebhookListResponse,
        WebhookMetricsResponse,
        WebhookResponse,
        WebhookTestResponse,
        # Devices
        DeviceIn,
        DeviceOut,
        LocationUpdateIn,
        LocationUpdateOut,
        # Storage
        DeleteFileResponse,
        FileListResponse,
        PresignedUrlRequest,
        PresignedUrlResponse,
        # Locations
        LocationIngestResponse,
        # Workspaces
        UsageResponse,
        WorkspaceIn,
        WorkspaceOut,
        # Integrations
        CreateIntegrationSchema,
        IntegrationResponseSchema,
        TestIntegrationResponseSchema,
        UpdateIntegrationSchema,
    )


class BaseResource:
    """Base class for resource wrappers."""

    def __init__(self, api: Any, timeout: int):
        self._api = api
        self._timeout = timeout

    async def _call(self, method: str, **kwargs: Any) -> Any:
        """Call an API method with timeout and exception translation."""
        api_method = getattr(self._api, method)
        try:
            return await api_method(_request_timeout=self._timeout, **kwargs)
        except Exception as e:
            raise translate_exception(e) from e


class GeofencesResource(BaseResource):
    """Geofence operations with clean API."""

    async def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        group_id: Optional[str] = None,
        **kwargs: Any,
    ) -> GeofenceListResponse:
        """List geofences.

        Args:
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)
            group_id: Filter by group ID
            **kwargs: Additional filter parameters

        Returns:
            GeofenceListResponse with geofences and count
        """
        call_kwargs: Dict[str, Any] = {"limit": limit, "offset": offset, **kwargs}
        if group_id is not None:
            call_kwargs["group_id"] = group_id
        return await self._call("apps_geofences_api_list_geofences", **call_kwargs)

    async def create(
        self, request: CreateGeofenceRequest, **kwargs: Any
    ) -> GeofenceResponse:
        """Create a geofence.

        Args:
            request: CreateGeofenceRequest with name, geometry, etc.
            **kwargs: Additional parameters

        Returns:
            GeofenceResponse
        """
        return await self._call(
            "apps_geofences_api_create_geofence",
            create_geofence_request=request,
            **kwargs,
        )

    async def get(self, geofence_id: str, **kwargs: Any) -> GeofenceResponse:
        """Get a geofence by ID.

        Args:
            geofence_id: The geofence ID

        Returns:
            GeofenceResponse
        """
        return await self._call(
            "apps_geofences_api_get_geofence",
            geofence_id=geofence_id,
            **kwargs,
        )

    async def update(
        self, geofence_id: str, request: UpdateGeofenceRequest, **kwargs: Any
    ) -> GeofenceResponse:
        """Update a geofence.

        Args:
            geofence_id: The geofence ID
            request: UpdateGeofenceRequest with fields to update
            **kwargs: Additional parameters

        Returns:
            GeofenceResponse
        """
        return await self._call(
            "apps_geofences_api_update_geofence",
            geofence_id=geofence_id,
            update_geofence_request=request,
            **kwargs,
        )

    async def delete(self, geofence_id: str, **kwargs: Any) -> None:
        """Delete a geofence.

        Args:
            geofence_id: The geofence ID
        """
        return await self._call(
            "apps_geofences_api_delete_geofence",
            geofence_id=geofence_id,
            **kwargs,
        )

    async def bulk_create(
        self, request: BulkGeofenceRequest, **kwargs: Any
    ) -> List[GeofenceResponse]:
        """Bulk create geofences.

        Args:
            request: BulkGeofenceRequest with list of geofences
            **kwargs: Additional parameters

        Returns:
            List of GeofenceResponse objects
        """
        return await self._call(
            "apps_geofences_api_bulk_create_geofences",
            bulk_geofence_request=request,
            **kwargs,
        )

    async def upload(
        self, request: UploadGeofencesRequest, **kwargs: Any
    ) -> AsyncUploadGeofencesResponse:
        """Start async geofence upload from file.

        Args:
            request: UploadGeofencesRequest with file_id
            **kwargs: Additional parameters

        Returns:
            AsyncUploadGeofencesResponse with job_id
        """
        return await self._call(
            "apps_geofences_api_upload_geofences_async",
            upload_geofences_request=request,
            **kwargs,
        )

    async def get_upload_status(self, job_id: str, **kwargs: Any) -> UploadJobStatus:
        """Get upload job status.

        Args:
            job_id: The upload job ID

        Returns:
            UploadJobStatus
        """
        return await self._call(
            "apps_geofences_api_get_upload_job_status",
            job_id=job_id,
            **kwargs,
        )

    async def create_with_group(
        self,
        name: str,
        geometry: Dict[str, Any],
        group_name: str,
        *,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> GeofenceResponse:
        """Create a geofence with group assignment.

        The group_id is auto-generated by the backend based on the group_name.
        All geofences with the same group_name will share the same group_id.

        Args:
            name: Geofence name
            geometry: GeoJSON geometry (Polygon or MultiPolygon)
            group_name: Group name for organization
            description: Optional description
            metadata: Optional metadata dict

        Returns:
            GeofenceResponse
        """
        from ._generated.spatialflow_generated.models import CreateGeofenceRequest

        request = CreateGeofenceRequest(
            name=name,
            geometry=geometry,
            group_name=group_name,
            description=description,
            metadata=metadata or {},
        )

        return await self.create(request, **kwargs)

    async def list_by_group(
        self,
        group_id: str,
        *,
        limit: int = 100,
        offset: int = 0,
        **kwargs: Any,
    ) -> GeofenceListResponse:
        """List all geofences in a specific group.

        Args:
            group_id: The group UUID
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)

        Returns:
            GeofenceListResponse with geofences and count
        """
        return await self.list(
            limit=limit,
            offset=offset,
            group_id=group_id,
            **kwargs,
        )


class WorkflowsResource(BaseResource):
    """Workflow operations with clean API."""

    async def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        **kwargs: Any,
    ) -> WorkflowListResponse:
        """List workflows.

        Args:
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)
            **kwargs: Additional filter parameters

        Returns:
            WorkflowListResponse with workflows and count
        """
        return await self._call(
            "apps_workflows_api_list_workflows",
            limit=limit,
            offset=offset,
            **kwargs,
        )

    async def create(self, request: WorkflowIn, **kwargs: Any) -> WorkflowOut:
        """Create a workflow.

        Args:
            request: WorkflowIn with name, nodes, edges, etc.
            **kwargs: Additional parameters

        Returns:
            WorkflowOut
        """
        return await self._call(
            "apps_workflows_api_create_workflow",
            workflow_in=request,
            **kwargs,
        )

    async def get(self, workflow_id: str, **kwargs: Any) -> WorkflowOut:
        """Get a workflow by ID.

        Args:
            workflow_id: The workflow ID

        Returns:
            WorkflowOut
        """
        return await self._call(
            "apps_workflows_api_get_workflow",
            workflow_id=workflow_id,
            **kwargs,
        )

    async def update(
        self, workflow_id: str, request: WorkflowIn, **kwargs: Any
    ) -> WorkflowOut:
        """Update a workflow.

        Args:
            workflow_id: The workflow ID
            request: WorkflowIn with updated fields
            **kwargs: Additional parameters

        Returns:
            WorkflowOut
        """
        return await self._call(
            "apps_workflows_api_update_workflow",
            workflow_id=workflow_id,
            workflow_in=request,
            **kwargs,
        )

    async def delete(self, workflow_id: str, **kwargs: Any) -> None:
        """Delete a workflow.

        Args:
            workflow_id: The workflow ID
        """
        return await self._call(
            "apps_workflows_api_delete_workflow",
            workflow_id=workflow_id,
            **kwargs,
        )

    async def toggle(self, workflow_id: str, **kwargs: Any) -> WorkflowOut:
        """Toggle workflow between active and paused states.

        Note: Cannot toggle a draft workflow. Use activate() first.

        Args:
            workflow_id: The workflow ID

        Returns:
            WorkflowOut
        """
        return await self._call(
            "apps_workflows_api_toggle_workflow",
            workflow_id=workflow_id,
            **kwargs,
        )

    async def activate(self, workflow_id: str, **kwargs: Any) -> WorkflowOut:
        """Activate a draft workflow for production use.

        Transitions a workflow from draft status (is_test_mode=True) to active
        status (is_active=True, is_test_mode=False).

        This operation is idempotent: calling activate on an already active
        workflow returns 200 without making changes.

        Args:
            workflow_id: The workflow ID

        Returns:
            WorkflowOut

        Raises:
            SpatialFlowError: If workflow validation fails (no trigger/steps)
        """
        return await self._call(
            "apps_workflows_api_activate_workflow",
            workflow_id=workflow_id,
            **kwargs,
        )

    # -------------------------------------------------------------------------
    # Execution methods
    # -------------------------------------------------------------------------

    async def execute(
        self, workflow_id: str, request: Optional[Any] = None, **kwargs: Any
    ) -> ExecutionOut:
        """Execute a workflow.

        Args:
            workflow_id: The workflow ID
            request: WorkflowExecutionRequest with execution parameters

        Returns:
            ExecutionOut
        """
        return await self._call(
            "apps_workflows_api_execute_workflow",
            workflow_id=workflow_id,
            workflow_execution_request=request,
            **kwargs,
        )

    async def test(
        self, workflow_id: str, request: Optional[Any] = None, **kwargs: Any
    ) -> ExecutionOut:
        """Test a workflow with sample data.

        Args:
            workflow_id: The workflow ID
            request: WorkflowTestRequest with test parameters

        Returns:
            ExecutionOut
        """
        return await self._call(
            "apps_workflows_api_test_workflow",
            workflow_id=workflow_id,
            workflow_test_request=request,
            **kwargs,
        )

    async def list_executions(
        self,
        workflow_id: str,
        *,
        limit: int = 100,
        offset: int = 0,
        **kwargs: Any,
    ) -> List[ExecutionOut]:
        """List executions for a specific workflow.

        Args:
            workflow_id: The workflow ID
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)

        Returns:
            List of ExecutionOut
        """
        return await self._call(
            "apps_workflows_api_get_workflow_executions",
            workflow_id=workflow_id,
            limit=limit,
            offset=offset,
            **kwargs,
        )

    async def get_execution(
        self, workflow_id: str, execution_id: str, **kwargs: Any
    ) -> ExecutionOut:
        """Get details of a specific workflow execution.

        Args:
            workflow_id: The workflow ID
            execution_id: The execution ID

        Returns:
            ExecutionOut
        """
        return await self._call(
            "apps_workflows_api_get_workflow_execution_detail",
            workflow_id=workflow_id,
            execution_id=execution_id,
            **kwargs,
        )

    # -------------------------------------------------------------------------
    # Performance and statistics methods
    # -------------------------------------------------------------------------

    async def get_performance(self, workflow_id: str, **kwargs: Any) -> Dict[str, Any]:
        """Get workflow performance metrics.

        Args:
            workflow_id: The workflow ID

        Returns:
            Performance metrics dict
        """
        return await self._call(
            "apps_workflows_api_get_workflow_performance",
            workflow_id=workflow_id,
            **kwargs,
        )

    async def get_statistics(self, workflow_id: str, **kwargs: Any) -> Dict[str, Any]:
        """Get workflow statistics.

        Args:
            workflow_id: The workflow ID

        Returns:
            Statistics dict
        """
        return await self._call(
            "apps_workflows_api_get_workflow_statistics",
            workflow_id=workflow_id,
            **kwargs,
        )

    # -------------------------------------------------------------------------
    # Versioning methods
    # -------------------------------------------------------------------------

    async def list_versions(
        self, workflow_id: str, **kwargs: Any
    ) -> List[Dict[str, Any]]:
        """List versions of a workflow.

        Args:
            workflow_id: The workflow ID

        Returns:
            List of workflow versions
        """
        return await self._call(
            "apps_workflows_api_list_workflow_versions",
            workflow_id=workflow_id,
            **kwargs,
        )

    async def restore_version(
        self, workflow_id: str, version_number: int, **kwargs: Any
    ) -> WorkflowOut:
        """Restore a previous version of a workflow.

        Args:
            workflow_id: The workflow ID
            version_number: The version number to restore

        Returns:
            WorkflowOut
        """
        return await self._call(
            "apps_workflows_api_restore_workflow_version",
            workflow_id=workflow_id,
            version_number=version_number,
            **kwargs,
        )

    # -------------------------------------------------------------------------
    # Import/Export and duplication methods
    # -------------------------------------------------------------------------

    async def duplicate(
        self, workflow_id: str, request: Optional[Any] = None, **kwargs: Any
    ) -> WorkflowOut:
        """Duplicate an existing workflow.

        Args:
            workflow_id: The workflow ID
            request: WorkflowDuplicateRequest with new name, etc.

        Returns:
            WorkflowOut
        """
        return await self._call(
            "apps_workflows_api_duplicate_workflow",
            workflow_id=workflow_id,
            workflow_duplicate_request=request,
            **kwargs,
        )

    async def export_workflow(
        self, workflow_id: str, **kwargs: Any
    ) -> Dict[str, Any]:
        """Export workflow as JSON.

        Args:
            workflow_id: The workflow ID

        Returns:
            Workflow export data (JSON-serializable)
        """
        return await self._call(
            "apps_workflows_api_export_workflow",
            workflow_id=workflow_id,
            **kwargs,
        )

    async def import_workflow(
        self, request: WorkflowImportSchema, **kwargs: Any
    ) -> WorkflowOut:
        """Import workflow from JSON.

        Args:
            request: WorkflowImportSchema with workflow data

        Returns:
            WorkflowOut
        """
        return await self._call(
            "apps_workflows_api_import_workflow",
            workflow_import_request=request,
            **kwargs,
        )

    async def get_retry_policy(
        self, workflow_id: str, **kwargs: Any
    ) -> Dict[str, Any]:
        """Get retry policy for a workflow.

        Args:
            workflow_id: The workflow ID

        Returns:
            Retry policy configuration
        """
        return await self._call(
            "apps_workflows_api_get_workflow_retry_policy",
            workflow_id=workflow_id,
            **kwargs,
        )

    async def update_retry_policy(
        self,
        workflow_id: str,
        request: WorkflowRetryPolicyUpdateSchema,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """Update retry policy for a workflow.

        Args:
            workflow_id: The workflow ID
            request: WorkflowRetryPolicyUpdateSchema with retry settings

        Returns:
            Updated retry policy configuration
        """
        return await self._call(
            "apps_workflows_api_update_workflow_retry_policy",
            workflow_id=workflow_id,
            workflow_retry_policy_request=request,
            **kwargs,
        )

    async def list_all_executions(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        **kwargs: Any,
    ) -> List[ExecutionOut]:
        """List all workflow executions across the workspace.

        Args:
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)

        Returns:
            List of ExecutionOut
        """
        return await self._call(
            "apps_workflows_api_list_workflow_executions",
            limit=limit,
            offset=offset,
            **kwargs,
        )

    async def get_bottlenecks(
        self, workflow_id: str, **kwargs: Any
    ) -> Dict[str, Any]:
        """Get workflow bottleneck analysis.

        Args:
            workflow_id: The workflow ID

        Returns:
            Bottleneck analysis data
        """
        return await self._call(
            "apps_workflows_api_get_workflow_bottlenecks",
            workflow_id=workflow_id,
            **kwargs,
        )

    async def get_step_performance(
        self, workflow_id: str, **kwargs: Any
    ) -> Dict[str, Any]:
        """Get performance metrics for each workflow step.

        Args:
            workflow_id: The workflow ID

        Returns:
            Step performance metrics
        """
        return await self._call(
            "apps_workflows_api_get_workflow_step_performance",
            workflow_id=workflow_id,
            **kwargs,
        )


class WebhooksResource(BaseResource):
    """Webhook operations with clean API."""

    async def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        **kwargs: Any,
    ) -> WebhookListResponse:
        """List webhooks.

        Args:
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)
            **kwargs: Additional filter parameters

        Returns:
            WebhookListResponse with webhooks and count
        """
        return await self._call(
            "apps_webhooks_api_list_webhooks",
            limit=limit,
            offset=offset,
            **kwargs,
        )

    async def create(
        self, request: CreateWebhookRequest, **kwargs: Any
    ) -> WebhookResponse:
        """Create a webhook.

        Args:
            request: CreateWebhookRequest with url, events, etc.
            **kwargs: Additional parameters

        Returns:
            WebhookResponse
        """
        return await self._call(
            "apps_webhooks_api_create_webhook",
            create_webhook_request=request,
            **kwargs,
        )

    async def get(self, webhook_id: str, **kwargs: Any) -> WebhookResponse:
        """Get a webhook by ID.

        Args:
            webhook_id: The webhook ID

        Returns:
            WebhookResponse
        """
        return await self._call(
            "apps_webhooks_api_get_webhook",
            webhook_id=webhook_id,
            **kwargs,
        )

    async def update(
        self, webhook_id: str, request: UpdateWebhookRequest, **kwargs: Any
    ) -> WebhookResponse:
        """Update a webhook.

        Args:
            webhook_id: The webhook ID
            request: UpdateWebhookRequest with fields to update
            **kwargs: Additional parameters

        Returns:
            WebhookResponse
        """
        return await self._call(
            "apps_webhooks_api_update_webhook",
            webhook_id=webhook_id,
            update_webhook_request=request,
            **kwargs,
        )

    async def delete(self, webhook_id: str, **kwargs: Any) -> None:
        """Delete a webhook.

        Args:
            webhook_id: The webhook ID
        """
        return await self._call(
            "apps_webhooks_api_delete_webhook",
            webhook_id=webhook_id,
            **kwargs,
        )

    async def rotate_secret(self, webhook_id: str, **kwargs: Any) -> WebhookResponse:
        """Rotate webhook signing secret.

        Args:
            webhook_id: The webhook ID

        Returns:
            WebhookResponse with new secret
        """
        return await self._call(
            "apps_webhooks_api_rotate_webhook_secret",
            webhook_id=webhook_id,
            **kwargs,
        )

    # -------------------------------------------------------------------------
    # Delivery tracking methods
    # -------------------------------------------------------------------------

    async def list_deliveries(
        self,
        webhook_id: str,
        *,
        limit: int = 100,
        offset: int = 0,
        **kwargs: Any,
    ) -> WebhookDeliveryListResponse:
        """List delivery history for a webhook.

        Args:
            webhook_id: The webhook ID
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)

        Returns:
            WebhookDeliveryListResponse
        """
        return await self._call(
            "apps_webhooks_api_get_webhook_deliveries",
            webhook_id=webhook_id,
            limit=limit,
            offset=offset,
            **kwargs,
        )

    async def get_delivery(
        self, webhook_id: str, delivery_id: str, **kwargs: Any
    ) -> WebhookDeliveryDetailResponse:
        """Get details of a specific webhook delivery.

        Args:
            webhook_id: The webhook ID
            delivery_id: The delivery ID

        Returns:
            WebhookDeliveryDetailResponse
        """
        return await self._call(
            "apps_webhooks_api_get_webhook_delivery_detail",
            webhook_id=webhook_id,
            delivery_id=delivery_id,
            **kwargs,
        )

    async def retry_delivery(
        self, webhook_id: str, delivery_id: str, **kwargs: Any
    ) -> WebhookDeliveryResponse:
        """Retry a failed webhook delivery.

        Args:
            webhook_id: The webhook ID
            delivery_id: The delivery ID

        Returns:
            WebhookDeliveryResponse
        """
        return await self._call(
            "apps_webhooks_api_retry_webhook_delivery",
            webhook_id=webhook_id,
            delivery_id=delivery_id,
            **kwargs,
        )

    # -------------------------------------------------------------------------
    # Metrics and monitoring methods
    # -------------------------------------------------------------------------

    async def get_metrics(self, webhook_id: str, **kwargs: Any) -> WebhookMetricsResponse:
        """Get performance metrics for a webhook.

        Args:
            webhook_id: The webhook ID

        Returns:
            WebhookMetricsResponse
        """
        return await self._call(
            "apps_webhooks_api_get_webhook_metrics",
            webhook_id=webhook_id,
            **kwargs,
        )

    async def get_success_timeline(
        self, webhook_id: str, **kwargs: Any
    ) -> Dict[str, Any]:
        """Get success/failure timeline for webhook deliveries.

        Args:
            webhook_id: The webhook ID

        Returns:
            Success timeline data
        """
        return await self._call(
            "apps_webhooks_api_get_webhook_success_timeline",
            webhook_id=webhook_id,
            **kwargs,
        )

    # -------------------------------------------------------------------------
    # Dead Letter Queue (DLQ) methods
    # -------------------------------------------------------------------------

    async def list_dlq_entries(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        **kwargs: Any,
    ) -> List[Dict[str, Any]]:
        """List Dead Letter Queue entries.

        Args:
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)

        Returns:
            List of DLQ entries
        """
        return await self._call(
            "apps_webhooks_api_list_dlq_entries",
            limit=limit,
            offset=offset,
            **kwargs,
        )

    async def retry_dlq(self, dlq_entry_id: str, **kwargs: Any) -> Dict[str, Any]:
        """Retry a failed webhook from the Dead Letter Queue.

        Args:
            dlq_entry_id: The DLQ entry ID

        Returns:
            Retry result
        """
        return await self._call(
            "apps_webhooks_api_retry_from_dlq",
            dlq_entry_id=dlq_entry_id,
            **kwargs,
        )

    async def test(
        self, webhook_id: str, request: Optional[TestWebhookRequest] = None, **kwargs: Any
    ) -> WebhookTestResponse:
        """Test a webhook with sample data.

        Args:
            webhook_id: The webhook ID
            request: TestWebhookRequest with test payload (optional, defaults to empty)

        Returns:
            WebhookTestResponse
        """
        # The API requires a request body, use empty dict if not provided
        test_request = request if request is not None else {}
        return await self._call(
            "apps_webhooks_api_test_webhook",
            webhook_id=webhook_id,
            test_webhook_request=test_request,
            **kwargs,
        )


class DevicesResource(BaseResource):
    """Device operations with clean API."""

    async def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        **kwargs: Any,
    ) -> List[DeviceOut]:
        """List devices.

        Args:
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)
            **kwargs: Additional filter parameters

        Returns:
            List of DeviceOut
        """
        return await self._call(
            "apps_devices_api_list_devices",
            limit=limit,
            offset=offset,
            **kwargs,
        )

    async def create(self, request: DeviceIn, **kwargs: Any) -> DeviceOut:
        """Create a device.

        Args:
            request: DeviceIn with device_id, name, etc.
            **kwargs: Additional parameters

        Returns:
            DeviceOut
        """
        return await self._call(
            "apps_devices_api_create_device",
            create_device_request=request,
            **kwargs,
        )

    async def get(self, device_id: str, **kwargs: Any) -> DeviceOut:
        """Get a device by ID.

        Args:
            device_id: The device ID

        Returns:
            DeviceOut
        """
        return await self._call(
            "apps_devices_api_get_device",
            device_id=device_id,
            **kwargs,
        )

    async def update(
        self, device_id: str, request: DeviceIn, **kwargs: Any
    ) -> DeviceOut:
        """Update a device.

        Args:
            device_id: The device ID
            request: DeviceIn with fields to update
            **kwargs: Additional parameters

        Returns:
            DeviceOut
        """
        return await self._call(
            "apps_devices_api_update_device",
            device_id=device_id,
            update_device_request=request,
            **kwargs,
        )

    async def delete(self, device_id: str, **kwargs: Any) -> None:
        """Delete a device.

        Args:
            device_id: The device ID
        """
        return await self._call(
            "apps_devices_api_delete_device",
            device_id=device_id,
            **kwargs,
        )

    async def update_location(
        self, device_id: str, request: LocationUpdateIn, **kwargs: Any
    ) -> LocationUpdateOut:
        """Update device location.

        Args:
            device_id: The device ID
            request: LocationUpdateIn with lat, lng, timestamp
            **kwargs: Additional parameters

        Returns:
            LocationUpdateOut
        """
        return await self._call(
            "apps_devices_api_update_device_location",
            device_id=device_id,
            location_update_request=request,
            **kwargs,
        )


class StorageResource(BaseResource):
    """Storage operations with clean API."""

    async def create_presigned_url(
        self, request: PresignedUrlRequest, **kwargs: Any
    ) -> PresignedUrlResponse:
        """Create a presigned URL for file upload.

        Args:
            request: PresignedUrlRequest with filename, content_type
            **kwargs: Additional parameters

        Returns:
            PresignedUrlResponse with upload_url and file_id
        """
        return await self._call(
            "apps_storage_api_create_presigned_url",
            presigned_url_request=request,
            **kwargs,
        )

    async def list_files(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        **kwargs: Any,
    ) -> FileListResponse:
        """List uploaded files.

        Args:
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)
            **kwargs: Additional filter parameters

        Returns:
            FileListResponse with files and count
        """
        return await self._call(
            "apps_storage_api_list_files",
            limit=limit,
            offset=offset,
            **kwargs,
        )

    async def get_download_url(self, file_id: str, **kwargs: Any) -> Dict[str, str]:
        """Get presigned download URL for a file.

        Args:
            file_id: The file ID

        Returns:
            Dict with download_url
        """
        return await self._call(
            "apps_storage_api_get_download_url",
            file_id=file_id,
            **kwargs,
        )

    async def delete_file(self, file_id: str, **kwargs: Any) -> DeleteFileResponse:
        """Delete a file.

        Args:
            file_id: The file ID

        Returns:
            DeleteFileResponse
        """
        return await self._call(
            "apps_storage_api_delete_file",
            file_id=file_id,
            **kwargs,
        )


class LocationsResource(BaseResource):
    """Public location ingestion API.

    This resource provides access to the public location ingest endpoints,
    which accept location data from any device without requiring pre-registration.
    """

    async def ingest(
        self,
        device_id: str,
        lat: float,
        lon: float,
        timestamp: Optional[datetime] = None,
        *,
        accuracy: Optional[float] = None,
        speed: Optional[float] = None,
        heading: Optional[float] = None,
        altitude: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> LocationIngestResponse:
        """Ingest a single location point.

        This uses the public ingest API which accepts any device_id
        without requiring the device to be pre-registered.

        Args:
            device_id: Unique identifier for the device
            lat: Latitude in decimal degrees
            lon: Longitude in decimal degrees
            timestamp: Event timestamp (defaults to now)
            accuracy: GPS accuracy in meters
            speed: Speed in m/s
            heading: Heading in degrees (0-360)
            altitude: Altitude in meters
            metadata: Additional metadata dict

        Returns:
            LocationIngestResponse
        """
        from ._generated.spatialflow_generated.models import LocationPointIn

        ts = timestamp if timestamp else datetime.utcnow()

        request = LocationPointIn(
            device_id=device_id,
            lat=lat,
            lon=lon,
            ts=ts,
            accuracy=accuracy,
            speed=speed,
            heading=heading,
            altitude=altitude,
            metadata=metadata,
        )

        return await self._call(
            "apps_public_locations_api_ingest_location",
            location_point_in=request,
        )

    async def ingest_batch(
        self,
        locations: List[Dict[str, Any]],
        idempotency_key: Optional[str] = None,
    ) -> LocationIngestResponse:
        """Ingest a batch of location points (up to 5000).

        Args:
            locations: List of location dicts with device_id, lat, lon, ts
            idempotency_key: Optional key for deduplication (24hr window)

        Returns:
            LocationIngestResponse with counts
        """
        from ._generated.spatialflow_generated.models import LocationBatchIn

        request = LocationBatchIn(
            locations=locations,
            idempotency_key=idempotency_key,
        )

        return await self._call(
            "apps_public_locations_api_ingest_location_batch",
            location_batch_in=request,
        )

    async def get_stats(self, **kwargs: Any) -> Dict[str, Any]:
        """Get location ingestion statistics.

        Returns:
            Dict with total_ingested_today, total_ingested_week, etc.
        """
        return await self._call(
            "apps_public_locations_api_get_ingest_stats",
            **kwargs,
        )


class WorkspacesResource(BaseResource):
    """Workspace operations with clean API.

    Workspaces are the top-level organizational unit in SpatialFlow.
    Each user belongs to a workspace that contains all their resources.
    """

    async def get(self, **kwargs: Any) -> WorkspaceOut:
        """Get the current workspace.

        Returns:
            WorkspaceOut with id, name, slug, settings, etc.
        """
        return await self._call(
            "apps_workspaces_api_get_workspace",
            **kwargs,
        )

    async def update(self, request: WorkspaceIn, **kwargs: Any) -> WorkspaceOut:
        """Update workspace settings.

        Args:
            request: WorkspaceIn with fields to update

        Returns:
            WorkspaceOut
        """
        return await self._call(
            "apps_workspaces_api_update_workspace",
            workspace_in=request,
            **kwargs,
        )

    async def get_usage(self, **kwargs: Any) -> UsageResponse:
        """Get current billing period usage metrics.

        Returns usage for the current billing period including:
        - Location events count
        - Action deliveries count
        - Event units (locations + 0.5 * actions)
        - Tier and tier limit

        Returns:
            UsageResponse with location_events, action_deliveries, event_units, etc.
        """
        return await self._call(
            "apps_workspaces_api_get_workspace_usage",
            **kwargs,
        )


class IntegrationsResource(BaseResource):
    """Integration operations with clean API.

    Integrations are reusable service connections (webhooks, Slack, SMS, etc.)
    that can be used as actions in workflows.
    """

    async def list(
        self,
        *,
        limit: int = 100,
        offset: int = 0,
        integration_type: Optional[str] = None,
        **kwargs: Any,
    ) -> List[IntegrationResponseSchema]:
        """List integrations.

        Args:
            limit: Maximum number of results (default 100)
            offset: Number of results to skip (default 0)
            integration_type: Optional filter by type (webhook, slack, etc.)

        Returns:
            List of IntegrationResponseSchema
        """
        return await self._call(
            "apps_integrations_api_list_integrations",
            limit=limit,
            offset=offset,
            integration_type=integration_type,
            **kwargs,
        )

    async def create(
        self, request: CreateIntegrationSchema, **kwargs: Any
    ) -> IntegrationResponseSchema:
        """Create an integration.

        Args:
            request: CreateIntegrationSchema with name, type, config

        Returns:
            IntegrationResponseSchema
        """
        return await self._call(
            "apps_integrations_api_create_integration",
            create_integration_schema=request,
            **kwargs,
        )

    async def get(self, integration_id: str, **kwargs: Any) -> IntegrationResponseSchema:
        """Get an integration by ID.

        Args:
            integration_id: The integration ID

        Returns:
            IntegrationResponseSchema
        """
        return await self._call(
            "apps_integrations_api_get_integration",
            integration_id=integration_id,
            **kwargs,
        )

    async def update(
        self, integration_id: str, request: UpdateIntegrationSchema, **kwargs: Any
    ) -> IntegrationResponseSchema:
        """Update an integration.

        Args:
            integration_id: The integration ID
            request: UpdateIntegrationSchema with fields to update

        Returns:
            IntegrationResponseSchema
        """
        return await self._call(
            "apps_integrations_api_update_integration",
            integration_id=integration_id,
            update_integration_schema=request,
            **kwargs,
        )

    async def delete(self, integration_id: str, **kwargs: Any) -> None:
        """Delete an integration.

        Args:
            integration_id: The integration ID
        """
        return await self._call(
            "apps_integrations_api_delete_integration",
            integration_id=integration_id,
            **kwargs,
        )

    async def test(
        self, integration_id: str, **kwargs: Any
    ) -> TestIntegrationResponseSchema:
        """Test an integration.

        Args:
            integration_id: The integration ID

        Returns:
            TestIntegrationResponseSchema with status
        """
        return await self._call(
            "apps_integrations_api_test_integration",
            integration_id=integration_id,
            **kwargs,
        )

    async def create_webhook(
        self,
        name: str,
        url: str,
        *,
        method: str = "POST",
        headers: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> IntegrationResponseSchema:
        """Convenience method to create a webhook integration.

        Args:
            name: Integration name
            url: Webhook URL
            method: HTTP method (default: POST)
            headers: Optional HTTP headers
            description: Optional description
            tags: Optional tags list

        Returns:
            IntegrationResponseSchema with id, name, type, config
        """
        from ._generated.spatialflow_generated.models import CreateIntegrationSchema

        config = {
            "url": url,
            "method": method,
            "headers": headers or {"Content-Type": "application/json"},
        }

        request = CreateIntegrationSchema(
            name=name,
            type="webhook",
            description=description,
            config=config,
            tags=tags,
        )

        return await self.create(request)


class AccountResource(BaseResource):
    """Account operations with clean API.

    Provides access to user profile, API key management, dashboard metrics,
    and onboarding progress.
    """

    # -------------------------------------------------------------------------
    # User Profile
    # -------------------------------------------------------------------------

    async def get_profile(self, **kwargs: Any) -> UserProfileResponse:
        """Get the current user's profile.

        Returns:
            UserProfileResponse with id, email, name, etc.
        """
        return await self._call(
            "apps_accounts_api_get_user_profile",
            **kwargs,
        )

    async def update_profile(
        self, request: UpdateProfileRequest, **kwargs: Any
    ) -> UserProfileResponse:
        """Update the current user's profile.

        Args:
            request: UpdateProfileRequest with profile fields to update (name, etc.)

        Returns:
            UserProfileResponse
        """
        return await self._call(
            "apps_accounts_api_update_user_profile",
            update_profile_request=request,
            **kwargs,
        )

    # -------------------------------------------------------------------------
    # API Keys
    # -------------------------------------------------------------------------

    async def list_api_keys(self, **kwargs: Any) -> List[ApiKeyResponse]:
        """List all API keys for the current user.

        Returns:
            List of ApiKeyResponse objects
        """
        return await self._call(
            "apps_accounts_api_get_api_keys",
            **kwargs,
        )

    async def get_api_key(self, key_id: str, **kwargs: Any) -> ApiKeyResponse:
        """Get a specific API key.

        Args:
            key_id: The API key ID

        Returns:
            ApiKeyResponse
        """
        return await self._call(
            "apps_accounts_api_get_api_key",
            api_key_id=key_id,
            **kwargs,
        )

    async def create_api_key(
        self, request: ApiKeyCreateRequest, **kwargs: Any
    ) -> ApiKeyCreateResponse:
        """Create a new API key.

        Args:
            request: ApiKeyCreateRequest with name and optional expires_at

        Returns:
            ApiKeyCreateResponse with key (only shown once)
        """
        return await self._call(
            "apps_accounts_api_create_api_key",
            api_key_create_request=request,
            **kwargs,
        )

    async def update_api_key(
        self, key_id: str, request: ApiKeyUpdateRequest, **kwargs: Any
    ) -> ApiKeyResponse:
        """Update an API key.

        Args:
            key_id: The API key ID
            request: ApiKeyUpdateRequest with fields to update (name, etc.)

        Returns:
            ApiKeyResponse
        """
        return await self._call(
            "apps_accounts_api_update_api_key",
            api_key_id=key_id,
            api_key_update_request=request,
            **kwargs,
        )

    async def delete_api_key(self, key_id: str, **kwargs: Any) -> None:
        """Delete an API key.

        Args:
            key_id: The API key ID
        """
        return await self._call(
            "apps_accounts_api_delete_api_key",
            api_key_id=key_id,
            **kwargs,
        )

    async def rotate_api_key(self, key_id: str, **kwargs: Any) -> ApiKeyCreateResponse:
        """Rotate an API key (generates new key value).

        Args:
            key_id: The API key ID

        Returns:
            ApiKeyCreateResponse with new key (only shown once)
        """
        return await self._call(
            "apps_accounts_api_rotate_api_key",
            api_key_id=key_id,
            **kwargs,
        )

    # -------------------------------------------------------------------------
    # Dashboard and Onboarding
    # -------------------------------------------------------------------------

    async def get_dashboard_metrics(self, **kwargs: Any) -> DashboardMetricsResponse:
        """Get dashboard metrics for the current user.

        Returns:
            DashboardMetricsResponse with counts, recent activity, etc.
        """
        return await self._call(
            "apps_accounts_api_get_dashboard_metrics",
            **kwargs,
        )

    async def get_onboarding_progress(
        self, **kwargs: Any
    ) -> OnboardingProgressResponse:
        """Get onboarding progress for the current user.

        Returns:
            OnboardingProgressResponse with completed steps, next steps, etc.
        """
        return await self._call(
            "apps_accounts_api_get_onboarding_progress",
            **kwargs,
        )

    async def update_onboarding_progress(
        self, request: UpdateOnboardingProgressRequest, **kwargs: Any
    ) -> OnboardingProgressResponse:
        """Update onboarding progress.

        Args:
            request: UpdateOnboardingProgressRequest with completed steps, etc.

        Returns:
            OnboardingProgressResponse
        """
        return await self._call(
            "apps_accounts_api_update_onboarding_progress",
            update_onboarding_progress_request=request,
            **kwargs,
        )

    async def dismiss_onboarding(self, **kwargs: Any) -> None:
        """Dismiss the onboarding flow."""
        return await self._call(
            "apps_accounts_api_dismiss_onboarding",
            **kwargs,
        )

    # -------------------------------------------------------------------------
    # Notifications
    # -------------------------------------------------------------------------

    async def get_notifications(self, **kwargs: Any) -> List[Dict[str, Any]]:
        """Get notifications for the current user.

        Returns:
            List of notification dicts
        """
        return await self._call(
            "apps_accounts_api_get_notifications",
            **kwargs,
        )

    async def mark_notification_read(
        self, notification_id: str, **kwargs: Any
    ) -> None:
        """Mark a notification as read.

        Args:
            notification_id: The notification ID
        """
        return await self._call(
            "apps_accounts_api_mark_notification_read",
            notification_id=notification_id,
            **kwargs,
        )

    async def mark_all_notifications_read(self, **kwargs: Any) -> None:
        """Mark all notifications as read."""
        return await self._call(
            "apps_accounts_api_mark_all_notifications_read",
            **kwargs,
        )
