"""Resource wrappers run against the real generated client.

Only the HTTP layer is replaced, so the generated operations still validate their
arguments. A wrapper that forwards a parameter the endpoint doesn't accept fails here
the way it does against the API.
"""

import json
from types import SimpleNamespace
from urllib.parse import parse_qs, urlparse

import pytest

from spatialflow import SpatialFlow, paginate_webhooks, paginate_workflows
from spatialflow._generated.spatialflow_generated.models import (
    DeviceIn,
    LocationUpdateIn,
    UpdateDeviceIn,
    WorkflowImportSchema,
    WorkflowRetryPolicyUpdateSchema,
    WorkflowUpdate,
)
from spatialflow._generated.spatialflow_generated.models import TestWorkflowIn as WorkflowTestBody
from spatialflow._generated.spatialflow_generated.rest import RESTResponse


class _FakeHttpResponse:
    status = 200
    reason = "OK"
    headers = {"content-type": "application/json"}

    def __init__(self, body):
        self._body = json.dumps(body).encode()

    async def read(self):
        return self._body


async def _call_ignoring_response_errors(call):
    """Await a wrapper call whose canned response needn't deserialize.

    Argument validation runs before the request is sent, so a rejected call leaves
    `client.requests` empty and the test's assertion on it fails.
    """
    try:
        await call
    except Exception:  # noqa: BLE001
        pass


@pytest.fixture
async def client():
    sf = SpatialFlow(api_key="sf_test")
    sf.requests = []
    sf.responses = {}

    async def request(method, url, **kwargs):
        parsed = urlparse(url)
        sf.requests.append((method, parsed.path, parse_qs(parsed.query)))
        return RESTResponse(_FakeHttpResponse(sf.responses[parsed.path]))

    sf._api_client.rest_client.request = request
    yield sf
    await sf._api_client.rest_client.pool_manager.close()


async def test_devices_list_sends_only_supported_filters(client):
    client.responses["/api/v1/devices/"] = []

    assert await client.devices.list() == []
    await client.devices.list(is_active=True, group="trucks")

    assert client.requests[0][2] == {}
    assert client.requests[1][2] == {"is_active": ["true"], "group": ["trucks"]}


async def test_integrations_list_sends_only_supported_filters(client):
    client.responses["/api/v1/integrations/"] = []

    assert await client.integrations.list() == []
    await client.integrations.list(type="slack", is_active=True)

    assert client.requests[0][2] == {}
    assert client.requests[1][2] == {"type": ["slack"], "is_active": ["true"]}


async def test_storage_list_files_passes_the_file_type(client):
    client.responses["/api/v1/storage/list/geofences"] = {
        "files": [],
        "count": 0,
        "file_type": "geofences",
    }

    result = await client.storage.list_files("geofences")

    assert result.file_type == "geofences"
    assert client.requests[0][1] == "/api/v1/storage/list/geofences"


async def test_webhook_metrics_take_no_webhook_id(client):
    client.responses["/api/v1/webhooks/metrics"] = {"metrics": {}, "cloudwatch_dashboard": {}}

    result = await client.webhooks.get_metrics()

    assert result.metrics == {}
    assert client.requests[0][1] == "/api/v1/webhooks/metrics"


async def test_webhook_success_timeline_takes_no_webhook_id(client):
    client.responses["/api/v1/webhooks/success-timeline"] = {"timeline": []}

    await client.webhooks.get_success_timeline()

    assert client.requests[0][1] == "/api/v1/webhooks/success-timeline"


async def test_retry_dlq_addresses_the_entry(client):
    client.responses["/api/v1/webhooks/dlq/dlq-1/retry"] = {"success": True}

    await client.webhooks.retry_dlq("dlq-1")

    assert client.requests[0][:2] == ("POST", "/api/v1/webhooks/dlq/dlq-1/retry")


async def test_geofences_list_filters_by_tags(client):
    client.responses["/api/v1/geofences/"] = {"geofences": [], "count": 0, "total_count": 0}

    await client.geofences.list(tags=["depot"])

    assert client.requests[0][2]["tags"] == ["depot"]


async def test_workflow_update_sends_the_update_body(client):
    client.responses["/api/v1/workflows/wf-1"] = {}

    await _call_ignoring_response_errors(
        client.workflows.update("wf-1", WorkflowUpdate(name="Renamed"))
    )

    assert client.requests[0][:2] == ("PUT", "/api/v1/workflows/wf-1")


async def test_workflow_execute_sends_test_data(client):
    client.responses["/api/v1/workflows/wf-1/execute"] = {}

    await _call_ignoring_response_errors(client.workflows.execute("wf-1", {"speed": 5}))

    assert client.requests[0][:2] == ("POST", "/api/v1/workflows/wf-1/execute")


async def test_workflow_test_sends_the_test_body(client):
    client.responses["/api/v1/workflows/wf-1/test"] = {}

    await _call_ignoring_response_errors(
        client.workflows.test("wf-1", WorkflowTestBody(test_data={"speed": 5}))
    )

    assert client.requests[0][:2] == ("POST", "/api/v1/workflows/wf-1/test")


async def test_workflow_duplicate_sends_the_new_name(client):
    client.responses["/api/v1/workflows/wf-1/duplicate"] = {}

    await _call_ignoring_response_errors(client.workflows.duplicate("wf-1", "Copy"))

    assert client.requests[0][2] == {"name": ["Copy"]}


async def test_workflow_import_sends_the_schema(client):
    client.responses["/api/v1/workflows/import"] = {}

    await _call_ignoring_response_errors(
        client.workflows.import_workflow(
            WorkflowImportSchema(version="1.0", workflow={"name": "Imported"})
        )
    )

    assert client.requests[0][:2] == ("POST", "/api/v1/workflows/import")


async def test_workflow_retry_policy_update_sends_the_schema(client):
    client.responses["/api/v1/workflows/wf-1/retry-policy"] = {}

    await _call_ignoring_response_errors(
        client.workflows.update_retry_policy(
            "wf-1", WorkflowRetryPolicyUpdateSchema(workflow_id="wf-1")
        )
    )

    assert client.requests[0][:2] == ("PUT", "/api/v1/workflows/wf-1/retry-policy")


async def test_device_create_sends_the_device(client):
    client.responses["/api/v1/devices/"] = {}

    await _call_ignoring_response_errors(
        client.devices.create(DeviceIn(device_id="truck-1", name="Truck"))
    )

    assert client.requests[0][:2] == ("POST", "/api/v1/devices/")


async def test_device_update_sends_the_update_body(client):
    client.responses["/api/v1/devices/dev-1"] = {}

    await _call_ignoring_response_errors(
        client.devices.update("dev-1", UpdateDeviceIn(name="Renamed"))
    )

    assert client.requests[0][:2] == ("PUT", "/api/v1/devices/dev-1")


async def test_device_update_location_sends_the_fix(client):
    client.responses["/api/v1/devices/dev-1/location"] = {}

    await _call_ignoring_response_errors(
        client.devices.update_location("dev-1", LocationUpdateIn(latitude=1.0, longitude=2.0))
    )

    assert client.requests[0][:2] == ("POST", "/api/v1/devices/dev-1/location")


def _pages(field, total, per_page, make_page):
    async def fetch(offset, limit):
        return make_page(list(range(offset, min(offset + per_page, total)))[:limit])

    return fetch


async def test_paginate_workflows_reads_the_workflow_list_shape():
    fetch = _pages(
        "workflows",
        5,
        2,
        lambda items: SimpleNamespace(workflows=items, total=5, page=1, page_size=2),
    )

    paginator = paginate_workflows(fetch, limit=2)
    assert [w async for w in paginator] == [0, 1, 2, 3, 4]
    assert paginator.total_count == 5


async def test_paginate_webhooks_reads_the_webhook_list_shape():
    def page(items):
        return SimpleNamespace(
            webhooks=items,
            pagination={"total": 5, "limit": 2, "offset": items[0] if items else 0},
        )

    paginator = paginate_webhooks(_pages("webhooks", 5, 2, page), limit=2)

    assert [w async for w in paginator] == [0, 1, 2, 3, 4]
    assert paginator.total_count == 5


def test_helpers_without_a_paginated_list_are_gone():
    import spatialflow

    assert not hasattr(spatialflow, "paginate_users")
    assert not hasattr(spatialflow, "paginate_files")
    assert not hasattr(spatialflow.GeofencesResource, "list_by_group")
