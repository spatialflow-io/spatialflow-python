# Changelog

All notable changes to the SpatialFlow Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
