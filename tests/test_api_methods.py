"""Smoke tests to verify generated API method names exist.

These tests catch future generator naming drift by verifying that
the method names used in our resource wrappers actually exist in
the generated API classes.
"""


def test_geofences_api_methods_exist():
    from spatialflow._generated.spatialflow_generated.api.geofences_api import (
        GeofencesApi,
    )

    assert hasattr(GeofencesApi, "apps_geofences_api_list_geofences")
    assert hasattr(GeofencesApi, "apps_geofences_api_create_geofence")
    assert hasattr(GeofencesApi, "apps_geofences_api_get_geofence")
    assert hasattr(GeofencesApi, "apps_geofences_api_update_geofence")
    assert hasattr(GeofencesApi, "apps_geofences_api_delete_geofence")


def test_workflows_api_methods_exist():
    from spatialflow._generated.spatialflow_generated.api.workflows_api import (
        WorkflowsApi,
    )

    assert hasattr(WorkflowsApi, "apps_workflows_api_list_workflows")
    assert hasattr(WorkflowsApi, "apps_workflows_api_create_workflow")
    assert hasattr(WorkflowsApi, "apps_workflows_api_get_workflow")
    assert hasattr(WorkflowsApi, "apps_workflows_api_update_workflow")
    assert hasattr(WorkflowsApi, "apps_workflows_api_delete_workflow")
    assert hasattr(WorkflowsApi, "apps_workflows_api_toggle_workflow")

    assert hasattr(WorkflowsApi, "apps_workflows_api_execute_workflow")
    assert hasattr(WorkflowsApi, "apps_workflows_api_test_workflow")
    assert hasattr(WorkflowsApi, "apps_workflows_api_get_workflow_executions")
    assert hasattr(WorkflowsApi, "apps_workflows_api_get_workflow_execution_detail")

    assert hasattr(WorkflowsApi, "apps_workflows_api_get_workflow_performance")
    assert hasattr(WorkflowsApi, "apps_workflows_api_get_workflow_statistics")
    assert hasattr(WorkflowsApi, "apps_workflows_api_get_workflow_retry_policy")

    assert hasattr(WorkflowsApi, "apps_workflows_api_list_workflow_versions")
    assert hasattr(WorkflowsApi, "apps_workflows_api_restore_workflow_version")
    assert hasattr(WorkflowsApi, "apps_workflows_api_duplicate_workflow")
    assert hasattr(WorkflowsApi, "apps_workflows_api_export_workflow")
    assert hasattr(WorkflowsApi, "apps_workflows_api_import_workflow")

    assert hasattr(WorkflowsApi, "apps_workflows_api_update_workflow_retry_policy")
    assert hasattr(WorkflowsApi, "apps_workflows_api_list_workflow_executions")
    assert hasattr(WorkflowsApi, "apps_workflows_api_get_workflow_bottlenecks")
    assert hasattr(WorkflowsApi, "apps_workflows_api_get_workflow_step_performance")


def test_webhooks_api_methods_exist():
    from spatialflow._generated.spatialflow_generated.api.webhooks_api import (
        WebhooksApi,
    )

    assert hasattr(WebhooksApi, "apps_webhooks_api_list_webhooks")
    assert hasattr(WebhooksApi, "apps_webhooks_api_create_webhook")
    assert hasattr(WebhooksApi, "apps_webhooks_api_get_webhook")
    assert hasattr(WebhooksApi, "apps_webhooks_api_update_webhook")
    assert hasattr(WebhooksApi, "apps_webhooks_api_delete_webhook")
    assert hasattr(WebhooksApi, "apps_webhooks_api_rotate_webhook_secret")

    assert hasattr(WebhooksApi, "apps_webhooks_api_get_webhook_deliveries")
    assert hasattr(WebhooksApi, "apps_webhooks_api_get_webhook_delivery_detail")
    assert hasattr(WebhooksApi, "apps_webhooks_api_retry_webhook_delivery")

    assert hasattr(WebhooksApi, "apps_webhooks_api_get_webhook_metrics")
    assert hasattr(WebhooksApi, "apps_webhooks_api_get_webhook_success_timeline")
    assert hasattr(WebhooksApi, "apps_webhooks_api_test_webhook")

    assert hasattr(WebhooksApi, "apps_webhooks_api_list_dlq_entries")
    assert hasattr(WebhooksApi, "apps_webhooks_api_retry_from_dlq")


def test_devices_api_methods_exist():
    from spatialflow._generated.spatialflow_generated.api.devices_api import DevicesApi

    assert hasattr(DevicesApi, "apps_devices_api_list_devices")
    assert hasattr(DevicesApi, "apps_devices_api_create_device")
    assert hasattr(DevicesApi, "apps_devices_api_get_device")
    # Note: update_device is done via create_device (upsert) or specific methods
    assert hasattr(DevicesApi, "apps_devices_api_delete_device")
    assert hasattr(DevicesApi, "apps_devices_api_update_device_location")
    assert hasattr(DevicesApi, "apps_devices_api_activate_device")
    assert hasattr(DevicesApi, "apps_devices_api_deactivate_device")


def test_locations_api_methods_exist():
    from spatialflow._generated.spatialflow_generated.api.public_location_ingest_api import (
        PublicLocationIngestApi,
    )

    assert hasattr(PublicLocationIngestApi, "apps_public_locations_api_ingest_location")
    assert hasattr(
        PublicLocationIngestApi, "apps_public_locations_api_ingest_location_batch"
    )
    assert hasattr(PublicLocationIngestApi, "apps_public_locations_api_get_ingest_stats")


def test_integrations_api_methods_exist():
    from spatialflow._generated.spatialflow_generated.api.integrations_api import (
        IntegrationsApi,
    )

    assert hasattr(IntegrationsApi, "apps_integrations_api_list_integrations")
    assert hasattr(IntegrationsApi, "apps_integrations_api_create_integration")
    assert hasattr(IntegrationsApi, "apps_integrations_api_get_integration")
    assert hasattr(IntegrationsApi, "apps_integrations_api_update_integration")
    assert hasattr(IntegrationsApi, "apps_integrations_api_delete_integration")
    assert hasattr(IntegrationsApi, "apps_integrations_api_test_integration")


def test_storage_api_methods_exist():
    from spatialflow._generated.spatialflow_generated.api.storage_api import StorageApi

    assert hasattr(StorageApi, "apps_storage_api_create_presigned_url")
    assert hasattr(StorageApi, "apps_storage_api_list_files")
    assert hasattr(StorageApi, "apps_storage_api_get_download_url")
    assert hasattr(StorageApi, "apps_storage_api_delete_file")


def test_workspaces_api_methods_exist():
    from spatialflow._generated.spatialflow_generated.api.workspaces_api import (
        WorkspacesApi,
    )

    assert hasattr(WorkspacesApi, "apps_workspaces_api_get_workspace")
    assert hasattr(WorkspacesApi, "apps_workspaces_api_update_workspace")
    assert hasattr(WorkspacesApi, "apps_workspaces_api_get_workspace_usage")


def test_workflow_in_model_accepts_dicts():
    from spatialflow._generated.spatialflow_generated.models import WorkflowIn

    workflow = WorkflowIn(
        name="Test",
        nodes=[{"id": "t1", "type": "trigger", "data": {}}],
        edges=[{"id": "e1", "source": "t1", "target": "a1"}],
    )
    assert workflow.name == "Test"
    assert len(workflow.nodes) == 1
    assert len(workflow.edges) == 1


def test_shift_session_group_and_member_api_methods_exist():
    from spatialflow._generated.spatialflow_generated.api.devices_api import DevicesApi
    from spatialflow._generated.spatialflow_generated.api.geofences_api import GeofencesApi
    from spatialflow._generated.spatialflow_generated.api.workspaces_api import WorkspacesApi

    for name in (
        "start_shift",
        "pause_shift",
        "resume_shift",
        "end_shift",
        "get_device_sessions",
        "get_session_detail",
        "get_session_locations",
        "list_session_notes",
        "create_manager_session_note",
    ):
        assert hasattr(DevicesApi, f"apps_devices_api_{name}")

    for name in ("list_geofence_groups", "list_group_geofences", "test_group_point"):
        assert hasattr(GeofencesApi, f"apps_geofences_api_{name}")

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
        assert hasattr(WorkspacesApi, f"apps_workspaces_api_{name}")
