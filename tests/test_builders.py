"""Tests for workflow builder helpers."""

import pytest

from spatialflow import (
    build_geofence_webhook_workflow,
    build_geofence_integration_workflow,
    TriggerType,
)


class TestBuildGeofenceWebhookWorkflow:
    """Test build_geofence_webhook_workflow function."""

    def test_basic_workflow_structure(self):
        """Test workflow builder returns expected structure."""
        result = build_geofence_webhook_workflow(
            name="Test Workflow",
            geofence_ids=["uuid-1", "uuid-2"],
            webhook_url="https://example.com/hook",
        )

        assert result.name == "Test Workflow"
        assert result.description is None
        assert len(result.nodes) == 2
        assert len(result.edges) == 1

    def test_trigger_node_structure(self):
        """Test trigger node has correct structure."""
        result = build_geofence_webhook_workflow(
            name="Test",
            geofence_ids=["uuid-1", "uuid-2"],
            webhook_url="https://example.com/hook",
        )

        trigger = next(n for n in result.nodes if n["type"] == "trigger")
        assert trigger["id"] == "trigger-1"
        assert trigger["type"] == "trigger"
        assert "position" in trigger
        assert trigger["position"]["x"] == 100
        assert trigger["position"]["y"] == 100
        assert trigger["data"]["triggerType"] == "geofence_enter"
        assert trigger["data"]["config"]["type"] == "geofence_enter"
        assert trigger["data"]["config"]["geofence_ids"] == ["uuid-1", "uuid-2"]

    def test_action_node_structure(self):
        """Test action node has correct structure."""
        result = build_geofence_webhook_workflow(
            name="Test",
            geofence_ids=["uuid-1"],
            webhook_url="https://example.com/hook",
        )

        action = next(n for n in result.nodes if n["type"] == "action")
        assert action["id"] == "action-1"
        assert action["type"] == "action"
        assert action["data"]["actionType"] == "webhook"
        assert action["data"]["config"]["url"] == "https://example.com/hook"
        assert action["data"]["config"]["method"] == "POST"
        assert action["data"]["config"]["headers"] == {"Content-Type": "application/json"}

    def test_edge_structure(self):
        """Test edge connects trigger to action."""
        result = build_geofence_webhook_workflow(
            name="Test",
            geofence_ids=["uuid-1"],
            webhook_url="https://example.com/hook",
        )

        edge = result.edges[0]
        assert edge["id"] == "edge-1"
        assert edge["source"] == "trigger-1"
        assert edge["target"] == "action-1"

    def test_geofence_exit_trigger(self):
        """Test exit trigger type."""
        result = build_geofence_webhook_workflow(
            name="Exit Alert",
            geofence_ids=["uuid-1"],
            webhook_url="https://example.com",
            trigger_type="geofence_exit",
        )

        trigger = next(n for n in result.nodes if n["type"] == "trigger")
        assert trigger["data"]["triggerType"] == "geofence_exit"
        assert trigger["data"]["config"]["type"] == "geofence_exit"
        assert "Exit" in trigger["data"]["label"]

    def test_geofence_dwell_trigger(self):
        """Test dwell trigger type."""
        result = build_geofence_webhook_workflow(
            name="Dwell Alert",
            geofence_ids=["uuid-1"],
            webhook_url="https://example.com",
            trigger_type="geofence_dwell",
        )

        trigger = next(n for n in result.nodes if n["type"] == "trigger")
        assert trigger["data"]["triggerType"] == "geofence_dwell"
        assert trigger["data"]["config"]["type"] == "geofence_dwell"

    def test_custom_description(self):
        """Test custom description is set."""
        result = build_geofence_webhook_workflow(
            name="Test",
            geofence_ids=["uuid-1"],
            webhook_url="https://example.com",
            description="My custom description",
        )

        assert result.description == "My custom description"

    def test_custom_webhook_method(self):
        """Test custom HTTP method."""
        result = build_geofence_webhook_workflow(
            name="Test",
            geofence_ids=["uuid-1"],
            webhook_url="https://example.com",
            webhook_method="PUT",
        )

        action = next(n for n in result.nodes if n["type"] == "action")
        assert action["data"]["config"]["method"] == "PUT"

    def test_custom_webhook_headers(self):
        """Test custom headers."""
        custom_headers = {
            "Authorization": "Bearer token123",
            "X-Custom": "value",
        }
        result = build_geofence_webhook_workflow(
            name="Test",
            geofence_ids=["uuid-1"],
            webhook_url="https://example.com",
            webhook_headers=custom_headers,
        )

        action = next(n for n in result.nodes if n["type"] == "action")
        assert action["data"]["config"]["headers"] == custom_headers


class TestBuildGeofenceIntegrationWorkflow:
    """Test build_geofence_integration_workflow function."""

    def test_basic_integration_workflow(self):
        """Test integration workflow structure."""
        result = build_geofence_integration_workflow(
            name="Integration Workflow",
            geofence_ids=["uuid-1"],
            integration_id="int-123",
        )

        assert result.name == "Integration Workflow"
        assert len(result.nodes) == 2
        assert len(result.edges) == 1

    def test_integration_action_node(self):
        """Test integration action node structure."""
        result = build_geofence_integration_workflow(
            name="Test",
            geofence_ids=["uuid-1"],
            integration_id="int-123",
        )

        action = next(n for n in result.nodes if n["type"] == "action")
        assert action["data"]["actionType"] == "integration"
        assert action["data"]["config"]["integration_id"] == "int-123"

    def test_integration_with_exit_trigger(self):
        """Test integration workflow with exit trigger."""
        result = build_geofence_integration_workflow(
            name="Exit Integration",
            geofence_ids=["uuid-1", "uuid-2"],
            integration_id="int-456",
            trigger_type="geofence_exit",
        )

        trigger = next(n for n in result.nodes if n["type"] == "trigger")
        assert trigger["data"]["triggerType"] == "geofence_exit"
        assert trigger["data"]["config"]["geofence_ids"] == ["uuid-1", "uuid-2"]


class TestTriggerType:
    """Test TriggerType literal."""

    def test_valid_trigger_types(self):
        """Test that valid trigger types are accepted."""
        # These should not raise type errors at runtime
        for trigger_type in ["geofence_enter", "geofence_exit", "geofence_dwell"]:
            result = build_geofence_webhook_workflow(
                name="Test",
                geofence_ids=["uuid-1"],
                webhook_url="https://example.com",
                trigger_type=trigger_type,  # type: ignore
            )
            trigger = next(n for n in result.nodes if n["type"] == "trigger")
            assert trigger["data"]["triggerType"] == trigger_type


class TestApiMethodsExist:
    """Verify generated API method names match our wrappers."""

    def test_public_location_api_methods_exist(self):
        """Verify generated API method names match our wrappers."""
        from spatialflow._generated.spatialflow_generated.api.public_location_ingest_api import (
            PublicLocationIngestApi,
        )

        assert hasattr(PublicLocationIngestApi, "apps_public_locations_api_ingest_location")
        assert hasattr(PublicLocationIngestApi, "apps_public_locations_api_ingest_location_batch")
        assert hasattr(PublicLocationIngestApi, "apps_public_locations_api_get_ingest_stats")

    def test_integrations_api_methods_exist(self):
        """Verify integration API method names."""
        from spatialflow._generated.spatialflow_generated.api.integrations_api import (
            IntegrationsApi,
        )

        assert hasattr(IntegrationsApi, "apps_integrations_api_list_integrations")
        assert hasattr(IntegrationsApi, "apps_integrations_api_create_integration")
        assert hasattr(IntegrationsApi, "apps_integrations_api_get_integration")
        assert hasattr(IntegrationsApi, "apps_integrations_api_delete_integration")
        assert hasattr(IntegrationsApi, "apps_integrations_api_test_integration")

    def test_workflows_api_toggle_exists(self):
        """Verify toggle method exists."""
        from spatialflow._generated.spatialflow_generated.api.workflows_api import (
            WorkflowsApi,
        )

        assert hasattr(WorkflowsApi, "apps_workflows_api_toggle_workflow")

    def test_workflow_in_accepts_dicts(self):
        """Verify WorkflowIn accepts List[Dict] for nodes/edges."""
        from spatialflow._generated.spatialflow_generated.models import WorkflowIn

        workflow = WorkflowIn(
            name="Test",
            nodes=[{"id": "t1", "type": "trigger", "data": {}}],
            edges=[{"id": "e1", "source": "t1", "target": "a1"}],
        )
        assert workflow.name == "Test"
        assert len(workflow.nodes) == 1
        assert len(workflow.edges) == 1
