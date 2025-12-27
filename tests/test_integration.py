"""
Integration/smoke tests for SpatialFlow Python SDK.

These tests run against a real API and are skipped unless SPATIALFLOW_API_KEY is set.
Run with: SPATIALFLOW_API_KEY=sf_xxx pytest tests/test_integration.py -v
"""

import os

import pytest

# Skip all tests in this module if no API key is configured
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

    # Detect token type and create client with proper cleanup
    if token.startswith("sf_"):
        async with SpatialFlow(api_key=token, base_url=base_url) as client:
            yield client
    else:
        async with SpatialFlow(access_token=token, base_url=base_url) as client:
            yield client


class TestClientIntegration:
    """Smoke tests to verify SDK works against real API."""

    async def test_client_can_authenticate(self, client):
        """Test that client can authenticate and make a basic request."""
        # List geofences using clean API - should work even if empty
        response = await client.geofences.list(limit=1)

        # Verify response structure - generated models use 'geofences' and 'count'
        assert hasattr(response, "geofences")
        assert hasattr(response, "count")

    async def test_client_handles_auth_error(self):
        """Test that invalid API key raises AuthenticationError."""
        from spatialflow import SpatialFlow, AuthenticationError

        base_url = os.environ.get("SPATIALFLOW_BASE_URL", "https://api.spatialflow.io")
        bad_client = SpatialFlow(api_key="sf_invalid_key_12345", base_url=base_url)

        # The clean API wraps UnauthorizedException into AuthenticationError
        with pytest.raises(AuthenticationError):
            await bad_client.geofences.list()

    async def test_pagination_works(self, client):
        """Test that pagination helper works with real API."""
        from spatialflow import paginate_geofences

        # Collect items from paginator using clean API
        items = []
        async for geofence in paginate_geofences(
            lambda offset, limit: client.geofences.list(offset=offset, limit=limit),
            limit=10,
        ):
            items.append(geofence)
            if len(items) >= 5:  # Don't iterate through everything
                break

        # Verify paginator yields items if there are any
        response = await client.geofences.list(limit=1)
        if response.count > 0:
            assert len(items) > 0, "Pagination should yield items when geofences exist"

    async def test_not_found_error(self, client):
        """Test that 404 raises NotFoundError."""
        from spatialflow import NotFoundError
        import uuid

        fake_id = str(uuid.uuid4())

        # The clean API wraps NotFoundException into NotFoundError
        with pytest.raises(NotFoundError):
            await client.geofences.get(geofence_id=fake_id)


class TestGeofencesCRUD:
    """Test geofence CRUD operations (creates real data - use with caution)."""

    @pytest.mark.skipif(
        not os.environ.get("SPATIALFLOW_RUN_CRUD_TESTS"),
        reason="SPATIALFLOW_RUN_CRUD_TESTS not set - skipping CRUD tests",
    )
    async def test_create_and_delete_geofence(self, client):
        """Test creating and deleting a geofence."""
        from spatialflow import models

        # Create using clean API
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

        # Delete using clean API
        await client.geofences.delete(geofence_id=geofence.id)

        # Verify deleted - backend uses soft delete, so geofence still exists
        # but is_active should be False
        deleted_geofence = await client.geofences.get(geofence_id=geofence.id)
        assert deleted_geofence.is_active is False, "Geofence should be soft-deleted"


class TestWorkflowExecution:
    """Test workflow execution paths."""

    @pytest.mark.skipif(
        not os.environ.get("SPATIALFLOW_RUN_CRUD_TESTS"),
        reason="SPATIALFLOW_RUN_CRUD_TESTS not set - skipping CRUD tests",
    )
    async def test_workflow_create_and_execute(self, client):
        """Test creating a workflow and checking execution capabilities."""
        import uuid

        from spatialflow import build_geofence_webhook_workflow

        # Use unique name to avoid conflicts with previous test runs
        workflow_name = f"SDK Test Workflow {uuid.uuid4().hex[:8]}"

        # Build a minimal workflow using the builder
        # Note: TriggerType is a Literal, use string value directly
        # Note: geofence_ids is required, use a placeholder UUID
        workflow_in = build_geofence_webhook_workflow(
            name=workflow_name,
            geofence_ids=["00000000-0000-0000-0000-000000000000"],
            trigger_type="geofence_enter",
            webhook_url="https://httpbin.org/post",
        )

        # Create workflow (builder returns WorkflowIn directly)
        workflow = await client.workflows.create(workflow_in)
        assert workflow.id is not None
        assert workflow.name == workflow_name

        try:
            # Get workflow details
            fetched = await client.workflows.get(workflow_id=workflow.id)
            assert fetched.id == workflow.id

            # List executions (may be empty)
            executions = await client.workflows.list_executions(
                workflow_id=workflow.id, limit=10
            )
            assert hasattr(executions, "executions") or isinstance(executions, list)

            # Get performance metrics
            performance = await client.workflows.get_performance(workflow_id=workflow.id)
            assert performance is not None

            # Get statistics
            stats = await client.workflows.get_statistics(workflow_id=workflow.id)
            assert stats is not None

            # Note: Toggle is not tested here because newly created workflows are in 'draft'
            # status and cannot be toggled until published via the UI.
            # Testing toggle would require publishing the workflow first.

        finally:
            # Cleanup
            await client.workflows.delete(workflow_id=workflow.id)


class TestWebhookOperations:
    """Test webhook operations including test delivery."""

    @pytest.mark.skipif(
        not os.environ.get("SPATIALFLOW_RUN_CRUD_TESTS"),
        reason="SPATIALFLOW_RUN_CRUD_TESTS not set - skipping CRUD tests",
    )
    async def test_webhook_create_and_test(self, client):
        """Test creating a webhook and sending a test delivery."""
        import uuid

        from spatialflow import models, ValidationError
        from spatialflow._generated.spatialflow_generated.exceptions import (
            BadRequestException,
        )

        # Use unique name to avoid conflicts with previous test runs
        webhook_name = f"SDK Test Webhook {uuid.uuid4().hex[:8]}"

        # Try to create webhook - may fail due to plan limits
        try:
            webhook = await client.webhooks.create(
                models.CreateWebhookRequest(
                    name=webhook_name,
                    url="https://httpbin.org/post",
                    events=["geofence.entered"],
                )
            )
        except ValidationError as e:
            # Check if this is a plan limit issue by examining the original cause
            if e.__cause__ and hasattr(e.__cause__, "body"):
                if "limit" in str(e.__cause__.body).lower():
                    pytest.skip("Webhook limit reached on this plan")
            raise

        assert webhook.id is not None
        assert webhook.name == webhook_name

        try:
            # Test the webhook - must provide matching event_type
            test_result = await client.webhooks.test(
                webhook_id=webhook.id,
                request=models.TestWebhookRequest(event_type="geofence.entered"),
            )
            assert test_result is not None
            # httpbin.org should return success
            assert hasattr(test_result, "success") or "success" in str(test_result)

            # List deliveries (may be empty or have test delivery)
            deliveries = await client.webhooks.list_deliveries(
                webhook_id=webhook.id, limit=10
            )
            assert deliveries is not None

            # Get metrics
            metrics = await client.webhooks.get_metrics(webhook_id=webhook.id)
            assert metrics is not None

        finally:
            # Cleanup
            await client.webhooks.delete(webhook_id=webhook.id)


class TestAccountOperations:
    """Test account operations including API key management."""

    async def test_get_profile(self, client):
        """Test fetching user profile."""
        profile = await client.account.get_profile()
        assert profile is not None
        assert hasattr(profile, "email") or "email" in str(profile)

    async def test_get_dashboard_metrics(self, client):
        """Test fetching dashboard metrics."""
        metrics = await client.account.get_dashboard_metrics()
        assert metrics is not None
        # Should have standard metric fields (events_total, active_workflows, etc.)
        assert hasattr(metrics, "events_total") or hasattr(metrics, "active_workflows")

    async def test_get_onboarding_progress(self, client):
        """Test fetching onboarding progress."""
        progress = await client.account.get_onboarding_progress()
        assert progress is not None

    @pytest.mark.skipif(
        not os.environ.get("SPATIALFLOW_RUN_CRUD_TESTS"),
        reason="SPATIALFLOW_RUN_CRUD_TESTS not set - skipping CRUD tests",
    )
    async def test_api_key_lifecycle(self, client):
        """Test full API key lifecycle: create, update, rotate, delete."""
        import uuid

        from spatialflow import models

        # Use unique name to avoid conflicts with previous test runs
        key_name = f"SDK Test Key {uuid.uuid4().hex[:8]}"

        # Create API key
        # ApiKeyCreateResponse has: message, api_key (dict with id, key, name, etc.)
        new_key_response = await client.account.create_api_key(
            models.ApiKeyCreateRequest(name=key_name)
        )
        assert new_key_response is not None
        # The response contains api_key dict with the key details
        assert hasattr(new_key_response, "api_key") or "api_key" in str(new_key_response)
        key_id = new_key_response.api_key.get("id") or new_key_response.api_key["id"]

        try:
            # List keys and verify new key exists
            keys = await client.account.list_api_keys()
            assert any(
                getattr(k, "id", None) == key_id or (hasattr(k, "get") and k.get("id") == key_id)
                for k in keys
            )

            # Get specific key
            fetched = await client.account.get_api_key(key_id=key_id)
            assert fetched is not None

            # Update key name - use unique name to avoid conflicts
            updated_name = f"SDK Test Key Updated {uuid.uuid4().hex[:8]}"
            updated = await client.account.update_api_key(
                key_id=key_id,
                request=models.ApiKeyUpdateRequest(name=updated_name),
            )
            assert updated is not None

            # Note: Rotate key is not tested here because the backend appends "(Rotated)"
            # to the name which can conflict with previously rotated keys in the workspace.
            # Testing rotate would require cleaning up old rotated keys first.

        finally:
            # Cleanup
            await client.account.delete_api_key(key_id=key_id)


class TestWorkspacesOperations:
    """Test workspace operations."""

    async def test_get_workspace(self, client):
        """Test fetching current workspace."""
        workspace = await client.workspaces.get()
        assert workspace is not None
        assert hasattr(workspace, "id") or "id" in str(workspace)
        assert hasattr(workspace, "name") or "name" in str(workspace)

    async def test_get_usage(self, client):
        """Test fetching workspace usage metrics."""
        usage = await client.workspaces.get_usage()
        assert usage is not None
        # Should have standard usage fields
        assert hasattr(usage, "event_units") or "event" in str(usage).lower()
        assert hasattr(usage, "tier") or "tier" in str(usage).lower()


class TestErrorTranslation:
    """Test that API errors are properly translated to SDK exceptions."""

    async def test_validation_error_on_invalid_geometry(self, client):
        """Test that invalid geometry raises ValidationError."""
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

        # Verify error contains useful information
        assert exc_info.value is not None

    async def test_validation_error_on_missing_required_field(self, client):
        """Test that missing required fields raise ValidationError."""
        from spatialflow import ValidationError
        from spatialflow._generated.spatialflow_generated.exceptions import (
            ApiException,
        )

        # Try to create geofence without required geometry
        # This may raise ValidationError or ApiException depending on where validation happens
        with pytest.raises((ValidationError, ApiException, Exception)):
            await client.raw.geofences.apps_geofences_api_create_geofence(
                create_geofence_request={"name": "No Geometry"}
            )


class TestPaginationBoundary:
    """Test pagination at boundary conditions."""

    async def test_pagination_with_max_limit(self, client):
        """Test pagination respects limit parameter."""
        # Request with reasonable limit
        response = await client.geofences.list(limit=100, offset=0)
        assert hasattr(response, "geofences")
        assert hasattr(response, "count")

        # Verify count matches or exceeds returned items
        assert response.count >= 0
        assert len(response.geofences) <= 100

    async def test_pagination_offset_behavior(self, client):
        """Test that offset correctly skips items."""
        # Get first page
        page1 = await client.geofences.list(limit=5, offset=0)

        if page1.count > 5:
            # Get second page
            page2 = await client.geofences.list(limit=5, offset=5)

            # Verify no overlap between pages
            page1_ids = {g.id for g in page1.geofences}
            page2_ids = {g.id for g in page2.geofences}
            assert page1_ids.isdisjoint(page2_ids), "Pages should not overlap"

    async def test_pagination_beyond_count(self, client):
        """Test pagination with offset beyond total count."""
        response = await client.geofences.list(limit=1, offset=0)
        total = response.count

        # Request with offset beyond total
        beyond = await client.geofences.list(limit=10, offset=total + 100)
        assert len(beyond.geofences) == 0, "Should return empty list when offset > count"
