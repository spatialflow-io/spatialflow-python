"""Mocked unit tests for SDK resource wrappers.

These tests verify that resource methods correctly call the underlying
generated API methods with the proper arguments, using mocks to avoid
needing live API credentials.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock

from spatialflow.resources import (
    AccountResource,
    WorkspacesResource,
    WorkflowsResource,
    WebhooksResource,
)


# -----------------------------------------------------------------------------
# WorkspacesResource Tests
# -----------------------------------------------------------------------------


class TestWorkspacesResource:
    """Tests for WorkspacesResource methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create a WorkspacesResource with mock API."""
        return WorkspacesResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_calls_correct_method(self, resource, mock_api):
        """Test that get() calls the correct API method."""
        result = await resource.get()

        mock_api.apps_workspaces_api_get_workspace.assert_called_once_with(
            _request_timeout=30
        )
        assert result["id"] == "ws-123"
        assert result["name"] == "Test Workspace"

    @pytest.mark.asyncio
    async def test_update_calls_correct_method(self, resource, mock_api):
        """Test that update() calls the correct API method with request."""
        request = {"name": "Updated Workspace"}
        result = await resource.update(request)

        mock_api.apps_workspaces_api_update_workspace.assert_called_once_with(
            _request_timeout=30, workspace_in=request
        )
        assert result["name"] == "Updated"

    @pytest.mark.asyncio
    async def test_get_usage_calls_correct_method(self, resource, mock_api):
        """Test that get_usage() calls the correct API method."""
        result = await resource.get_usage()

        mock_api.apps_workspaces_api_get_workspace_usage.assert_called_once_with(
            _request_timeout=30
        )
        assert result["location_events"] == 1000
        assert result["event_units"] == 1250


# -----------------------------------------------------------------------------
# WorkflowsResource Tests - New Methods
# -----------------------------------------------------------------------------


class TestWorkflowsResourceActivate:
    """Tests for WorkflowsResource activate method."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create a WorkflowsResource with mock API."""
        return WorkflowsResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_activate_calls_correct_method(self, resource, mock_api):
        """Test that activate() calls the correct API method."""
        result = await resource.activate("wf-123")

        mock_api.apps_workflows_api_activate_workflow.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["status"] == "active"
        assert result["is_active"] is True

    @pytest.mark.asyncio
    async def test_toggle_calls_correct_method(self, resource, mock_api):
        """Test that toggle() calls the correct API method."""
        result = await resource.toggle("wf-123")

        mock_api.apps_workflows_api_toggle_workflow.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["status"] == "paused"


class TestWorkflowsResourceExecution:
    """Tests for WorkflowsResource execution-related methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create a WorkflowsResource with mock API."""
        return WorkflowsResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_execute_calls_correct_method(self, resource, mock_api):
        """Test that execute() calls the correct API method."""
        request = {"context": {"device_id": "dev-1"}}
        result = await resource.execute("wf-123", request)

        mock_api.apps_workflows_api_execute_workflow.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            workflow_execution_request=request,
        )
        assert result["execution_id"] == "ex-123"

    @pytest.mark.asyncio
    async def test_execute_without_request(self, resource, mock_api):
        """Test that execute() works without optional request."""
        result = await resource.execute("wf-123")

        mock_api.apps_workflows_api_execute_workflow.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            workflow_execution_request=None,
        )
        assert result["status"] == "pending"

    @pytest.mark.asyncio
    async def test_test_calls_correct_method(self, resource, mock_api):
        """Test that test() calls the correct API method."""
        request = {"sample_data": {"lat": 37.7, "lon": -122.4}}
        result = await resource.test("wf-123", request)

        mock_api.apps_workflows_api_test_workflow.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            workflow_test_request=request,
        )
        assert result["result"] == "success"

    @pytest.mark.asyncio
    async def test_list_executions_calls_correct_method(self, resource, mock_api):
        """Test that list_executions() calls the correct API method."""
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
        """Test that get_execution() calls the correct API method."""
        result = await resource.get_execution("wf-123", "ex-456")

        mock_api.apps_workflows_api_get_workflow_execution_detail.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            execution_id="ex-456",
        )
        assert result["status"] == "completed"


class TestWorkflowsResourceMonitoring:
    """Tests for WorkflowsResource monitoring methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create a WorkflowsResource with mock API."""
        return WorkflowsResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_performance_calls_correct_method(self, resource, mock_api):
        """Test that get_performance() calls the correct API method."""
        result = await resource.get_performance("wf-123")

        mock_api.apps_workflows_api_get_workflow_performance.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["success_rate"] == 0.98

    @pytest.mark.asyncio
    async def test_get_statistics_calls_correct_method(self, resource, mock_api):
        """Test that get_statistics() calls the correct API method."""
        result = await resource.get_statistics("wf-123")

        mock_api.apps_workflows_api_get_workflow_statistics.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["total_executions"] == 1000

    @pytest.mark.asyncio
    async def test_get_retry_policy_calls_correct_method(self, resource, mock_api):
        """Test that get_retry_policy() calls the correct API method."""
        result = await resource.get_retry_policy("wf-123")

        mock_api.apps_workflows_api_get_workflow_retry_policy.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["max_retries"] == 3


class TestWorkflowsResourceAdditional:
    """Tests for additional WorkflowsResource methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create a WorkflowsResource with mock API."""
        return WorkflowsResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_update_retry_policy_calls_correct_method(self, resource, mock_api):
        """Test that update_retry_policy() calls the correct API method."""
        request = {"max_retries": 5, "backoff_seconds": 120}
        result = await resource.update_retry_policy("wf-123", request)

        mock_api.apps_workflows_api_update_workflow_retry_policy.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            workflow_retry_policy_request=request,
        )
        assert result["max_retries"] == 5

    @pytest.mark.asyncio
    async def test_list_all_executions_calls_correct_method(self, resource, mock_api):
        """Test that list_all_executions() calls the correct API method."""
        result = await resource.list_all_executions(limit=50, offset=10)

        mock_api.apps_workflows_api_list_workflow_executions.assert_called_once_with(
            _request_timeout=30,
            limit=50,
            offset=10,
        )
        assert result["count"] == 0

    @pytest.mark.asyncio
    async def test_get_bottlenecks_calls_correct_method(self, resource, mock_api):
        """Test that get_bottlenecks() calls the correct API method."""
        result = await resource.get_bottlenecks("wf-123")

        mock_api.apps_workflows_api_get_workflow_bottlenecks.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert "bottlenecks" in result

    @pytest.mark.asyncio
    async def test_get_step_performance_calls_correct_method(self, resource, mock_api):
        """Test that get_step_performance() calls the correct API method."""
        result = await resource.get_step_performance("wf-123")

        mock_api.apps_workflows_api_get_workflow_step_performance.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert "steps" in result


class TestWorkflowsResourceVersioning:
    """Tests for WorkflowsResource versioning methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create a WorkflowsResource with mock API."""
        return WorkflowsResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_list_versions_calls_correct_method(self, resource, mock_api):
        """Test that list_versions() calls the correct API method."""
        result = await resource.list_versions("wf-123")

        mock_api.apps_workflows_api_list_workflow_versions.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert result["count"] == 2

    @pytest.mark.asyncio
    async def test_restore_version_calls_correct_method(self, resource, mock_api):
        """Test that restore_version() calls the correct API method."""
        result = await resource.restore_version("wf-123", 1)

        mock_api.apps_workflows_api_restore_workflow_version.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123", version_number=1
        )
        assert result["version"] == 1

    @pytest.mark.asyncio
    async def test_duplicate_calls_correct_method(self, resource, mock_api):
        """Test that duplicate() calls the correct API method."""
        request = {"name": "Copy of Workflow"}
        result = await resource.duplicate("wf-123", request)

        mock_api.apps_workflows_api_duplicate_workflow.assert_called_once_with(
            _request_timeout=30,
            workflow_id="wf-123",
            workflow_duplicate_request=request,
        )
        assert result["name"] == "Copy of Workflow"

    @pytest.mark.asyncio
    async def test_export_workflow_calls_correct_method(self, resource, mock_api):
        """Test that export_workflow() calls the correct API method."""
        result = await resource.export_workflow("wf-123")

        mock_api.apps_workflows_api_export_workflow.assert_called_once_with(
            _request_timeout=30, workflow_id="wf-123"
        )
        assert "workflow_json" in result

    @pytest.mark.asyncio
    async def test_import_workflow_calls_correct_method(self, resource, mock_api):
        """Test that import_workflow() calls the correct API method."""
        request = {"data": {"name": "Imported", "nodes": []}}
        result = await resource.import_workflow(request)

        mock_api.apps_workflows_api_import_workflow.assert_called_once_with(
            _request_timeout=30, workflow_import_request=request
        )
        assert result["name"] == "Imported"


# -----------------------------------------------------------------------------
# WebhooksResource Tests - New Methods
# -----------------------------------------------------------------------------


class TestWebhooksResourceDeliveries:
    """Tests for WebhooksResource delivery-related methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create a WebhooksResource with mock API."""
        return WebhooksResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_list_deliveries_calls_correct_method(self, resource, mock_api):
        """Test that list_deliveries() calls the correct API method."""
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
        """Test that get_delivery() calls the correct API method."""
        result = await resource.get_delivery("wh-123", "del-456")

        mock_api.apps_webhooks_api_get_webhook_delivery_detail.assert_called_once_with(
            _request_timeout=30,
            webhook_id="wh-123",
            delivery_id="del-456",
        )
        assert result["status"] == "success"

    @pytest.mark.asyncio
    async def test_retry_delivery_calls_correct_method(self, resource, mock_api):
        """Test that retry_delivery() calls the correct API method."""
        result = await resource.retry_delivery("wh-123", "del-456")

        mock_api.apps_webhooks_api_retry_webhook_delivery.assert_called_once_with(
            _request_timeout=30,
            webhook_id="wh-123",
            delivery_id="del-456",
        )
        assert result["status"] == "pending"


class TestWebhooksResourceMonitoring:
    """Tests for WebhooksResource monitoring methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create a WebhooksResource with mock API."""
        return WebhooksResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_metrics_calls_correct_method(self, resource, mock_api):
        """Test that get_metrics() calls the correct API method."""
        result = await resource.get_metrics("wh-123")

        mock_api.apps_webhooks_api_get_webhook_metrics.assert_called_once_with(
            _request_timeout=30, webhook_id="wh-123"
        )
        assert result["success_rate"] == 0.95

    @pytest.mark.asyncio
    async def test_get_success_timeline_calls_correct_method(self, resource, mock_api):
        """Test that get_success_timeline() calls the correct API method."""
        result = await resource.get_success_timeline("wh-123")

        mock_api.apps_webhooks_api_get_webhook_success_timeline.assert_called_once_with(
            _request_timeout=30, webhook_id="wh-123"
        )
        assert "timeline" in result

    @pytest.mark.asyncio
    async def test_test_calls_correct_method(self, resource, mock_api):
        """Test that test() calls the correct API method."""
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
        """Test that test() works without optional request."""
        result = await resource.test("wh-123")

        mock_api.apps_webhooks_api_test_webhook.assert_called_once_with(
            _request_timeout=30,
            webhook_id="wh-123",
            test_webhook_request={},
        )


class TestWebhooksResourceDLQ:
    """Tests for WebhooksResource Dead Letter Queue methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
        api = MagicMock()
        api.apps_webhooks_api_list_dlq_entries = AsyncMock(
            return_value={"entries": [], "count": 0}
        )
        api.apps_webhooks_api_retry_from_dlq = AsyncMock(
            return_value={"entry_id": "dlq-123", "status": "retried"}
        )
        return api

    @pytest.fixture
    def resource(self, mock_api):
        """Create a WebhooksResource with mock API."""
        return WebhooksResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_list_dlq_entries_calls_correct_method(self, resource, mock_api):
        """Test that list_dlq_entries() calls the correct API method."""
        result = await resource.list_dlq_entries(limit=50, offset=10)

        mock_api.apps_webhooks_api_list_dlq_entries.assert_called_once_with(
            _request_timeout=30,
            limit=50,
            offset=10,
        )
        assert result["count"] == 0

    @pytest.mark.asyncio
    async def test_list_dlq_entries_with_defaults(self, resource, mock_api):
        """Test that list_dlq_entries() uses default pagination values."""
        result = await resource.list_dlq_entries()

        mock_api.apps_webhooks_api_list_dlq_entries.assert_called_once_with(
            _request_timeout=30,
            limit=100,
            offset=0,
        )

    @pytest.mark.asyncio
    async def test_retry_dlq_calls_correct_method(self, resource, mock_api):
        """Test that retry_dlq() calls the correct API method."""
        result = await resource.retry_dlq("dlq-123")

        mock_api.apps_webhooks_api_retry_from_dlq.assert_called_once_with(
            _request_timeout=30, dlq_entry_id="dlq-123"
        )
        assert result["status"] == "retried"


# -----------------------------------------------------------------------------
# AccountResource Tests
# -----------------------------------------------------------------------------


class TestAccountResourceProfile:
    """Tests for AccountResource profile methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create an AccountResource with mock API."""
        return AccountResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_profile_calls_correct_method(self, resource, mock_api):
        """Test that get_profile() calls the correct API method."""
        result = await resource.get_profile()

        mock_api.apps_accounts_api_get_user_profile.assert_called_once_with(
            _request_timeout=30
        )
        assert result["id"] == "user-123"
        assert result["email"] == "test@example.com"

    @pytest.mark.asyncio
    async def test_update_profile_calls_correct_method(self, resource, mock_api):
        """Test that update_profile() calls the correct API method."""
        request = {"name": "Updated Name"}
        result = await resource.update_profile(request)

        mock_api.apps_accounts_api_update_user_profile.assert_called_once_with(
            _request_timeout=30, update_profile_request=request
        )
        assert result["name"] == "Updated"


class TestAccountResourceApiKeys:
    """Tests for AccountResource API key methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create an AccountResource with mock API."""
        return AccountResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_list_api_keys_calls_correct_method(self, resource, mock_api):
        """Test that list_api_keys() calls the correct API method."""
        result = await resource.list_api_keys()

        mock_api.apps_accounts_api_get_api_keys.assert_called_once_with(
            _request_timeout=30
        )
        assert len(result) == 2
        assert result[0]["id"] == "key-1"

    @pytest.mark.asyncio
    async def test_get_api_key_calls_correct_method(self, resource, mock_api):
        """Test that get_api_key() calls the correct API method."""
        result = await resource.get_api_key("key-1")

        mock_api.apps_accounts_api_get_api_key.assert_called_once_with(
            _request_timeout=30, api_key_id="key-1"
        )
        assert result["id"] == "key-1"

    @pytest.mark.asyncio
    async def test_create_api_key_calls_correct_method(self, resource, mock_api):
        """Test that create_api_key() calls the correct API method."""
        request = {"name": "New Key"}
        result = await resource.create_api_key(request)

        mock_api.apps_accounts_api_create_api_key.assert_called_once_with(
            _request_timeout=30, api_key_create_request=request
        )
        assert result["id"] == "key-new"
        assert "key" in result  # Full key only returned on create

    @pytest.mark.asyncio
    async def test_update_api_key_calls_correct_method(self, resource, mock_api):
        """Test that update_api_key() calls the correct API method."""
        request = {"name": "Renamed Key"}
        result = await resource.update_api_key("key-1", request)

        mock_api.apps_accounts_api_update_api_key.assert_called_once_with(
            _request_timeout=30, api_key_id="key-1", api_key_update_request=request
        )
        assert result["name"] == "Renamed Key"

    @pytest.mark.asyncio
    async def test_delete_api_key_calls_correct_method(self, resource, mock_api):
        """Test that delete_api_key() calls the correct API method."""
        await resource.delete_api_key("key-1")

        mock_api.apps_accounts_api_delete_api_key.assert_called_once_with(
            _request_timeout=30, api_key_id="key-1"
        )

    @pytest.mark.asyncio
    async def test_rotate_api_key_calls_correct_method(self, resource, mock_api):
        """Test that rotate_api_key() calls the correct API method."""
        result = await resource.rotate_api_key("key-1")

        mock_api.apps_accounts_api_rotate_api_key.assert_called_once_with(
            _request_timeout=30, api_key_id="key-1"
        )
        assert "key" in result


class TestAccountResourceDashboardOnboarding:
    """Tests for AccountResource dashboard and onboarding methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
        api = MagicMock()
        api.apps_accounts_api_get_dashboard_metrics = AsyncMock(
            return_value={
                "geofence_count": 10,
                "workflow_count": 5,
                "recent_events": 100,
            }
        )
        api.apps_accounts_api_get_onboarding_progress = AsyncMock(
            return_value={
                "completed_steps": ["create_geofence", "create_workflow"],
                "is_complete": False,
            }
        )
        api.apps_accounts_api_update_onboarding_progress = AsyncMock(
            return_value={
                "completed_steps": ["create_geofence", "create_workflow", "test_webhook"],
                "is_complete": True,
            }
        )
        api.apps_accounts_api_dismiss_onboarding = AsyncMock(return_value=None)
        return api

    @pytest.fixture
    def resource(self, mock_api):
        """Create an AccountResource with mock API."""
        return AccountResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_dashboard_metrics_calls_correct_method(self, resource, mock_api):
        """Test that get_dashboard_metrics() calls the correct API method."""
        result = await resource.get_dashboard_metrics()

        mock_api.apps_accounts_api_get_dashboard_metrics.assert_called_once_with(
            _request_timeout=30
        )
        assert result["geofence_count"] == 10
        assert result["workflow_count"] == 5

    @pytest.mark.asyncio
    async def test_get_onboarding_progress_calls_correct_method(self, resource, mock_api):
        """Test that get_onboarding_progress() calls the correct API method."""
        result = await resource.get_onboarding_progress()

        mock_api.apps_accounts_api_get_onboarding_progress.assert_called_once_with(
            _request_timeout=30
        )
        assert "completed_steps" in result

    @pytest.mark.asyncio
    async def test_update_onboarding_progress_calls_correct_method(
        self, resource, mock_api
    ):
        """Test that update_onboarding_progress() calls the correct API method."""
        request = {"completed_steps": ["step1", "step2"]}
        result = await resource.update_onboarding_progress(request)

        mock_api.apps_accounts_api_update_onboarding_progress.assert_called_once_with(
            _request_timeout=30, update_onboarding_progress_request=request
        )
        assert result["is_complete"] is True

    @pytest.mark.asyncio
    async def test_dismiss_onboarding_calls_correct_method(self, resource, mock_api):
        """Test that dismiss_onboarding() calls the correct API method."""
        await resource.dismiss_onboarding()

        mock_api.apps_accounts_api_dismiss_onboarding.assert_called_once_with(
            _request_timeout=30
        )


class TestAccountResourceNotifications:
    """Tests for AccountResource notification methods."""

    @pytest.fixture
    def mock_api(self):
        """Create a mock API with AsyncMock methods."""
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
        """Create an AccountResource with mock API."""
        return AccountResource(mock_api, timeout=30)

    @pytest.mark.asyncio
    async def test_get_notifications_calls_correct_method(self, resource, mock_api):
        """Test that get_notifications() calls the correct API method."""
        result = await resource.get_notifications()

        mock_api.apps_accounts_api_get_notifications.assert_called_once_with(
            _request_timeout=30
        )
        assert len(result) == 2
        assert result[0]["id"] == "notif-1"

    @pytest.mark.asyncio
    async def test_mark_notification_read_calls_correct_method(self, resource, mock_api):
        """Test that mark_notification_read() calls the correct API method."""
        await resource.mark_notification_read("notif-1")

        mock_api.apps_accounts_api_mark_notification_read.assert_called_once_with(
            _request_timeout=30, notification_id="notif-1"
        )

    @pytest.mark.asyncio
    async def test_mark_all_notifications_read_calls_correct_method(
        self, resource, mock_api
    ):
        """Test that mark_all_notifications_read() calls the correct API method."""
        await resource.mark_all_notifications_read()

        mock_api.apps_accounts_api_mark_all_notifications_read.assert_called_once_with(
            _request_timeout=30
        )
