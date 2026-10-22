# Changelog

All notable changes to the SpatialFlow Python SDK will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.2.0] - 2026-10-22

### Added

- `POST /api/v1/devices/batch-update` (spec v1.62.0): each point in `locations` (`LocationUpdateIn`) takes an optional `fix_id`, a UUID string naming the fix. A later point with the same `fix_id` for the same device is answered with status `duplicate` and is not stored, evaluated or counted again, even when its other fields differ. The match holds for at least 48 hours after the first copy is processed. A `fix_id` that is not a UUID rejects only its own point, with error code `INVALID_FIX_ID`. `POST /api/v1/devices/{device_id}/location` ignores the field.

## [3.1.0] - 2026-10-21

### Added

- `GET /api/v1/workflow-runs-to-retry` (spec v1.60.0): the live workflows in the workspace with failed runs that Retry failed runs could queue, by name, as `apps_operations_api_list_workflow_runs_to_retry` returning `WorkflowRunsToRetryListOut`: `results` of `WorkflowRunsToRetryOut` (`workflow_id`, `workflow_name`, `retryable_count`, `capped`), `next_cursor` and `has_more`. Pass `cursor` (and optionally `limit`) to continue, or `incident_id` to page through the workflows one incident is about with live counts. Each count looks at a bounded number of the workflow's failed runs, and `capped` marks a lower bound. Owner or manager only; other roles get 403.

### Changed

- `GET /api/v1/devices/dashboard-stats/timeline` (spec v1.57.0): `in_geofence_count` on each bucket (`TimelineBucketOut`) and on `previous` (`TimelinePreviousOut`) can now be null. A bucket that ends before the workspace's location retention cutoff reads null instead of 0, and `previous` reads null when any of its buckets does. Each bucket counts the devices whose position at the bucket's end is inside an active geofence, the same test as the live `in_geofence_count` on `/dashboard-stats`.
- `GET /api/v1/devices/dashboard-stats/timeline` (spec v1.58.0): `live_count` and `offline_stale_count` on each bucket (`TimelineBucketOut`) and on `previous` (`TimelinePreviousOut`) can now be null, like `in_geofence_count`. Both read null when the bucket's live window, the two minutes before its end, starts before the workspace's location retention cutoff, since retention may have deleted the fixes they count, and `previous` reads null when any of its buckets does. Other buckets return the same values as before.

### Deprecated

- `POST /api/v1/auth/oauth/{provider}/link` (spec v1.59.0). It no longer starts a link: every call returns 400, and it never returned the provider's authorization URL, so no call could have completed a link. The generated `AuthenticationApi` keeps `apps_authentication_oauth_api_link_oauth_account` and `OAuthLinkResponse` with the same signature until the next major SDK release removes them. `GET /api/v1/auth/oauth/user/linked-accounts` and `DELETE /api/v1/auth/oauth/{provider}/disconnect` are unchanged.

### Removed

- `GET /api/v1/admin/users/stats` (spec v1.61.0): a platform-admin route that always returned an empty list. No SDK exposed it, so no SDK method is affected.

## [3.0.0] - 2026-10-19

**Breaking changes.** The GPX simulator endpoints and the `gpx_simulator` API are gone from the generated client.

### Added

- Geofence group workflow lookup (spec v1.55.0). `GET /api/v1/geofences/groups/workflows` takes repeated `group_id` and an optional `destination_name` and returns the active workflows whose geofence trigger expands any of those groups (`GroupWorkflowsOut`; each `GroupWorkflowItemOut` has `id`, `name`, the matched `group_ids` and the trigger's own `geofence_ids`), plus `destination_group_id`, the id that name resolves to even when the group has no active members. It needs the `workflows:read` and `geofences:read` permissions.
- Failed workflow runs can be retried (spec v1.53.0). `POST /api/v1/workflows/{workflow_id}/runs/{run_id}/retry` retries one run (`RunRetryOut`). `GET /api/v1/workflows/{workflow_id}/retry-failed-runs` counts the runs a batch would retry (`RetryFailedRunsPreviewOut`, whose `blocked_reason` says why when the workflow itself prevents retries, such as test mode), and `POST` to it queues up to `batch_limit` of them, oldest first (`RetryFailedRunsOut`; `not_queued` lists runs whose retries couldn't be queued). Both POSTs return 409 for a run or batch that can't be retried and 503 when nothing could be queued. Run history executions (`ExecutionOut`) carry optional `retry_of`, `retried_by`, `retryable` and `retry_blocked_reason`.
- Run history actions (`ActionDeliveryOut`) carry two optional properties for a failed webhook delivery: `response_status_code`, the receiver's HTTP status, and `response_excerpt`, the start of its reply as plain text with echoed secrets withheld.
- The Google and Apple mobile token exchanges (`GoogleTokenExchangeResponse`, `AppleTokenExchangeResponse`, spec v1.56.0) carry two optional properties when the request accepted an invitation: `already_member`, true when the account already belonged to the invited workspace, and `role`, the role it holds there. Accepting an invitation never changes an existing member's role.

### Changed

- Creating an integration (`CreateIntegrationSchema`) no longer requires `name`. Leave it out or send it blank, and the API names the integration after its type, numbered when the name is taken ("Webhook", "Webhook 2", ...). The create returns 409 with `error_code` `INTEGRATION_NAME_BUSY` when concurrent creates in the workspace took every name it tried; retry it.

### Fixed

- `poll_job` and `upload_geofences` treat `timeout` as a wall-clock deadline. Time spent in status calls counts, the wait between polls is cut short at the deadline, and a status call still running then is cancelled and raises `JobTimeoutError`. A timeout raised by the status call itself still propagates.
- `workflows.execute` sends the payload as a JSON request body (`{"test_data": ...}`). The endpoint previously read `test_data` from the query string, so a payload failed validation. The server now stores it as the execution's trigger data.

### Removed

- The GPX simulator endpoints (spec v1.54.0): `/api/v1/gpx/routes`, `/api/v1/gpx/routes/upload`, `/api/v1/gpx/routes/{route_id}`, `/api/v1/gpx/routes/{route_id}/playback` and `/api/v1/gpx/playbacks` with its get, pause, resume and cancel routes, along with the `GPXRouteOut`, `GPXPlaybackOut` and `StartPlaybackRequest` models. The feature was retired and the service held no routes or playbacks. The generated client no longer has the `gpx_simulator` API. Geofence uploads still accept GPX files.

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
