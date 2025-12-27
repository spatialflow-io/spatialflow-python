# SpatialFlow Python SDK

The official Python SDK for [SpatialFlow](https://spatialflow.io) - a real-time geospatial automation platform.

## Installation

```bash
pip install spatialflow
```

### Development Installation

```bash
cd sdks/python
pip install -e ".[dev]"
```

## Quick Start

```python
import asyncio
from spatialflow import SpatialFlow

async def main():
    async with SpatialFlow(api_key="sf_xxx") as client:
        # List geofences
        response = await client.geofences.list()
        for geofence in response.geofences:
            print(f"{geofence.name}: {geofence.id}")

        # Get workspace usage
        usage = await client.workspaces.get_usage()
        print(f"Event units: {usage.event_units}")

asyncio.run(main())
```

## Supported Resources

| Resource | Methods | Description |
|----------|---------|-------------|
| **Geofences** | CRUD, upload, bulk | Manage geofence boundaries |
| **Workflows** | CRUD, execute, monitor, versioning | Automation workflows |
| **Webhooks** | CRUD, deliveries, DLQ, metrics | Webhook endpoints and delivery tracking |
| **Devices** | CRUD, location updates | Device management |
| **Account** | profile, API keys, metrics, onboarding | User account management |
| **Workspaces** | get, update, usage | Workspace settings and usage metrics |
| **Locations** | ingest, batch, stats | Public location ingestion API |
| **Integrations** | CRUD, test | Third-party service connections |
| **Storage** | presigned URLs, files | File upload and management |

## Features

- Fully async with `aiohttp`
- Automatic retry with exponential backoff
- Pagination helpers
- Webhook signature verification
- Workflow builders for common patterns
- File upload with streaming (memory efficient)

## Error Handling

```python
from spatialflow import SpatialFlow, NotFoundError, ValidationError

async with SpatialFlow(api_key="sf_xxx") as client:
    try:
        geofence = await client.geofences.get("invalid-id")
    except NotFoundError as e:
        print(f"Geofence not found: {e}")
    except ValidationError as e:
        print(f"Invalid request: {e.errors}")
```

## Raw API Access

For advanced use cases, access the generated API clients directly:

```python
async with SpatialFlow(api_key="sf_xxx") as client:
    # Use raw generated API
    response = await client.raw.geofences.apps_geofences_api_list_geofences()
```

Available via `client.raw`:
- `geofences`, `workflows`, `webhooks`, `devices`, `storage`, `locations`, `integrations`, `workspaces`, `account` (also wrapped)
- `authentication`, `admin`, `billing`, `subscriptions`, `tiles` (raw only)

> **Alpha Notice:** This SDK is in alpha (v0.1.0). Some generated APIs (email, system, gpx_simulator,
> public, default, e2e_test) are not yet exposed. Use the generated client directly for those.

## Documentation

Full documentation: [docs.spatialflow.io/sdks/python](https://docs.spatialflow.io/sdks/python)

## License

MIT
