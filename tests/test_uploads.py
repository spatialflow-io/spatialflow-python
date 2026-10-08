import os
import tempfile
from unittest.mock import ANY, AsyncMock, MagicMock, patch

import pytest

from spatialflow.uploads import _extract_data, upload_geofences


class TestExtractData:
    def test_extract_from_dict(self):
        data = {"key": "value", "count": 42}
        result = _extract_data(data)
        assert result == data

    def test_extract_from_object_with_data_attr(self):
        mock_response = MagicMock()
        mock_response.data = {"upload_url": "https://s3.example.com/file"}
        result = _extract_data(mock_response)
        assert result == {"upload_url": "https://s3.example.com/file"}

    def test_extract_from_object_with_dict_attr(self):
        class SimpleObject:
            def __init__(self):
                self.field1 = "value1"
                self.field2 = 123

        obj = SimpleObject()
        result = _extract_data(obj)
        assert result["field1"] == "value1"
        assert result["field2"] == 123

    def test_extract_from_none_like(self):
        result = _extract_data(42)
        assert result == {}


class TestUploadGeofencesValidation:
    async def test_file_not_found(self):
        mock_client = MagicMock()

        with pytest.raises(FileNotFoundError, match="File not found"):
            await upload_geofences(mock_client, "/nonexistent/file.geojson")

    async def test_unsupported_file_type(self):
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
        mock_client = MagicMock()
        mock_client.storage.create_presigned_url = AsyncMock(
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
    async def test_presigned_url_missing_upload_url(self):
        from spatialflow import SpatialFlowError

        mock_client = MagicMock()

        mock_client.storage.create_presigned_url = AsyncMock(
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
        from spatialflow import SpatialFlowError

        mock_client = MagicMock()

        mock_client.storage.create_presigned_url = AsyncMock(
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
        mock_client = MagicMock()

        mock_client.storage.create_presigned_url = AsyncMock(
            return_value={
                "upload_url": "https://s3.example.com/upload",
                "file_id": "file-123",
            }
        )

        with tempfile.NamedTemporaryFile(suffix=".geojson", delete=False) as f:
            f.write(b'{"type": "FeatureCollection", "features": []}')
            temp_path = f.name

        try:
            with patch("spatialflow.uploads.aiohttp.ClientSession") as mock_session:
                mock_session.return_value.__aenter__ = AsyncMock(
                    side_effect=Exception("S3 upload attempted")
                )

                with pytest.raises(Exception, match="S3 upload attempted"):
                    await upload_geofences(mock_client, temp_path)

            mock_client.storage.create_presigned_url.assert_called_once()
        finally:
            os.unlink(temp_path)

    async def test_completes_upload_before_starting_import(self):
        mock_client = MagicMock()
        call_order = []

        mock_client.storage.create_presigned_url = AsyncMock(
            return_value={
                "upload_url": "https://s3.example.com/upload",
                "file_id": "file-123",
            }
        )

        async def complete_upload(file_id):
            call_order.append("complete")
            return {"file_id": file_id, "status": "complete"}

        async def start_import(request):
            call_order.append("import")
            return {"job_id": "job-123"}

        mock_client.storage.complete_upload = AsyncMock(side_effect=complete_upload)
        mock_client.geofences.upload = AsyncMock(side_effect=start_import)

        response = MagicMock(status=200)
        put_context = MagicMock()

        async def enter_put():
            call_order.append("s3_put")
            return response

        put_context.__aenter__ = AsyncMock(side_effect=enter_put)
        put_context.__aexit__ = AsyncMock(return_value=None)
        session = MagicMock()
        session.put.return_value = put_context
        session_context = MagicMock()
        session_context.__aenter__ = AsyncMock(return_value=session)
        session_context.__aexit__ = AsyncMock(return_value=None)

        expected_result = MagicMock()

        async def finish_poll(*args, **kwargs):
            call_order.append("poll")
            return expected_result

        with tempfile.NamedTemporaryFile(suffix=".geojson", delete=False) as f:
            content = b'{"type": "FeatureCollection", "features": []}'
            f.write(content)
            temp_path = f.name

        try:
            with (
                patch(
                    "spatialflow.uploads.aiohttp.ClientSession",
                    return_value=session_context,
                ),
                patch(
                    "spatialflow.uploads.poll_job",
                    new=AsyncMock(side_effect=finish_poll),
                ),
            ):
                result = await upload_geofences(mock_client, temp_path)

            assert result is expected_result
            assert call_order == ["s3_put", "complete", "import", "poll"]
            mock_client.storage.complete_upload.assert_awaited_once_with("file-123")
            session.put.assert_called_once_with(
                "https://s3.example.com/upload",
                data=ANY,
                headers={
                    "Content-Type": "application/geo+json",
                    "Content-Length": str(len(content)),
                    "If-None-Match": "*",
                },
            )
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
