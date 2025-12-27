"""Tests for file upload helpers."""

import os
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from spatialflow.uploads import upload_geofences, _extract_data


class TestExtractData:
    """Test the _extract_data helper function."""

    def test_extract_from_dict(self):
        """Test extracting data from a plain dict."""
        data = {"key": "value", "count": 42}
        result = _extract_data(data)
        assert result == data

    def test_extract_from_object_with_data_attr(self):
        """Test extracting data from axios-style response with .data."""
        mock_response = MagicMock()
        mock_response.data = {"upload_url": "https://s3.example.com/file"}
        result = _extract_data(mock_response)
        assert result == {"upload_url": "https://s3.example.com/file"}

    def test_extract_from_object_with_dict_attr(self):
        """Test extracting data from object with __dict__."""
        class SimpleObject:
            def __init__(self):
                self.field1 = "value1"
                self.field2 = 123

        obj = SimpleObject()
        result = _extract_data(obj)
        assert result["field1"] == "value1"
        assert result["field2"] == 123

    def test_extract_from_none_like(self):
        """Test extracting data from non-dict-like object."""
        result = _extract_data(42)
        assert result == {}


class TestUploadGeofencesValidation:
    """Test upload_geofences validation logic."""

    async def test_file_not_found(self):
        """Test that missing file raises FileNotFoundError."""
        mock_client = MagicMock()

        with pytest.raises(FileNotFoundError, match="File not found"):
            await upload_geofences(mock_client, "/nonexistent/file.geojson")

    async def test_unsupported_file_type(self):
        """Test that unsupported file types raise ValidationError."""
        from spatialflow import ValidationError

        mock_client = MagicMock()

        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
            f.write(b"test content")
            temp_path = f.name

        try:
            with pytest.raises(ValidationError, match="Unsupported file type"):
                await upload_geofences(mock_client, temp_path)
        finally:
            os.unlink(temp_path)

    async def test_supported_file_types(self):
        """Test that supported file types are accepted (until API call)."""
        mock_client = MagicMock()
        # Make the storage API call fail immediately
        mock_client.storage.apps_storage_api_create_presigned_url = AsyncMock(
            side_effect=Exception("API call made - file type accepted")
        )

        supported_extensions = [".geojson", ".json", ".kml", ".gpx"]

        for ext in supported_extensions:
            with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as f:
                f.write(b'{"type": "FeatureCollection", "features": []}')
                temp_path = f.name

            try:
                with pytest.raises(Exception, match="API call made"):
                    await upload_geofences(mock_client, temp_path)
            finally:
                os.unlink(temp_path)


class TestUploadGeofencesMocked:
    """Test upload_geofences with mocked dependencies."""

    async def test_presigned_url_missing_upload_url(self):
        """Test that missing upload_url raises SpatialFlowError."""
        from spatialflow import SpatialFlowError

        mock_client = MagicMock()

        # Return dict without upload_url
        mock_client.storage.apps_storage_api_create_presigned_url = AsyncMock(
            return_value={"file_id": "file-123"}
        )

        with tempfile.NamedTemporaryFile(suffix=".geojson", delete=False) as f:
            f.write(b'{"type": "FeatureCollection", "features": []}')
            temp_path = f.name

        try:
            with pytest.raises(SpatialFlowError, match="missing 'upload_url'"):
                await upload_geofences(mock_client, temp_path)
        finally:
            os.unlink(temp_path)

    async def test_presigned_url_missing_file_id(self):
        """Test that missing file_id raises SpatialFlowError."""
        from spatialflow import SpatialFlowError

        mock_client = MagicMock()

        # Return dict without file_id
        mock_client.storage.apps_storage_api_create_presigned_url = AsyncMock(
            return_value={"upload_url": "https://s3.example.com/upload"}
        )

        with tempfile.NamedTemporaryFile(suffix=".geojson", delete=False) as f:
            f.write(b'{"type": "FeatureCollection", "features": []}')
            temp_path = f.name

        try:
            with pytest.raises(SpatialFlowError, match="missing 'file_id'"):
                await upload_geofences(mock_client, temp_path)
        finally:
            os.unlink(temp_path)

    async def test_s3_upload_called_with_presigned_url(self):
        """Test that S3 upload is attempted with presigned URL."""
        mock_client = MagicMock()

        # Return valid presigned URL response
        mock_client.storage.apps_storage_api_create_presigned_url = AsyncMock(
            return_value={
                "upload_url": "https://s3.example.com/upload",
                "file_id": "file-123",
            }
        )

        with tempfile.NamedTemporaryFile(suffix=".geojson", delete=False) as f:
            f.write(b'{"type": "FeatureCollection", "features": []}')
            temp_path = f.name

        try:
            # Mock aiohttp session - make S3 upload fail with identifiable error
            with patch("spatialflow.uploads.aiohttp.ClientSession") as mock_session:
                mock_session.return_value.__aenter__ = AsyncMock(
                    side_effect=Exception("S3 upload attempted")
                )

                with pytest.raises(Exception, match="S3 upload attempted"):
                    await upload_geofences(mock_client, temp_path)

            # Verify storage API was called
            mock_client.storage.apps_storage_api_create_presigned_url.assert_called_once()
        finally:
            os.unlink(temp_path)


# Integration test - env-gated
@pytest.mark.skipif(
    not os.environ.get("SPATIALFLOW_API_KEY")
    or not os.environ.get("SPATIALFLOW_RUN_UPLOAD_TESTS"),
    reason="SPATIALFLOW_API_KEY and SPATIALFLOW_RUN_UPLOAD_TESTS required",
)
class TestUploadGeofencesIntegration:
    """Integration tests for upload_geofences (requires live API + S3)."""

    @pytest.fixture
    async def client(self):
        """Create SpatialFlow client for testing."""
        from spatialflow import SpatialFlow

        token = os.environ.get("SPATIALFLOW_API_KEY")
        base_url = os.environ.get(
            "SPATIALFLOW_BASE_URL", "https://api.spatialflow.io"
        )

        if token.startswith("sf_"):
            return SpatialFlow(api_key=token, base_url=base_url)
        else:
            return SpatialFlow(access_token=token, base_url=base_url)

    async def test_upload_small_geojson(self, client, tmp_path):
        """Test uploading a small GeoJSON file."""
        # Create a simple GeoJSON file
        geojson_path = tmp_path / "test_geofence.geojson"
        geojson_path.write_text(
            """{
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {"name": "SDK Upload Test"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [-122.4, 37.8],
                        [-122.4, 37.7],
                        [-122.3, 37.7],
                        [-122.3, 37.8],
                        [-122.4, 37.8]
                    ]]
                }
            }]
        }"""
        )

        result = await upload_geofences(
            client,
            geojson_path,
            group_name="sdk-integration-test",
            timeout=60,
        )

        assert result.status == "completed"
        assert result.created_count >= 1
