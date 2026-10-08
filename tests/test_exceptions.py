"""Tests for translating generated API exceptions and closing the client."""

import json

import pytest

from spatialflow import SpatialFlow
from spatialflow._generated.spatialflow_generated.exceptions import (
    ApiException,
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    ServiceException,
    UnauthorizedException,
)
from spatialflow.exceptions import (
    AuthenticationError,
    NotFoundError,
    PermissionError,
    ServerError,
    SpatialFlowError,
    ValidationError,
    translate_exception,
)

LIMIT_BODY = {
    "detail": "Workflow limit reached (10). Upgrade your plan to create more workflows.",
    "error_code": "WORKFLOW_LIMIT_REACHED",
}


@pytest.mark.parametrize(
    ("exc_class", "status", "expected"),
    [
        (UnauthorizedException, 401, AuthenticationError),
        (ForbiddenException, 403, PermissionError),
        (NotFoundException, 404, NotFoundError),
        (BadRequestException, 400, ValidationError),
        (ServiceException, 503, ServerError),
        (ApiException, 409, SpatialFlowError),
        (ApiException, 429, SpatialFlowError),
    ],
)
def test_translated_exception_keeps_detail_and_error_code(exc_class, status, expected):
    exc = exc_class(status=status, reason="Reason", body=json.dumps(LIMIT_BODY))

    translated = translate_exception(exc)

    assert isinstance(translated, expected)
    assert translated.status_code == status
    assert translated.detail == LIMIT_BODY["detail"]
    assert translated.error_code == "WORKFLOW_LIMIT_REACHED"


def test_translated_exception_accepts_bytes_body():
    exc = ForbiddenException(
        status=403, reason="Forbidden", body=json.dumps(LIMIT_BODY).encode()
    )

    assert translate_exception(exc).error_code == "WORKFLOW_LIMIT_REACHED"


def test_validation_list_detail_is_kept_as_errors():
    errors = [{"loc": ["body", "name"], "msg": "field required"}]
    exc = BadRequestException(
        status=400, reason="Bad Request", body=json.dumps({"detail": errors})
    )

    translated = translate_exception(exc)

    assert isinstance(translated, ValidationError)
    assert translated.errors == errors
    assert "field required" in translated.detail


@pytest.mark.parametrize(
    "body", [None, "", "<html>Bad gateway</html>", "[1, 2]", '"text"']
)
def test_translated_exception_tolerates_unusable_bodies(body):
    exc = ServiceException(status=502, reason="Bad Gateway", body=body)

    translated = translate_exception(exc)

    assert isinstance(translated, ServerError)
    assert translated.status_code == 502
    assert translated.detail is None
    assert translated.error_code is None


async def test_async_with_closes_the_aiohttp_session():
    async with SpatialFlow(api_key="sf_test") as client:  # pragma: allowlist secret
        session = client._api_client.rest_client.pool_manager
        assert not session.closed

    assert session.closed


async def test_close_is_idempotent():
    client = SpatialFlow(api_key="sf_test")  # pragma: allowlist secret
    session = client._api_client.rest_client.pool_manager

    await client.close()
    await client.close()

    assert session.closed
