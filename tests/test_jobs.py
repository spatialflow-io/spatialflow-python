"""Tests for async job polling helpers."""

import pytest

from spatialflow import poll_job, JobResult, JobTimeoutError, JobFailedError


class TestPollJob:
    """Test the poll_job async function."""

    async def test_poll_job_completes_immediately(self):
        """Test polling a job that completes on first check."""
        async def fetch_status():
            return {
                "job_id": "test-123",
                "status": "completed",
                "created_count": 5,
                "failed_count": 0,
                "total_features": 5,
                "results": {"created_geofences": [{"id": "1", "name": "Test"}]},
                "duration": 1.5,
            }

        result = await poll_job(fetch_status, timeout=10, poll_interval=0.1)

        assert result.job_id == "test-123"
        assert result.status == "completed"
        assert result.created_count == 5
        assert result.failed_count == 0
        assert result.duration == 1.5
        assert len(result.created_geofences) == 1

    async def test_poll_job_waits_for_completion(self):
        """Test polling a job that takes multiple polls to complete."""
        poll_count = 0

        async def fetch_status():
            nonlocal poll_count
            poll_count += 1
            if poll_count < 3:
                return {"job_id": "test-456", "status": "processing"}
            return {
                "job_id": "test-456",
                "status": "completed",
                "created_count": 10,
                "failed_count": 0,
                "total_features": 10,
                "results": {},
            }

        result = await poll_job(fetch_status, timeout=10, poll_interval=0.01)

        assert result.status == "completed"
        assert poll_count == 3

    async def test_poll_job_timeout(self):
        """Test that poll_job raises JobTimeoutError on timeout."""
        async def fetch_status():
            return {"job_id": "slow-job", "status": "processing"}

        with pytest.raises(JobTimeoutError) as exc_info:
            await poll_job(fetch_status, timeout=0.05, poll_interval=0.02)

        assert exc_info.value.job_id == "slow-job"
        assert exc_info.value.last_status == "processing"

    async def test_poll_job_failure(self):
        """Test that poll_job raises JobFailedError on failure."""
        async def fetch_status():
            return {
                "job_id": "failed-job",
                "status": "failed",
                "error_message": "Invalid file format",
                "results": {"errors": [{"message": "Parse error"}]},
            }

        with pytest.raises(JobFailedError) as exc_info:
            await poll_job(fetch_status, timeout=10, poll_interval=0.1)

        assert exc_info.value.job_id == "failed-job"
        assert "Invalid file format" in exc_info.value.error_message

    async def test_poll_job_status_callback(self):
        """Test that on_status callback is called on each poll."""
        statuses = []
        poll_count = 0

        async def fetch_status():
            nonlocal poll_count
            poll_count += 1
            if poll_count < 3:
                return {"job_id": "cb-test", "status": "processing"}
            return {"job_id": "cb-test", "status": "completed", "created_count": 0}

        def on_status(status, response):
            statuses.append(status)

        await poll_job(
            fetch_status,
            timeout=10,
            poll_interval=0.01,
            on_status=on_status,
        )

        assert statuses == ["processing", "processing", "completed"]

    async def test_poll_job_custom_terminal_statuses(self):
        """Test custom terminal statuses."""
        async def fetch_status():
            return {"job_id": "custom", "status": "cancelled"}

        # "cancelled" is not a default terminal status, should timeout
        with pytest.raises(JobTimeoutError):
            await poll_job(
                fetch_status,
                timeout=0.05,
                poll_interval=0.02,
            )

        # With custom terminal statuses, should complete
        result = await poll_job(
            fetch_status,
            timeout=10,
            poll_interval=0.1,
            terminal_statuses=("completed", "failed", "cancelled"),
        )
        assert result.status == "cancelled"

    async def test_poll_job_extracts_from_object_response(self):
        """Test extraction from object with attributes."""

        class MockResponse:
            job_id = "obj-123"
            status = "completed"
            created_count = 3
            failed_count = 1
            total_features = 4
            results = {}
            duration = 2.5

        async def fetch_status():
            return MockResponse()

        result = await poll_job(fetch_status, timeout=10, poll_interval=0.1)

        assert result.job_id == "obj-123"
        assert result.created_count == 3


class TestJobResult:
    """Test the JobResult class."""

    def test_job_result_created_geofences(self):
        """Test created_geofences property."""
        result = JobResult(
            job_id="test",
            status="completed",
            results={"created_geofences": [{"id": "1"}, {"id": "2"}]},
        )

        assert len(result.created_geofences) == 2

    def test_job_result_errors(self):
        """Test errors property."""
        result = JobResult(
            job_id="test",
            status="completed",
            results={"errors": [{"message": "Error 1"}]},
        )

        assert len(result.errors) == 1

    def test_job_result_warnings(self):
        """Test warnings property."""
        result = JobResult(
            job_id="test",
            status="completed",
            results={"warnings": ["Warning 1", "Warning 2"]},
        )

        assert len(result.warnings) == 2

    def test_job_result_repr(self):
        """Test JobResult string representation."""
        result = JobResult(
            job_id="test-repr",
            status="completed",
            created_count=5,
            failed_count=2,
        )

        repr_str = repr(result)
        assert "test-repr" in repr_str
        assert "completed" in repr_str
        assert "5" in repr_str
        assert "2" in repr_str


class TestJobTimeoutError:
    """Test the JobTimeoutError exception."""

    def test_job_timeout_error_message(self):
        """Test error message format."""
        error = JobTimeoutError("job-123", 60.0, "processing")

        assert "job-123" in str(error)
        assert "60" in str(error)
        assert "processing" in str(error)

    def test_job_timeout_error_without_status(self):
        """Test error message without last status."""
        error = JobTimeoutError("job-456", 30.0)

        assert "job-456" in str(error)
        assert "30" in str(error)


class TestJobFailedError:
    """Test the JobFailedError exception."""

    def test_job_failed_error_with_message(self):
        """Test error with error message."""
        error = JobFailedError("job-789", "Parse error")

        assert "job-789" in str(error)
        assert "Parse error" in str(error)

    def test_job_failed_error_with_results(self):
        """Test error includes results."""
        results = {"errors": [{"line": 1, "message": "Invalid"}]}
        error = JobFailedError("job-abc", "Validation failed", results)

        assert error.results == results
