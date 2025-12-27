# Changelog

All notable changes to the SpatialFlow Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-12-26

### Added

- **Workflow activation**: `client.workflows.activate(workflow_id)` - Activate draft workflows for production use
  - Idempotent: returns success if workflow is already active
  - Validates workflow has trigger and steps before activation
  - Rate limited: 1000 requests/hour

### Fixed

- **Integrations API key auth**: Integrations API now accepts API key authentication (was JWT-only)
  - Requires `integrations:read` permission for list/get endpoints
  - Requires `integrations:write` permission for create/update/delete/test endpoints
  - Fixes: GitHub issue #114

- **Location ingest JWT auth**: Location ingest API now accepts JWT authentication (was API-key-only)
  - Both JWT and API key auth now work for location ingestion
  - Fixes: GitHub issue #115

### Technical Details

- Regenerated from OpenAPI spec using openapi-generator-cli 7.19.0
- Generated package now installed as `spatialflow_generated` in virtualenv
- OpenAPI spec hash: ce5ef5f82f7f17ebc5d628a612b84d1d39159c330c8362c4680be7bbdda50327

## [0.1.0] - 2025-12-04

### Added

- Initial alpha release
- **Authentication**: API key and JWT token support
- **Client**: `SpatialFlow` async client with resource accessors
- **Resources**: Full CRUD for geofences, workflows, webhooks, devices
- **Pagination**: `paginate()` async iterator for paginated endpoints
- **Webhook verification**: `verify_webhook_signature()` with HMAC-SHA256
- **Job polling**: `poll_job()` for async job status tracking
- **File uploads**: `upload_geofences()` for GeoJSON/KML/GPX imports
- **Typed exceptions**: `AuthenticationError`, `NotFoundError`, `ValidationError`, etc.
- **Models**: Re-exported Pydantic models from generated code

### Technical Details

- Generated from OpenAPI spec using openapi-generator-cli 7.10.0
- Python generator with `library=asyncio` for native async/await
- Requires Python 3.9+
- Dependencies: aiohttp, pydantic v2, python-dateutil
