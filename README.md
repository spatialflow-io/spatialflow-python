# SpatialFlow Python SDK

The official Python SDK for [SpatialFlow](https://spatialflow.io) - a real-time geospatial automation platform.

## Installation

```bash
pip install spatialflow
```

## Quick Start

```python
import asyncio
from spatialflow import SpatialFlow, models

async def main():
    # Initialize with API key
    async with SpatialFlow(api_key="sf_xxx") as client:
        # List geofences
        response = await client.geofences.apps_geofences_api_list_geofences()
        for geofence in response.results:
            print(f"{geofence.name}: {geofence.id}")

        # Create a geofence
        geofence = await client.geofences.apps_geofences_api_create_geofence(
            models.CreateGeofenceRequest(
                name="My Region",
                geometry={
                    "type": "Polygon",
                    "coordinates": [[[-122.4, 37.8], [-122.4, 37.7], [-122.3, 37.7], [-122.3, 37.8], [-122.4, 37.8]]]
                }
            )
        )

asyncio.run(main())
```

## Authentication

### API Key (Recommended for server-side)

```python
client = SpatialFlow(api_key="sf_xxx")
```

### JWT Token (For client-side apps)

```python
client = SpatialFlow(access_token="eyJ...")
```

## Resources

- **Geofences** - Create and manage geofences
- **Workflows** - Automate location-based actions
- **Webhooks** - Receive real-time event notifications
- **Devices** - Track device locations

## Method Naming

API methods are auto-generated from the OpenAPI spec and follow the pattern:
`apps_{resource}_api_{operation}`. For example:

```python
# Geofences
client.geofences.apps_geofences_api_list_geofences()
client.geofences.apps_geofences_api_create_geofence(...)
client.geofences.apps_geofences_api_get_geofence(id=...)
client.geofences.apps_geofences_api_update_geofence(id=..., ...)
client.geofences.apps_geofences_api_delete_geofence(id=...)

# Workflows
client.workflows.apps_workflows_api_list_workflows()
client.workflows.apps_workflows_api_create_workflow(...)

# Webhooks
client.webhooks.apps_webhooks_api_list_webhooks()
client.webhooks.apps_webhooks_api_create_webhook(...)
```

Use your IDE's autocomplete to discover available methods, or see the
[API Reference](https://docs.spatialflow.io/sdk/python) for the full list.

## Webhook Verification

Verify incoming webhook signatures to ensure they're from SpatialFlow:

```python
from spatialflow import verify_webhook_signature, WebhookSignatureError

# In your webhook handler (e.g., FastAPI/Flask)
@app.post("/webhook")
async def handle_webhook(request):
    payload = await request.body()
    signature = request.headers.get("X-SF-Signature")

    try:
        event = verify_webhook_signature(
            payload=payload,
            signature=signature,
            secret=WEBHOOK_SECRET,
        )
        print(f"Event type: {event['type']}")
        return {"status": "ok"}
    except WebhookSignatureError as e:
        return {"error": str(e)}, 400
```

## Pagination

Use the async paginator to iterate through all results:

```python
from spatialflow import paginate

async def fetch_page(offset, limit):
    return await client.geofences.apps_geofences_api_list_geofences(
        offset=offset, limit=limit
    )

async for geofence in paginate(fetch_page):
    print(geofence.name)
```

## File Uploads

Upload geofence files (GeoJSON, KML, GPX) with automatic job polling:

```python
from spatialflow import upload_geofences

result = await upload_geofences(
    client,
    "boundaries.geojson",
    group_name="my-region",
    timeout=120,
    on_status=lambda status, _: print(f"Status: {status}"),
)

print(f"Created {result.created_count} geofences")
for geofence in result.created_geofences:
    print(f"  - {geofence['name']} ({geofence['id']})")
```

## Async Job Polling

For lower-level control over job polling:

```python
from spatialflow import poll_job, JobTimeoutError, JobFailedError

async def get_status():
    return await client.geofences.apps_geofences_api_get_upload_job_status(
        job_id=job_id
    )

try:
    result = await poll_job(
        get_status,
        timeout=120,
        poll_interval=2.0,
        on_status=lambda status, _: print(f"Status: {status}"),
    )
    print(f"Job completed: {result.created_count} created")
except JobTimeoutError as e:
    print(f"Job timed out after {e.timeout}s (last status: {e.last_status})")
except JobFailedError as e:
    print(f"Job failed: {e.error_message}")
```

## Models

Request/response models are available via the `models` namespace:

```python
from spatialflow import models

# Common models
models.CreateGeofenceRequest
models.GeofenceResponse
models.CreateWebhookRequest
models.WebhookResponse
models.WorkflowIn
models.WorkflowOut

# Explore all available models
print([m for m in dir(models) if not m.startswith('_')])
```

## Documentation

- [API Reference](https://docs.spatialflow.io/sdk/python)
- [Examples](./examples/)
- [Changelog](./CHANGELOG.md)

## Support

- GitHub Issues: https://github.com/spatialflow-io/spatialflow-python/issues
- Email: support@spatialflow.io

## License

MIT License - see [LICENSE](./LICENSE) for details.
