"""
Integration/smoke tests for SpatialFlow Python SDK.

These tests run against a real API and are skipped unless SPATIALFLOW_API_KEY is set.
Run with: SPATIALFLOW_API_KEY=sf_xxx pytest tests/test_integration.py -v
"""

import os

import pytest

pytestmark = pytest.mark.skipif(
    not os.environ.get("SPATIALFLOW_API_KEY"),
    reason="SPATIALFLOW_API_KEY not set - skipping integration tests",
)


@pytest.fixture
async def client():
    """Create a SpatialFlow client for integration testing.

    Note: The client must be created within an async context because
    the aiohttp-based generated client creates a TCPConnector at init.
    Using async context manager ensures proper cleanup.

    The SPATIALFLOW_API_KEY env var can contain either:
    - An API key (starts with "sf_") - uses api_key parameter
    - A JWT token (starts with "ey") - uses access_token parameter
    """
    from spatialflow import SpatialFlow

    token = os.environ.get("SPATIALFLOW_API_KEY")
    base_url = os.environ.get("SPATIALFLOW_BASE_URL", "https://api.spatialflow.io")

    if token.startswith("sf_"):
        async with SpatialFlow(api_key=token, base_url=base_url) as client:
            yield client
    else:
        async with SpatialFlow(access_token=token, base_url=base_url) as client:
            yield client


class TestClientIntegration:
    async def test_client_can_authenticate(self, client):
        response = await client.geofences.list(limit=1)

        # Generated models use 'geofences' and 'count'
        assert hasattr(response, "geofences")
        assert hasattr(response, "count")

    async def test_client_handles_auth_error(self):
        from spatialflow import SpatialFlow, AuthenticationError

        base_url = os.environ.get("SPATIALFLOW_BASE_URL", "https://api.spatialflow.io")
        bad_client = SpatialFlow(api_key="sf_invalid_key_12345", base_url=base_url)

        # The clean API wraps UnauthorizedException into AuthenticationError
        with pytest.raises(AuthenticationError):
            await bad_client.geofences.list()

    async def test_pagination_works(self, client):
        from spatialflow import paginate_geofences

        items = []
        async for geofence in paginate_geofences(
            lambda offset, limit: client.geofences.list(offset=offset, limit=limit),
            limit=10,
        ):
            items.append(geofence)
            if len(items) >= 5:  # Don't iterate through everything
                break

        response = await client.geofences.list(limit=1)
        if response.count > 0:
            assert len(items) > 0, "Pagination should yield items when geofences exist"

    async def test_not_found_error(self, client):
        from spatialflow import NotFoundError
        import uuid

        fake_id = str(uuid.uuid4())

        # The clean API wraps NotFoundException into NotFoundError
        with pytest.raises(NotFoundError):
            await client.geofences.get(geofence_id=fake_id)


class TestGeofencesCRUD:
    """Creates real data - use with caution."""

    @pytest.mark.skipif(
        not os.environ.get("SPATIALFLOW_RUN_CRUD_TESTS"),
        reason="SPATIALFLOW_RUN_CRUD_TESTS not set - skipping CRUD tests",
    )
    async def test_create_and_delete_geofence(self, client):
        from spatialflow import models

        geofence = await client.geofences.create(
            models.CreateGeofenceRequest(
                name="SDK Integration Test Geofence",
                geometry={
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [-122.4, 37.8],
                            [-122.4, 37.7],
                            [-122.3, 37.7],
                            [-122.3, 37.8],
                            [-122.4, 37.8],
                        ]
                    ],
                },
            )
        )

        assert geofence.name == "SDK Integration Test Geofence"
        assert geofence.id is not None

        await client.geofences.delete(geofence_id=geofence.id)

        # Backend uses soft delete, so geofence still exists but is_active should be False
        deleted_geofence = await client.geofences.get(geofence_id=geofence.id)
        assert deleted_geofence.is_active is False, "Geofence should be soft-deleted"


class TestWorkflowExecution:
    @pytest.mark.skipif(
        not os.environ.get("SPATIALFLOW_RUN_CRUD_TESTS"),
        reason="SPATIALFLOW_RUN_CRUD_TESTS not set - skipping CRUD tests",
    )
    async def test_workflow_create_and_execute(self, client):
        import uuid

        from spatialflow import build_geofence_webhook_workflow

        # Use unique name to avoid conflicts with previous test runs
        workflow_name = f"SDK Test Workflow {uuid.uuid4().hex[:8]}"

        # TriggerType is a Literal, use string value directly
        # geofence_ids is required, use a placeholder UUID
        workflow_in = build_geofence_webhook_workflow(
            name=workflow_name,
            geofence_ids=["00000000-0000-0000-0000-000000000000"],
            trigger_type="geofence_enter",
            webhook_url="https://httpbin.org/post",
        )

        # Builder returns WorkflowIn directly
        workflow = await client.workflows.create(workflow_in)
        assert workflow.id is not None
        assert workflow.name == workflow_name

        try:
            fetched = await client.workflows.get(workflow_id=workflow.id)
            assert fetched.id == workflow.id

            executions = await client.workflows.list_executions(workflow_id=workflow.id, limit=10)
            assert hasattr(executions, "executions") or isinstance(executions, list)

            performance = await client.workflows.get_performance(workflow_id=workflow.id)
            assert performance is not None

            stats = await client.workflows.get_statistics(workflow_id=workflow.id)
            assert stats is not None

            # Toggle is not tested here because newly created workflows are in 'draft'
            # status and cannot be toggled until published via the UI. Testing toggle
            # would require publishing the workflow first.

        finally:
            await client.workflows.delete(workflow_id=workflow.id)


class TestWebhookOperations:
    @pytest.mark.skipif(
        not os.environ.get("SPATIALFLOW_RUN_CRUD_TESTS"),
        reason="SPATIALFLOW_RUN_CRUD_TESTS not set - skipping CRUD tests",
    )
    async def test_webhook_create_and_test(self, client):
        import uuid

        from spatialflow import models, ValidationError
        from spatialflow._generated.spatialflow_generated.exceptions import (
            BadRequestException,
        )

        # Use unique name to avoid conflicts with previous test runs
        webhook_name = f"SDK Test Webhook {uuid.uuid4().hex[:8]}"

        try:
            webhook = await client.webhooks.create(
                models.CreateWebhookRequest(
                    name=webhook_name,
                    url="https://httpbin.org/post",
                    events=["geofence.entered"],
                )
            )
        except ValidationError as e:
            # Distinguish a plan-limit rejection from other validation errors
            if e.__cause__ and hasattr(e.__cause__, "body"):
                if "limit" in str(e.__cause__.body).lower():
                    pytest.skip("Webhook limit reached on this plan")
            raise

        assert webhook.id is not None
        assert webhook.name == webhook_name

        try:
            # Must provide a matching event_type
            test_result = await client.webhooks.test(
                webhook_id=webhook.id,
                request=models.TestWebhookRequest(event_type="geofence.entered"),
            )
            assert test_result is not None
            # httpbin.org should return success
            assert hasattr(test_result, "success") or "success" in str(test_result)

            deliveries = await client.webhooks.list_deliveries(webhook_id=webhook.id, limit=10)
            assert deliveries is not None

        finally:
            await client.webhooks.delete(webhook_id=webhook.id)


class TestAccountOperations:
    async def test_get_profile(self, client):
        profile = await client.account.get_profile()
        assert profile is not None
        assert hasattr(profile, "email") or "email" in str(profile)

    async def test_get_dashboard_metrics(self, client):
        metrics = await client.account.get_dashboard_metrics()
        assert metrics is not None
        assert hasattr(metrics, "events_total") or hasattr(metrics, "active_workflows")

    @pytest.mark.skipif(
        not os.environ.get("SPATIALFLOW_RUN_CRUD_TESTS"),
        reason="SPATIALFLOW_RUN_CRUD_TESTS not set - skipping CRUD tests",
    )
    async def test_api_key_lifecycle(self, client):
        import uuid

        from spatialflow import models

        # Use unique name to avoid conflicts with previous test runs
        key_name = f"SDK Test Key {uuid.uuid4().hex[:8]}"

        # ApiKeyCreateResponse has: message, api_key (dict with id, key, name, etc.)
        new_key_response = await client.account.create_api_key(
            models.ApiKeyCreateRequest(name=key_name)
        )
        assert new_key_response is not None
        assert hasattr(new_key_response, "api_key") or "api_key" in str(new_key_response)
        key_id = new_key_response.api_key.get("id") or new_key_response.api_key["id"]

        try:
            keys = await client.account.list_api_keys()
            assert any(
                getattr(k, "id", None) == key_id or (hasattr(k, "get") and k.get("id") == key_id)
                for k in keys
            )

            fetched = await client.account.get_api_key(key_id=key_id)
            assert fetched is not None

            # Use unique name to avoid conflicts
            updated_name = f"SDK Test Key Updated {uuid.uuid4().hex[:8]}"
            updated = await client.account.update_api_key(
                key_id=key_id,
                request=models.ApiKeyUpdateRequest(name=updated_name),
            )
            assert updated is not None

            # Rotate key is not tested here because the backend appends "(Rotated)"
            # to the name which can conflict with previously rotated keys in the
            # workspace. Testing rotate would require cleaning up old rotated keys first.

        finally:
            await client.account.delete_api_key(key_id=key_id)


class TestWorkspacesOperations:
    async def test_get_workspace(self, client):
        workspace = await client.workspaces.get()
        assert workspace is not None
        assert hasattr(workspace, "id") or "id" in str(workspace)
        assert hasattr(workspace, "name") or "name" in str(workspace)

    async def test_get_usage(self, client):
        usage = await client.workspaces.get_usage()
        assert usage is not None
        assert hasattr(usage, "event_units") or "event" in str(usage).lower()
        assert hasattr(usage, "tier") or "tier" in str(usage).lower()


class TestErrorTranslation:
    async def test_validation_error_on_invalid_geometry(self, client):
        from spatialflow import models, ValidationError

        with pytest.raises(ValidationError) as exc_info:
            await client.geofences.create(
                models.CreateGeofenceRequest(
                    name="Invalid Geofence",
                    geometry={
                        "type": "Polygon",
                        "coordinates": [
                            # Invalid: only 2 points (need at least 4 for closed polygon)
                            [[-122.4, 37.8], [-122.3, 37.7]],
                        ],
                    },
                )
            )

        assert exc_info.value is not None

    async def test_validation_error_on_missing_required_field(self, client):
        from spatialflow import ValidationError
        from spatialflow._generated.spatialflow_generated.exceptions import (
            ApiException,
        )

        # May raise ValidationError or ApiException depending on where validation happens
        with pytest.raises((ValidationError, ApiException, Exception)):
            await client.raw.geofences.apps_geofences_api_create_geofence(
                create_geofence_request={"name": "No Geometry"}
            )


class TestPaginationBoundary:
    async def test_pagination_with_max_limit(self, client):
        response = await client.geofences.list(limit=100, offset=0)
        assert hasattr(response, "geofences")
        assert hasattr(response, "count")

        assert response.count >= 0
        assert len(response.geofences) <= 100

    async def test_pagination_offset_behavior(self, client):
        page1 = await client.geofences.list(limit=5, offset=0)

        if page1.count > 5:
            page2 = await client.geofences.list(limit=5, offset=5)

            page1_ids = {g.id for g in page1.geofences}
            page2_ids = {g.id for g in page2.geofences}
            assert page1_ids.isdisjoint(page2_ids), "Pages should not overlap"

    async def test_pagination_beyond_count(self, client):
        response = await client.geofences.list(limit=1, offset=0)
        total = response.count

        beyond = await client.geofences.list(limit=10, offset=total + 100)
        assert len(beyond.geofences) == 0, "Should return empty list when offset > count"
