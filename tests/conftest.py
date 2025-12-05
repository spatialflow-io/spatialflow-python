"""Pytest configuration and fixtures for SDK tests."""

import pytest


@pytest.fixture
def sample_geojson():
    """Sample GeoJSON for testing."""
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "Test Geofence"},
                "geometry": {
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
            }
        ],
    }


@pytest.fixture
def webhook_secret():
    """Sample webhook secret for testing."""
    return "whsec_test_secret_key_12345"
