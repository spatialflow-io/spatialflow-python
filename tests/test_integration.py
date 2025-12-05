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

    The SPATIALFLOW_API_KEY env var can contain either:
    - An API key (starts with "sf_") - uses api_key parameter
    - A JWT token (starts with "ey") - uses access_token parameter
    """
    from spatialflow import SpatialFlow

    token = os.environ.get("SPATIALFLOW_API_KEY")
    base_url = os.environ.get("SPATIALFLOW_BASE_URL", "https://api.spatialflow.io")

    # Detect token type
    if token.startswith("sf_"):
        return SpatialFlow(api_key=token, base_url=base_url)
    else:
        return SpatialFlow(access_token=token, base_url=base_url)


class TestClientIntegration:
    """Smoke tests to verify SDK works against real API."""

    async def test_client_can_authenticate(self, client):
        """Test that client can authenticate and make a basic request."""
        # List geofences - should work even if empty
        response = await client.geofences.apps_geofences_api_list_geofences(limit=1)

        # Verify response structure - generated models use 'geofences' and 'count'
        assert hasattr(response, "geofences")
        assert hasattr(response, "count")

    async def test_client_handles_auth_error(self):
        """Test that invalid API key raises AuthenticationError."""
        from spatialflow import SpatialFlow
        from spatialflow._generated.spatialflow_generated.exceptions import UnauthorizedException

        base_url = os.environ.get("SPATIALFLOW_BASE_URL", "https://api.spatialflow.io")
        bad_client = SpatialFlow(api_key="sf_invalid_key_12345", base_url=base_url)

        # The generated client raises UnauthorizedException for 401s
        with pytest.raises(UnauthorizedException):
            await bad_client.geofences.apps_geofences_api_list_geofences()

    async def test_pagination_works(self, client):
        """Test that pagination helper works with real API."""
        from spatialflow import paginate

        # Just verify we can iterate without error
        count = 0
        async for geofence in paginate(
            lambda offset, limit: client.geofences.apps_geofences_api_list_geofences(
                offset=offset, limit=limit
            ),
            limit=10,
        ):
            count += 1
            if count >= 5:  # Don't iterate through everything
                break

        # Test passed if no exceptions

    async def test_not_found_error(self, client):
        """Test that 404 raises NotFoundError."""
        from spatialflow._generated.spatialflow_generated.exceptions import NotFoundException
        import uuid

        fake_id = str(uuid.uuid4())

        with pytest.raises(NotFoundException):
            await client.geofences.apps_geofences_api_get_geofence(geofence_id=fake_id)


class TestGeofencesCRUD:
    """Test geofence CRUD operations (creates real data - use with caution)."""

    @pytest.mark.skipif(
        not os.environ.get("SPATIALFLOW_RUN_CRUD_TESTS"),
        reason="SPATIALFLOW_RUN_CRUD_TESTS not set - skipping CRUD tests",
    )
    async def test_create_and_delete_geofence(self, client):
        """Test creating and deleting a geofence."""
        from spatialflow import models

        # Create
        geofence = await client.geofences.apps_geofences_api_create_geofence(
            create_geofence_request=models.CreateGeofenceRequest(
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

        # Delete
        await client.geofences.apps_geofences_api_delete_geofence(id=geofence.id)

        # Verify deleted
        from spatialflow import NotFoundError

        with pytest.raises(NotFoundError):
            await client.geofences.apps_geofences_api_get_geofence(id=geofence.id)
