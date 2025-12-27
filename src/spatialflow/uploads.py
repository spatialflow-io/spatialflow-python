"""
File upload helpers for SpatialFlow SDK.

Provides utilities for uploading files (GeoJSON, KML, GPX) and processing them.
"""

from pathlib import Path
from typing import Any, Callable, Optional, Union

import aiohttp

from .exceptions import SpatialFlowError, ValidationError, translate_exception
from .jobs import JobResult, poll_job


async def upload_geofences(
    client: Any,
    file_path: Union[str, Path],
    *,
    group_name: Optional[str] = None,
    timeout: float = 300,
    poll_interval: float = 2.0,
    upload_timeout: float = 60.0,
    on_status: Optional[Callable[[str, Any], None]] = None,
) -> JobResult:
    """
    Upload a geofence file and wait for processing to complete.

    This is a convenience method that:
    1. Requests a presigned upload URL
    2. Uploads the file to S3
    3. Starts the geofence import job
    4. Polls until completion

    Args:
        client: SpatialFlow client instance.
        file_path: Path to the file to upload (GeoJSON, KML, or GPX).
        group_name: Optional name for the geofence group.
        timeout: Maximum time to wait for processing in seconds. Default: 300.
        poll_interval: Time between status polls in seconds. Default: 2.0.
        upload_timeout: Maximum time to wait for S3 upload in seconds. Default: 60.0.
        on_status: Optional callback called on each poll with (status, response).

    Returns:
        JobResult with the final job state including created geofences.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValidationError: If the file type is not supported.
        SpatialFlowError: If the upload or API call fails.
        JobTimeoutError: If processing doesn't complete within timeout.
        JobFailedError: If the import job fails.

    Example:
        >>> result = await upload_geofences(
        ...     client,
        ...     "boundaries.geojson",
        ...     group_name="my-region",
        ...     timeout=120,
        ... )
        >>> print(f"Created {result.created_count} geofences")
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Get file info
    filename = file_path.name
    file_size = file_path.stat().st_size

    # Determine content type
    ext = file_path.suffix.lower()
    content_types = {
        ".geojson": "application/geo+json",
        ".json": "application/json",
        ".kml": "application/vnd.google-earth.kml+xml",
        ".gpx": "application/gpx+xml",
    }

    if ext not in content_types:
        raise ValidationError(
            f"Unsupported file type: {ext}. "
            f"Supported types: {', '.join(content_types.keys())}",
            status_code=400,
            error_code="UNSUPPORTED_FILE_TYPE",
        )

    content_type = content_types[ext]

    # Step 1: Get presigned upload URL
    try:
        presigned_response = await client.storage.apps_storage_api_create_presigned_url(
            presigned_url_request={
                "file_type": "geofences",
                "filename": filename,
                "file_size": file_size,
            }
        )
    except Exception as e:
        raise translate_exception(e) from e

    # Extract from response (handle both direct and axios-style responses)
    presigned_data = _extract_data(presigned_response)
    upload_url = presigned_data.get("upload_url")
    file_id = presigned_data.get("file_id")

    if not upload_url:
        raise SpatialFlowError(
            "Failed to get presigned upload URL from storage API. "
            "Response missing 'upload_url' field.",
            error_code="MISSING_UPLOAD_URL",
        )
    if not file_id:
        raise SpatialFlowError(
            "Failed to get file ID from storage API. "
            "Response missing 'file_id' field.",
            error_code="MISSING_FILE_ID",
        )

    # Step 2: Upload file to S3 with streaming (avoids loading large files into memory)
    s3_timeout = aiohttp.ClientTimeout(total=upload_timeout)
    async with aiohttp.ClientSession(timeout=s3_timeout) as session:
        try:
            # Stream the file directly without loading into memory
            with open(file_path, "rb") as f:
                async with session.put(
                    upload_url,
                    data=f,
                    headers={
                        "Content-Type": content_type,
                        "Content-Length": str(file_size),
                    },
                ) as resp:
                    if resp.status not in (200, 204):
                        text = await resp.text()
                        raise SpatialFlowError(
                            f"Failed to upload file to S3: {resp.status} - {text}",
                            status_code=resp.status,
                            error_code="S3_UPLOAD_FAILED",
                        )
        except aiohttp.ClientError as e:
            raise SpatialFlowError(
                f"S3 upload failed: {e}",
                error_code="S3_UPLOAD_ERROR",
            ) from e

    # Step 3: Start the geofence import job
    upload_request = {"file_id": file_id}
    if group_name:
        upload_request["group_name"] = group_name

    try:
        job_response = await client.geofences.apps_geofences_api_upload_geofences_async(
            upload_geofences_request=upload_request
        )
    except Exception as e:
        raise translate_exception(e) from e

    job_data = _extract_data(job_response)
    job_id = job_data.get("job_id")

    if not job_id:
        raise SpatialFlowError(
            "Failed to start upload job. Response missing 'job_id' field.",
            error_code="MISSING_JOB_ID",
        )

    # Step 4: Poll for completion
    async def fetch_status():
        return await client.geofences.apps_geofences_api_get_upload_job_status(
            job_id=job_id
        )

    return await poll_job(
        fetch_status,
        timeout=timeout,
        poll_interval=poll_interval,
        on_status=on_status,
    )


def _extract_data(response: Any) -> dict:
    """Extract data from response, handling axios-style responses."""
    if hasattr(response, "data"):
        return response.data if isinstance(response.data, dict) else response.data.__dict__
    if isinstance(response, dict):
        return response
    if hasattr(response, "__dict__"):
        return response.__dict__
    return {}
