# Changelog

All notable changes to the SpatialFlow Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-10-08

**Breaking changes.** `paginate_users`, `paginate_files`, `GeofencesResource.list_by_group` and the account onboarding wrappers are removed, and several list and request-body wrappers take different arguments. See Removed and Fixed below.

### Added

- `client.devices`: `start_shift`, `pause_shift`, `resume_shift`, `end_shift`,
  `list_sessions`, `get_session`, `get_session_locations`, `list_session_notes`,
  `add_session_note`.
- `client.geofences`: `list_groups`, `list_group_geofences`, `test_group_point`,
  `assign_to_group`.
- `client.workspaces`: `list_members`, `update_member_role`, `remove_member`,
  `list_invitations`, `create_invitation`, `resend_invitation`,
  `resend_missing_invitations`, `extend_invitation`, `cancel_invitation`.
- `verify_workflow_signature` verifies a workflow Webhook action delivery: `X-SpatialFlow-Signature` (`sha256=<hex>` HMAC-SHA256 over `<timestamp>.<raw body>`) and `X-SpatialFlow-Timestamp`, with a default 300 second tolerance in both directions. A body that isn't JSON is returned as text. `verify_webhook_signature` is unchanged.

### Fixed

- Exceptions raised from generated API calls now carry the server's `detail` and
  `error_code` for every status class, not just the generic case. A plan limit
  returns a `PermissionError` with `error_code == "WORKFLOW_LIMIT_REACHED"`
  instead of `detail=None`.
- `SpatialFlow.close()` and `async with SpatialFlow(...)` now close the aiohttp
  session, so Python no longer prints `Unclosed client session` on exit.
- `client.storage.delete_file(file_id=...)` now deletes an uploaded file. The
  endpoint takes the `file_id` an upload returned; before, it could not find
  uploaded files and the call failed. It returns `None` on success.
- **List and metrics wrappers**: these forwarded parameters the endpoints reject, so they failed validation before any request was sent.
  - `client.devices.list()` takes `is_active`, `include_geofences` and `group` instead of `limit` and `offset`.
  - `client.integrations.list()` takes `type`, `is_active`, `is_verified` and `search` instead of `limit`, `offset` and `integration_type`.
  - `client.storage.list_files(file_type)` takes the file type the endpoint requires, and no `limit` or `offset`.
  - `client.geofences.list()` no longer takes `group_id`; use `list_group_geofences(group_id)` for the geofences in one group.
  - `client.webhooks.get_metrics()` and `get_success_timeline()` no longer take `webhook_id`: the metrics endpoint is platform-wide and admin-only, and the timeline covers the whole workspace.
  - Request-body wrappers sent argument names the generated client doesn't have. `workflows.update` takes a `WorkflowUpdate`, `workflows.test` a `TestWorkflowIn`, `workflows.duplicate` the copy's `name` instead of a `request`, `workflows.execute` an optional dict sent as `test_data` (the endpoint does not accept a payload yet), and `devices.update` an `UpdateDeviceIn`. `workflows.import_workflow`, `workflows.update_retry_policy`, `devices.create` and `devices.update_location` keep their signatures.
  - `client.webhooks.retry_dlq()` sends the entry ID as the endpoint's `dlq_id`.
- **Paginators**: `paginate_workflows` reads `total` and `paginate_webhooks` reads `pagination.total`, instead of a `count` field those responses don't have. `paginate_geofences` reports `total_count` as its total.
- **Webhook signature verification**: `verify_webhook_signature` now matches the platform, which signs the raw request body with HMAC-SHA256 and sends it as `X-SF-Signature: sha256=<hex>`. The previous implementation expected a Stripe-style `t=<timestamp>,v1=<sig>` header and rejected every real webhook.
  - Malformed (non-hex or non-ASCII) signatures now raise `WebhookSignatureError` instead of a `TypeError`.
  - The `tolerance` parameter is retained but deprecated and ignored (the signature carries no timestamp; to guard against replays, verify the signature and then deduplicate on the signed payload `id`, because the `X-Idempotency-Key` and `X-SF-Event-ID` headers are not signed).
  - Docs corrected to read the backend `event` key (`event["event"]`).

### Removed

- Removed the account wrapper methods `get_onboarding_progress`,
  `update_onboarding_progress`, and `dismiss_onboarding`. Their endpoints were
  removed from the platform; the generated Python and Node clients already no
  longer expose them. No generated files were changed.
- `GeofencesResource.list_by_group`, which always failed; `list_group_geofences` covers it.
- `paginate_users` and `paginate_files`. The SDK has no user list call, and the storage list isn't paginated, so `paginate_files` never stopped.

## [1.1.0] - 2026-04-05

### Changed

- The generated API client is rebuilt from OpenAPI spec v1.1.0. Schemas that were untyped objects are now typed, including geofence geometry, the login response's user, the created API key, workflow import, retry policy, integration configs and simulation details.
- Every operation's generated types include the standard 4xx error responses.
- `VERSION` and the `User-Agent` header report `1.1.0` (they reported `0.2.0` before).

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
