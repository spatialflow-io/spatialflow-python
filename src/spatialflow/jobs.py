"""
Async job polling helpers for SpatialFlow SDK.

Provides utilities for polling long-running jobs like file uploads.
"""

import asyncio
from typing import Any, Callable, Dict, Optional, TypeVar

from .exceptions import SpatialFlowError, TimeoutError

T = TypeVar("T")


class JobTimeoutError(TimeoutError):
    """Raised when a job polling operation times out."""

    def __init__(self, job_id: str, timeout: float, last_status: Optional[str] = None):
        self.job_id = job_id
        self.timeout = timeout
        self.last_status = last_status
        message = f"Job {job_id} did not complete within {timeout} seconds"
        if last_status:
            message += f" (last status: {last_status})"
        super().__init__(message)


class JobFailedError(SpatialFlowError):
    """Raised when a polled job fails."""

    def __init__(
        self,
        job_id: str,
        error_message: Optional[str] = None,
        results: Optional[Dict[str, Any]] = None,
    ):
        self.job_id = job_id
        self.error_message = error_message
        self.results = results
        message = f"Job {job_id} failed"
        if error_message:
            message += f": {error_message}"
        super().__init__(message)


class JobResult:
    """Result of a completed job."""

    def __init__(
        self,
        job_id: str,
        status: str,
        created_count: int = 0,
        failed_count: int = 0,
        total_features: int = 0,
        results: Optional[Dict[str, Any]] = None,
        duration: Optional[float] = None,
        raw_response: Optional[Any] = None,
    ):
        self.job_id = job_id
        self.status = status
        self.created_count = created_count
        self.failed_count = failed_count
        self.total_features = total_features
        self.results = results or {}
        self.duration = duration
        self.raw_response = raw_response

    @property
    def created_geofences(self) -> list:
        """List of created geofence info (id, name)."""
        return self.results.get("created_geofences", [])

    @property
    def errors(self) -> list:
        """List of errors that occurred during processing."""
        return self.results.get("errors", [])

    @property
    def warnings(self) -> list:
        """List of warnings from processing."""
        return self.results.get("warnings", [])

    def __repr__(self) -> str:
        return (
            f"JobResult(job_id={self.job_id!r}, status={self.status!r}, "
            f"created={self.created_count}, failed={self.failed_count})"
        )


async def poll_job(
    fetch_status: Callable[[], Any],
    *,
    timeout: float = 300,
    poll_interval: float = 2.0,
    terminal_statuses: tuple = ("completed", "failed"),
    on_status: Optional[Callable[[str, Any], None]] = None,
    extract_job_id: Optional[Callable[[Any], str]] = None,
    extract_status: Optional[Callable[[Any], str]] = None,
) -> JobResult:
    """
    Poll a job until it reaches a terminal status.

    Args:
        fetch_status: Async function that fetches the current job status.
                     Should return a response object with status information.
        timeout: Maximum time to wait in seconds. Default: 300 (5 minutes).
        poll_interval: Time between polls in seconds. Default: 2.0.
        terminal_statuses: Tuple of statuses that indicate the job is done.
                          Default: ("completed", "failed").
        on_status: Optional callback called on each poll with (status, response).
        extract_job_id: Function to extract job_id from response.
                       Default: looks for job_id attribute or dict key.
        extract_status: Function to extract status from response.
                       Default: looks for status attribute or dict key.

    Returns:
        JobResult with the final job state.

    Raises:
        JobTimeoutError: If the job doesn't complete within the timeout.
        JobFailedError: If the job fails.

    Example:
        >>> async def get_status():
        ...     return await client.geofences.apps_geofences_api_get_upload_job_status(
        ...         job_id=job_id
        ...     )
        ...
        >>> result = await poll_job(get_status, timeout=120)
        >>> print(f"Created {result.created_count} geofences")
    """
    extract_job_id = extract_job_id or _default_extract_job_id
    extract_status = extract_status or _default_extract_status

    elapsed = 0.0
    last_status: Optional[str] = None
    last_response: Optional[Any] = None

    while elapsed < timeout:
        response = await fetch_status()
        last_response = response
        status = extract_status(response)
        last_status = status

        if on_status:
            on_status(status, response)

        if status in terminal_statuses:
            job_id = extract_job_id(response)
            return _build_job_result(job_id, status, response)

        await asyncio.sleep(poll_interval)
        elapsed += poll_interval

    # Timeout
    job_id = extract_job_id(last_response) if last_response else "unknown"
    raise JobTimeoutError(job_id, timeout, last_status)


def _default_extract_job_id(response: Any) -> str:
    """Extract job_id from response."""
    if hasattr(response, "job_id"):
        return str(response.job_id)
    if isinstance(response, dict):
        return str(response.get("job_id", "unknown"))
    return "unknown"


def _default_extract_status(response: Any) -> str:
    """Extract status from response."""
    if hasattr(response, "status"):
        return str(response.status)
    if isinstance(response, dict):
        return str(response.get("status", "unknown"))
    return "unknown"


def _build_job_result(job_id: str, status: str, response: Any) -> JobResult:
    """Build a JobResult from the response."""
    # Handle both object attributes and dict access
    def get_field(name: str, default: Any = None) -> Any:
        if hasattr(response, name):
            return getattr(response, name)
        if isinstance(response, dict):
            return response.get(name, default)
        return default

    # Check for failure
    if status == "failed":
        error_message = get_field("error_message")
        results = get_field("results")
        raise JobFailedError(job_id, error_message, results)

    return JobResult(
        job_id=job_id,
        status=status,
        created_count=get_field("created_count", 0),
        failed_count=get_field("failed_count", 0),
        total_features=get_field("total_features", 0),
        results=get_field("results"),
        duration=get_field("duration"),
        raw_response=response,
    )
