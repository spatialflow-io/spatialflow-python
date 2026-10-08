"""Mocked unit tests for SDK resource wrappers.

These tests verify that resource methods correctly call the underlying
generated API methods with the proper arguments, using mocks to avoid
needing live API credentials.
"""

from datetime import datetime, timezone

import pytest
from unittest.mock import AsyncMock, MagicMock

from spatialflow.exceptions import NotFoundError, PermissionError, ValidationError
from spatialflow.resources import (
    AccountResource,
    DevicesResource,
    GeofencesResource,
    StorageResource,
    WorkspacesResource,
    WorkflowsResource,
    WebhooksResource,
)


class TestStorageResource:
    async def test_complete_upload_calls_generated_operation(self):
        mock_api = MagicMock()
        mock_api.apps_storage_api_complete_presigned_upload = AsyncMock(
            return_value={"file_id": "file-123", "status": "complete"}
        )
        resource = StorageResource(mock_api, timeout=30)

        result = await resource.complete_upload("file-123")

        mock_api.apps_storage_api_complete_presigned_upload.assert_awaited_once_with(
            _request_timeout=30,
            file_id="file-123",
        )
        assert result["status"] == "complete"

    async def test_delete_file_calls_generated_operation(self):
        mock_api = MagicMock()
        mock_api.apps_storage_api_delete_file = AsyncMock(return_value=None)
        resource = StorageResource(mock_api, timeout=30)

        await resource.delete_file("file-123")

        mock_api.apps_storage_api_delete_file.assert_awaited_once_with(
            _request_timeout=30,
            file_id="file-123",
        )


class TestWorkspacesResource:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_workspaces_api_get_workspace = AsyncMock(
            return_value={"id": "ws-123", "name": "Test Workspace", "slug": "test"}
        )
        api.apps_workspaces_api_update_workspace = AsyncMock(
            return_value={"id": "ws-123", "name": "Updated", "slug": "test"}
        )
        api.apps_workspaces_api_get_workspace_usage = AsyncMock(
            return_value={
                "location_events": 1000,
                "action_deliveries": 500,
                "event_units": 1250,
                "tier": "free",
                "tier_limit": 5000,
            }
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return WorkspacesResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_calls_correct_method(self, resource, mock_api):
        result = await resource.get()

        mock_api.apps_workspaces_api_get_workspace.assert_called_once_with(_request_timeout=30)
        assert result["id"] == "ws-123"
        assert result["name"] == "Test Workspace"

    @pytest.mark.asyncio
    async def test_update_calls_correct_method(self, resource, mock_api):
        request = {"name": "Updated Workspace"}
        result = await resource.update(request)

        mock_api.apps_workspaces_api_update_workspace.assert_called_once_with(
            _request_timeout=30, workspace_in=request
        )
        assert result["name"] == "Updated"

    @pytest.mark.asyncio
    async def test_get_usage_calls_correct_method(self, resource, mock_api):
        result = await resource.get_usage()

        mock_api.apps_workspaces_api_get_workspace_usage.assert_called_once_with(
            _request_timeout=30
        )
        assert result["location_events"] == 1000
        assert result["event_units"] == 1250


class TestWorkflowsResourceActivate:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_workflows_api_activate_workflow = AsyncMock(
            return_value={"id": "wf-123", "status": "active", "is_active": True}
        )
        api.apps_workflows_api_toggle_workflow = AsyncMock(
            return_value={"id": "wf-123", "status": "paused", "is_active": False}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return WorkflowsResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_activate_calls_correct_method(self, resource, mock_api):
        result = await resource.activate("wf-123")

        mock_api.apps_workflows_api_activate_workflow.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["status"] == "active"
        assert result["is_active"] is True

    @pytest.mark.asyncio
    async def test_toggle_calls_correct_method(self, resource, mock_api):
        result = await resource.toggle("wf-123")

        mock_api.apps_workflows_api_toggle_workflow.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["status"] == "paused"


class TestWorkflowsResourceExecution:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_workflows_api_execute_workflow = AsyncMock(
            return_value={"execution_id": "ex-123", "status": "pending"}
        )
        api.apps_workflows_api_test_workflow = AsyncMock(
            return_value={"test_id": "test-123", "result": "success"}
        )
        api.apps_workflows_api_get_workflow_executions = AsyncMock(
            return_value={"executions": [], "count": 0}
        )
        api.apps_workflows_api_get_workflow_execution_detail = AsyncMock(
            return_value={"execution_id": "ex-123", "status": "completed"}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return WorkflowsResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_execute_calls_correct_method(self, resource, mock_api):
        request = {"context": {"device_id": "dev-1"}}
        result = await resource.execute("wf-123", request)

        mock_api.apps_workflows_api_execute_workflow.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            test_data=request,
        )
        assert result["execution_id"] == "ex-123"

    @pytest.mark.asyncio
    async def test_execute_without_request(self, resource, mock_api):
        result = await resource.execute("wf-123")

        mock_api.apps_workflows_api_execute_workflow.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            test_data=None,
        )
        assert result["status"] == "pending"

    @pytest.mark.asyncio
    async def test_test_calls_correct_method(self, resource, mock_api):
        request = {"sample_data": {"lat": 37.7, "lon": -122.4}}
        result = await resource.test("wf-123", request)

        mock_api.apps_workflows_api_test_workflow.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            test_workflow_in=request,
        )
        assert result["result"] == "success"

    @pytest.mark.asyncio
    async def test_list_executions_calls_correct_method(self, resource, mock_api):
        result = await resource.list_executions("wf-123", limit=50, offset=10)

        mock_api.apps_workflows_api_get_workflow_executions.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            limit=50,
            offset=10,
        )
        assert result["count"] == 0

    @pytest.mark.asyncio
    async def test_get_execution_calls_correct_method(self, resource, mock_api):
        result = await resource.get_execution("wf-123", "ex-456")

        mock_api.apps_workflows_api_get_workflow_execution_detail.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            execution_id="ex-456",
        )
        assert result["status"] == "completed"


class TestWorkflowsResourceMonitoring:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_workflows_api_get_workflow_performance = AsyncMock(
            return_value={"avg_duration_ms": 150, "success_rate": 0.98}
        )
        api.apps_workflows_api_get_workflow_statistics = AsyncMock(
            return_value={"total_executions": 1000, "failed": 20}
        )
        api.apps_workflows_api_get_workflow_retry_policy = AsyncMock(
            return_value={"max_retries": 3, "backoff_seconds": 60}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return WorkflowsResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_performance_calls_correct_method(self, resource, mock_api):
        result = await resource.get_performance("wf-123")

        mock_api.apps_workflows_api_get_workflow_performance.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["success_rate"] == 0.98

    @pytest.mark.asyncio
    async def test_get_statistics_calls_correct_method(self, resource, mock_api):
        result = await resource.get_statistics("wf-123")

        mock_api.apps_workflows_api_get_workflow_statistics.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["total_executions"] == 1000

    @pytest.mark.asyncio
    async def test_get_retry_policy_calls_correct_method(self, resource, mock_api):
        result = await resource.get_retry_policy("wf-123")

        mock_api.apps_workflows_api_get_workflow_retry_policy.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["max_retries"] == 3


class TestWorkflowsResourceAdditional:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_workflows_api_update_workflow_retry_policy = AsyncMock(
            return_value={"max_retries": 5, "backoff_seconds": 120}
        )
        api.apps_workflows_api_list_workflow_executions = AsyncMock(
            return_value={"executions": [], "count": 0}
        )
        api.apps_workflows_api_get_workflow_bottlenecks = AsyncMock(
            return_value={"bottlenecks": [{"step": "action1", "avg_ms": 500}]}
        )
        api.apps_workflows_api_get_workflow_step_performance = AsyncMock(
            return_value={"steps": [{"id": "step1", "avg_duration_ms": 100}]}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return WorkflowsResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_update_retry_policy_calls_correct_method(self, resource, mock_api):
        request = {"max_retries": 5, "backoff_seconds": 120}
        result = await resource.update_retry_policy("wf-123", request)

        mock_api.apps_workflows_api_update_workflow_retry_policy.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            workflow_retry_policy_update_schema=request,
        )
        assert result["max_retries"] == 5

    @pytest.mark.asyncio
    async def test_list_all_executions_calls_correct_method(self, resource, mock_api):
        result = await resource.list_all_executions(limit=50, offset=10)

        mock_api.apps_workflows_api_list_workflow_executions.assert_called_once_with(
            _request_timeout=30,
            limit=50,
            offset=10,
        )
        assert result["count"] == 0

    @pytest.mark.asyncio
    async def test_get_bottlenecks_calls_correct_method(self, resource, mock_api):
        result = await resource.get_bottlenecks("wf-123")

        mock_api.apps_workflows_api_get_workflow_bottlenecks.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert "bottlenecks" in result

    @pytest.mark.asyncio
    async def test_get_step_performance_calls_correct_method(self, resource, mock_api):
        result = await resource.get_step_performance("wf-123")

        mock_api.apps_workflows_api_get_workflow_step_performance.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert "steps" in result


class TestWorkflowsResourceVersioning:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_workflows_api_list_workflow_versions = AsyncMock(
            return_value={"versions": [{"version": 1}, {"version": 2}], "count": 2}
        )
        api.apps_workflows_api_restore_workflow_version = AsyncMock(
            return_value={"id": "wf-123", "version": 1}
        )
        api.apps_workflows_api_duplicate_workflow = AsyncMock(
            return_value={"id": "wf-456", "name": "Copy of Workflow"}
        )
        api.apps_workflows_api_export_workflow = AsyncMock(
            return_value={"workflow_json": {"name": "Test", "nodes": []}}
        )
        api.apps_workflows_api_import_workflow = AsyncMock(
            return_value={"id": "wf-789", "name": "Imported"}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return WorkflowsResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_list_versions_calls_correct_method(self, resource, mock_api):
        result = await resource.list_versions("wf-123")

        mock_api.apps_workflows_api_list_workflow_versions.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["count"] == 2

    @pytest.mark.asyncio
    async def test_restore_version_calls_correct_method(self, resource, mock_api):
        result = await resource.restore_version("wf-123", 1)

        mock_api.apps_workflows_api_restore_workflow_version.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123", version_number=1
        )
        assert result["version"] == 1

    @pytest.mark.asyncio
    async def test_duplicate_calls_correct_method(self, resource, mock_api):
        result = await resource.duplicate("wf-123", "Copy of Workflow")

        mock_api.apps_workflows_api_duplicate_workflow.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            name="Copy of Workflow",
        )
        assert result["name"] == "Copy of Workflow"

    @pytest.mark.asyncio
    async def test_export_workflow_calls_correct_method(self, resource, mock_api):
        result = await resource.export_workflow("wf-123")

        mock_api.apps_workflows_api_export_workflow.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert "workflow_json" in result

    @pytest.mark.asyncio
    async def test_import_workflow_calls_correct_method(self, resource, mock_api):
        request = {"data": {"name": "Imported", "nodes": []}}
        result = await resource.import_workflow(request)

        mock_api.apps_workflows_api_import_workflow.assert_called_once_with(
            _request_timeout=30, workflow_import_schema=request
        )
        assert result["name"] == "Imported"


class TestWebhooksResourceDeliveries:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_webhooks_api_get_webhook_deliveries = AsyncMock(
            return_value={"deliveries": [], "count": 0}
        )
        api.apps_webhooks_api_get_webhook_delivery_detail = AsyncMock(
            return_value={"delivery_id": "del-123", "status": "success"}
        )
        api.apps_webhooks_api_retry_webhook_delivery = AsyncMock(
            return_value={"delivery_id": "del-123", "status": "pending"}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return WebhooksResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_list_deliveries_calls_correct_method(self, resource, mock_api):
        result = await resource.list_deliveries("wh-123", limit=50, offset=10)

        mock_api.apps_webhooks_api_get_webhook_deliveries.assert_called_once_with(
            _request_timeout=30,
            webhook_id="wh-123",
            limit=50,
            offset=10,
        )
        assert result["count"] == 0

    @pytest.mark.asyncio
    async def test_get_delivery_calls_correct_method(self, resource, mock_api):
        result = await resource.get_delivery("wh-123", "del-456")

        mock_api.apps_webhooks_api_get_webhook_delivery_detail.assert_called_once_with(
            _request_timeout=30,
            webhook_id="wh-123",
            delivery_id="del-456",
        )
        assert result["status"] == "success"

    @pytest.mark.asyncio
    async def test_retry_delivery_calls_correct_method(self, resource, mock_api):
        result = await resource.retry_delivery("wh-123", "del-456")

        mock_api.apps_webhooks_api_retry_webhook_delivery.assert_called_once_with(
            _request_timeout=30,
            webhook_id="wh-123",
            delivery_id="del-456",
        )
        assert result["status"] == "pending"


class TestWebhooksResourceMonitoring:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_webhooks_api_get_webhook_metrics = AsyncMock(
            return_value={"success_rate": 0.95, "avg_response_ms": 200}
        )
        api.apps_webhooks_api_get_webhook_success_timeline = AsyncMock(
            return_value={"timeline": [{"date": "2024-01-01", "success": 100}]}
        )
        api.apps_webhooks_api_test_webhook = AsyncMock(
            return_value={"test_id": "test-123", "response_code": 200}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return WebhooksResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_metrics_calls_correct_method(self, resource, mock_api):
        result = await resource.get_metrics()

        mock_api.apps_webhooks_api_get_webhook_metrics.assert_called_once_with(_request_timeout=30)
        assert result["success_rate"] == 0.95

    @pytest.mark.asyncio
    async def test_get_success_timeline_calls_correct_method(self, resource, mock_api):
        result = await resource.get_success_timeline()

        mock_api.apps_webhooks_api_get_webhook_success_timeline.assert_called_once_with(
            _request_timeout=30
        )
        assert "timeline" in result

    @pytest.mark.asyncio
    async def test_test_calls_correct_method(self, resource, mock_api):
        request = {"payload": {"test": True}}
        result = await resource.test("wh-123", request)

        mock_api.apps_webhooks_api_test_webhook.assert_called_once_with(
            _request_timeout=30,
            webhook_id="wh-123",
            test_webhook_request=request,
        )
        assert result["response_code"] == 200

    @pytest.mark.asyncio
    async def test_test_without_request(self, resource, mock_api):
        result = await resource.test("wh-123")

        mock_api.apps_webhooks_api_test_webhook.assert_called_once_with(
            _request_timeout=30,
            webhook_id="wh-123",
            test_webhook_request={},
        )


class TestWebhooksResourceDLQ:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_webhooks_api_list_dlq_entries = AsyncMock(return_value={"entries": [], "count": 0})
        api.apps_webhooks_api_retry_from_dlq = AsyncMock(
            return_value={"entry_id": "dlq-123", "status": "retried"}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return WebhooksResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_list_dlq_entries_calls_correct_method(self, resource, mock_api):
        result = await resource.list_dlq_entries(limit=50, offset=10)

        mock_api.apps_webhooks_api_list_dlq_entries.assert_called_once_with(
            _request_timeout=30,
            limit=50,
            offset=10,
        )
        assert result["count"] == 0

    @pytest.mark.asyncio
    async def test_list_dlq_entries_with_defaults(self, resource, mock_api):
        result = await resource.list_dlq_entries()

        mock_api.apps_webhooks_api_list_dlq_entries.assert_called_once_with(
            _request_timeout=30,
            limit=100,
            offset=0,
        )

    @pytest.mark.asyncio
    async def test_retry_dlq_calls_correct_method(self, resource, mock_api):
        result = await resource.retry_dlq("dlq-123")

        mock_api.apps_webhooks_api_retry_from_dlq.assert_called_once_with(
            _request_timeout=30, dlq_id="dlq-123"
        )
        assert result["status"] == "retried"


class TestAccountResourceProfile:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_accounts_api_get_user_profile = AsyncMock(
            return_value={"id": "user-123", "email": "test@example.com", "name": "Test"}
        )
        api.apps_accounts_api_update_user_profile = AsyncMock(
            return_value={"id": "user-123", "email": "test@example.com", "name": "Updated"}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return AccountResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_profile_calls_correct_method(self, resource, mock_api):
        result = await resource.get_profile()

        mock_api.apps_accounts_api_get_user_profile.assert_called_once_with(_request_timeout=30)
        assert result["id"] == "user-123"
        assert result["email"] == "test@example.com"

    @pytest.mark.asyncio
    async def test_update_profile_calls_correct_method(self, resource, mock_api):
        request = {"name": "Updated Name"}
        result = await resource.update_profile(request)

        mock_api.apps_accounts_api_update_user_profile.assert_called_once_with(
            _request_timeout=30, update_profile_request=request
        )
        assert result["name"] == "Updated"


class TestAccountResourceApiKeys:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_accounts_api_get_api_keys = AsyncMock(
            return_value=[{"id": "key-1", "name": "Key 1"}, {"id": "key-2", "name": "Key 2"}]
        )
        api.apps_accounts_api_get_api_key = AsyncMock(
            return_value={"id": "key-1", "name": "Key 1", "prefix": "sf_xxx"}
        )
        api.apps_accounts_api_create_api_key = AsyncMock(
            return_value={"id": "key-new", "key": "sf_newkey123", "name": "New Key"}
        )
        api.apps_accounts_api_update_api_key = AsyncMock(
            return_value={"id": "key-1", "name": "Renamed Key"}
        )
        api.apps_accounts_api_delete_api_key = AsyncMock(return_value=None)
        api.apps_accounts_api_rotate_api_key = AsyncMock(
            return_value={"id": "key-1", "key": "sf_rotated456"}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return AccountResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_list_api_keys_calls_correct_method(self, resource, mock_api):
        result = await resource.list_api_keys()

        mock_api.apps_accounts_api_get_api_keys.assert_called_once_with(_request_timeout=30)
        assert len(result) == 2
        assert result[0]["id"] == "key-1"

    @pytest.mark.asyncio
    async def test_get_api_key_calls_correct_method(self, resource, mock_api):
        result = await resource.get_api_key("key-1")

        mock_api.apps_accounts_api_get_api_key.assert_called_once_with(
            _request_timeout=30, api_key_id="key-1"
        )
        assert result["id"] == "key-1"

    @pytest.mark.asyncio
    async def test_create_api_key_calls_correct_method(self, resource, mock_api):
        request = {"name": "New Key"}
        result = await resource.create_api_key(request)

        mock_api.apps_accounts_api_create_api_key.assert_called_once_with(
            _request_timeout=30, api_key_create_request=request
        )
        assert result["id"] == "key-new"
        assert "key" in result  # Full key only returned on create

    @pytest.mark.asyncio
    async def test_update_api_key_calls_correct_method(self, resource, mock_api):
        request = {"name": "Renamed Key"}
        result = await resource.update_api_key("key-1", request)

        mock_api.apps_accounts_api_update_api_key.assert_called_once_with(
            _request_timeout=30, api_key_id="key-1", api_key_update_request=request
        )
        assert result["name"] == "Renamed Key"

    @pytest.mark.asyncio
    async def test_delete_api_key_calls_correct_method(self, resource, mock_api):
        await resource.delete_api_key("key-1")

        mock_api.apps_accounts_api_delete_api_key.assert_called_once_with(
            _request_timeout=30, api_key_id="key-1"
        )

    @pytest.mark.asyncio
    async def test_rotate_api_key_calls_correct_method(self, resource, mock_api):
        result = await resource.rotate_api_key("key-1")

        mock_api.apps_accounts_api_rotate_api_key.assert_called_once_with(
            _request_timeout=30, api_key_id="key-1"
        )
        assert "key" in result


class TestAccountResourceDashboard:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_accounts_api_get_dashboard_metrics = AsyncMock(
            return_value={
                "geofence_count": 10,
                "workflow_count": 5,
                "recent_events": 100,
            }
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return AccountResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_dashboard_metrics_calls_correct_method(self, resource, mock_api):
        result = await resource.get_dashboard_metrics()

        mock_api.apps_accounts_api_get_dashboard_metrics.assert_called_once_with(
            _request_timeout=30
        )
        assert result["geofence_count"] == 10
        assert result["workflow_count"] == 5

    @pytest.mark.parametrize(
        "method", ["get_onboarding_progress", "update_onboarding_progress", "dismiss_onboarding"]
    )
    def test_removed_onboarding_endpoints_are_not_exposed(self, method):
        assert not hasattr(AccountResource, method)


class TestAccountResourceNotifications:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_accounts_api_get_notifications = AsyncMock(
            return_value=[
                {"id": "notif-1", "message": "Welcome!", "read": False},
                {"id": "notif-2", "message": "Workflow triggered", "read": True},
            ]
        )
        api.apps_accounts_api_mark_notification_read = AsyncMock(return_value=None)
        api.apps_accounts_api_mark_all_notifications_read = AsyncMock(return_value=None)
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return AccountResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_notifications_calls_correct_method(self, resource, mock_api):
        result = await resource.get_notifications()

        mock_api.apps_accounts_api_get_notifications.assert_called_once_with(_request_timeout=30)
        assert len(result) == 2
        assert result[0]["id"] == "notif-1"

    @pytest.mark.asyncio
    async def test_mark_notification_read_calls_correct_method(self, resource, mock_api):
        await resource.mark_notification_read("notif-1")

        mock_api.apps_accounts_api_mark_notification_read.assert_called_once_with(
            _request_timeout=30, notification_id="notif-1"
        )

    @pytest.mark.asyncio
    async def test_mark_all_notifications_read_calls_correct_method(self, resource, mock_api):
        await resource.mark_all_notifications_read()

        mock_api.apps_accounts_api_mark_all_notifications_read.assert_called_once_with(
            _request_timeout=30
        )


def _api_error(exc_class, status):
    return exc_class(status=status, reason="denied")


class TestDevicesResourceShifts:
    @pytest.mark.parametrize("action", ["start", "pause", "resume", "end"])
    async def test_shift_action_calls_generated_operation(self, action):
        mock_api = MagicMock()
        operation = AsyncMock(return_value={"status": "ok"})
        setattr(mock_api, f"apps_devices_api_{action}_shift", operation)
        resource = DevicesResource(mock_api, timeout=30)

        result = await getattr(resource, f"{action}_shift")("dev-1")

        operation.assert_awaited_once_with(_request_timeout=30, device_id="dev-1")
        assert result == {"status": "ok"}

    @pytest.mark.parametrize(
        "exc_class_name, status, expected",
        [
            ("BadRequestException", 400, ValidationError),
            ("ForbiddenException", 403, PermissionError),
            ("NotFoundException", 404, NotFoundError),
        ],
    )
    async def test_shift_errors_are_translated(self, exc_class_name, status, expected):
        from spatialflow._generated.spatialflow_generated import exceptions

        mock_api = MagicMock()
        mock_api.apps_devices_api_start_shift = AsyncMock(
            side_effect=_api_error(getattr(exceptions, exc_class_name), status)
        )
        resource = DevicesResource(mock_api, timeout=30)

        with pytest.raises(expected):
            await resource.start_shift("dev-1")


class TestDevicesResourceSessions:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_devices_api_get_device_sessions = AsyncMock(
            return_value={"sessions": [], "total_count": 0}
        )
        api.apps_devices_api_get_session_detail = AsyncMock(return_value={"id": "s-1"})
        api.apps_devices_api_get_session_locations = AsyncMock(
            return_value={"locations": [], "total_count": 0}
        )
        api.apps_devices_api_list_session_notes = AsyncMock(return_value=[])
        api.apps_devices_api_create_manager_session_note = AsyncMock(return_value={"id": "n-1"})
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return DevicesResource(mock_api, timeout=30)

    async def test_list_sessions_sends_defaults(self, resource, mock_api):
        await resource.list_sessions("dev-1")

        mock_api.apps_devices_api_get_device_sessions.assert_awaited_once_with(
            _request_timeout=30,
            device_id="dev-1",
            limit=20,
            offset=0,
            include_open=False,
        )

    async def test_list_sessions_passes_pagination_and_filters(self, resource, mock_api):
        after = datetime(2026, 1, 1, tzinfo=timezone.utc)
        before = datetime(2026, 2, 1, tzinfo=timezone.utc)

        await resource.list_sessions(
            "dev-1",
            limit=5,
            offset=10,
            started_after=after,
            started_before=before,
            include_open=True,
        )

        mock_api.apps_devices_api_get_device_sessions.assert_awaited_once_with(
            _request_timeout=30,
            device_id="dev-1",
            limit=5,
            offset=10,
            include_open=True,
            started_after=after,
            started_before=before,
        )

    async def test_get_session(self, resource, mock_api):
        result = await resource.get_session("dev-1", "s-1")

        mock_api.apps_devices_api_get_session_detail.assert_awaited_once_with(
            _request_timeout=30, device_id="dev-1", session_id="s-1"
        )
        assert result["id"] == "s-1"

    async def test_get_session_locations_passes_simplification_and_paging(
        self, resource, mock_api
    ):
        snapshot = datetime(2026, 1, 1, tzinfo=timezone.utc)

        await resource.get_session_locations(
            "dev-1", "s-1", limit=100, offset=200, snapshot_at=snapshot, max_points=500
        )

        mock_api.apps_devices_api_get_session_locations.assert_awaited_once_with(
            _request_timeout=30,
            device_id="dev-1",
            session_id="s-1",
            limit=100,
            offset=200,
            snapshot_at=snapshot,
            max_points=500,
        )

    async def test_get_session_locations_omits_unset_filters(self, resource, mock_api):
        await resource.get_session_locations("dev-1", "s-1")

        mock_api.apps_devices_api_get_session_locations.assert_awaited_once_with(
            _request_timeout=30,
            device_id="dev-1",
            session_id="s-1",
            limit=1000,
            offset=0,
        )

    async def test_notes_use_device_uuid_and_session_id(self, resource, mock_api):
        request = {"body": "Gate was locked"}

        await resource.list_session_notes("dev-1", "s-1")
        await resource.add_session_note("dev-1", "s-1", request)

        mock_api.apps_devices_api_list_session_notes.assert_awaited_once_with(
            _request_timeout=30, device_uuid="dev-1", session_id="s-1"
        )
        mock_api.apps_devices_api_create_manager_session_note.assert_awaited_once_with(
            _request_timeout=30, device_uuid="dev-1", session_id="s-1", session_note_in=request
        )

    @pytest.mark.parametrize(
        "method, args",
        [
            ("list_sessions", ("dev-1",)),
            ("get_session", ("dev-1", "s-1")),
            ("get_session_locations", ("dev-1", "s-1")),
            ("list_session_notes", ("dev-1", "s-1")),
            ("add_session_note", ("dev-1", "s-1", {"body": "x"})),
        ],
    )
    async def test_missing_session_maps_to_not_found(self, resource, mock_api, method, args):
        from spatialflow._generated.spatialflow_generated.exceptions import NotFoundException

        for name in dir(mock_api):
            if name.startswith("apps_devices_api_"):
                getattr(mock_api, name).side_effect = _api_error(NotFoundException, 404)

        with pytest.raises(NotFoundError):
            await getattr(resource, method)(*args)


class TestGeofencesResourceGroups:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        api.apps_geofences_api_list_geofence_groups = AsyncMock(return_value={"groups": []})
        api.apps_geofences_api_list_group_geofences = AsyncMock(return_value={"geofences": []})
        api.apps_geofences_api_test_group_point = AsyncMock(return_value={"matches": []})
        api.apps_geofences_api_update_geofence = AsyncMock(return_value={"id": "g-1"})
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return GeofencesResource(mock_api, timeout=30)

    async def test_list_groups(self, resource, mock_api):
        await resource.list_groups()

        mock_api.apps_geofences_api_list_geofence_groups.assert_awaited_once_with(
            _request_timeout=30
        )

    async def test_list_group_geofences(self, resource, mock_api):
        await resource.list_group_geofences("grp-1")

        mock_api.apps_geofences_api_list_group_geofences.assert_awaited_once_with(
            _request_timeout=30, group_id="grp-1"
        )

    async def test_test_group_point(self, resource, mock_api):
        request = {"lat": 37.7, "lng": -122.4}

        await resource.test_group_point("grp-1", request)

        mock_api.apps_geofences_api_test_group_point.assert_awaited_once_with(
            _request_timeout=30, group_id="grp-1", test_point_request=request
        )

    async def test_assign_to_group_updates_group_name_through_update(self, resource, mock_api):
        await resource.assign_to_group("g-1", "delivery-zones")

        mock_api.apps_geofences_api_update_geofence.assert_awaited_once()
        kwargs = mock_api.apps_geofences_api_update_geofence.await_args.kwargs
        assert kwargs["geofence_id"] == "g-1"
        assert kwargs["update_geofence_request"].group_name == "delivery-zones"
        assert kwargs["update_geofence_request"].model_fields_set == {"group_name"}

    async def test_unknown_group_maps_to_not_found(self, resource, mock_api):
        from spatialflow._generated.spatialflow_generated.exceptions import NotFoundException

        mock_api.apps_geofences_api_list_group_geofences.side_effect = _api_error(
            NotFoundException, 404
        )

        with pytest.raises(NotFoundError):
            await resource.list_group_geofences("missing")

    async def test_invalid_point_maps_to_validation_error(self, resource, mock_api):
        from spatialflow._generated.spatialflow_generated.exceptions import BadRequestException

        mock_api.apps_geofences_api_test_group_point.side_effect = _api_error(
            BadRequestException, 400
        )

        with pytest.raises(ValidationError):
            await resource.test_group_point("grp-1", {})


class TestWorkspacesResourceMembers:
    @pytest.fixture
    def mock_api(self):
        api = MagicMock()
        for name in (
            "list_workspace_members",
            "update_member_role",
            "remove_member",
            "create_invitation",
            "list_invitations",
            "resend_invitation",
            "resend_missing_invitations",
            "extend_invitation",
            "cancel_invitation",
        ):
            setattr(api, f"apps_workspaces_api_{name}", AsyncMock(return_value={}))
        return api

    @pytest.fixture
    def resource(self, mock_api):
        return WorkspacesResource(mock_api, timeout=30)

    async def test_list_members(self, resource, mock_api):
        await resource.list_members()

        mock_api.apps_workspaces_api_list_workspace_members.assert_awaited_once_with(
            _request_timeout=30
        )

    async def test_update_member_role(self, resource, mock_api):
        request = {"role": "manager"}

        await resource.update_member_role("user-1", request)

        mock_api.apps_workspaces_api_update_member_role.assert_awaited_once_with(
            _request_timeout=30, user_id="user-1", update_member_role_in=request
        )

    async def test_remove_member(self, resource, mock_api):
        await resource.remove_member("user-1")

        mock_api.apps_workspaces_api_remove_member.assert_awaited_once_with(
            _request_timeout=30, user_id="user-1"
        )

    async def test_list_invitations_defaults_and_cursor(self, resource, mock_api):
        await resource.list_invitations()
        await resource.list_invitations(limit=10, offset=20, before="cursor-1")

        calls = mock_api.apps_workspaces_api_list_invitations.await_args_list
        assert calls[0].kwargs == {"_request_timeout": 30, "limit": 100, "offset": 0}
        assert calls[1].kwargs == {
            "_request_timeout": 30,
            "limit": 10,
            "offset": 20,
            "before": "cursor-1",
        }

    async def test_invitation_lifecycle_calls(self, resource, mock_api):
        create = {"email": "a@example.com", "role": "field_worker"}
        extend = {"expires_at": datetime(2030, 1, 1, tzinfo=timezone.utc)}
        batch = {"invitation_ids": ["inv-1"]}

        await resource.create_invitation(create)
        await resource.resend_invitation("inv-1")
        await resource.resend_missing_invitations(batch)
        await resource.extend_invitation("inv-1", extend)
        await resource.cancel_invitation("inv-1")

        api = mock_api
        api.apps_workspaces_api_create_invitation.assert_awaited_once_with(
            _request_timeout=30, create_invitation_in=create
        )
        api.apps_workspaces_api_resend_invitation.assert_awaited_once_with(
            _request_timeout=30, invite_id="inv-1"
        )
        api.apps_workspaces_api_resend_missing_invitations.assert_awaited_once_with(
            _request_timeout=30, batch_resend_in=batch
        )
        api.apps_workspaces_api_extend_invitation.assert_awaited_once_with(
            _request_timeout=30, invite_id="inv-1", extend_invitation_in=extend
        )
        api.apps_workspaces_api_cancel_invitation.assert_awaited_once_with(
            _request_timeout=30, invite_id="inv-1"
        )

    async def test_non_admin_is_denied(self, resource, mock_api):
        from spatialflow._generated.spatialflow_generated.exceptions import ForbiddenException

        mock_api.apps_workspaces_api_remove_member.side_effect = _api_error(
            ForbiddenException, 403
        )
        mock_api.apps_workspaces_api_create_invitation.side_effect = _api_error(
            ForbiddenException, 403
        )

        with pytest.raises(PermissionError):
            await resource.remove_member("user-1")
        with pytest.raises(PermissionError):
            await resource.create_invitation({"email": "a@example.com"})

    async def test_unknown_member_maps_to_not_found(self, resource, mock_api):
        from spatialflow._generated.spatialflow_generated.exceptions import NotFoundException

        mock_api.apps_workspaces_api_update_member_role.side_effect = _api_error(
            NotFoundException, 404
        )

        with pytest.raises(NotFoundError):
            await resource.update_member_role("missing", {"role": "manager"})

    async def test_invalid_invitation_maps_to_validation_error(self, resource, mock_api):
        from spatialflow._generated.spatialflow_generated.exceptions import BadRequestException

        mock_api.apps_workspaces_api_create_invitation.side_effect = _api_error(
            BadRequestException, 400
        )

        with pytest.raises(ValidationError):
            await resource.create_invitation({"email": "not-an-email"})
