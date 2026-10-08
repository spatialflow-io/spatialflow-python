"""The version the SDK reports must match the package metadata."""

import re
from pathlib import Path

import spatialflow
from spatialflow import SpatialFlow
from spatialflow.client import VERSION

PYPROJECT = Path(__file__).resolve().parents[1] / "pyproject.toml"


def _package_version() -> str:
    match = re.search(r'^version = "([^"]+)"', PYPROJECT.read_text(), re.MULTILINE)
    assert match, "version not found in pyproject.toml"
    return match.group(1)


def test_reported_versions_match_pyproject():
    assert spatialflow.__version__ == _package_version()
    assert VERSION == _package_version()


async def test_user_agent_uses_package_version():
    async with SpatialFlow(api_key="sf_test") as client:  # pragma: allowlist secret
        assert client._api_client.user_agent == f"spatialflow-python/{_package_version()}"
