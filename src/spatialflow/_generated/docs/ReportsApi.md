# spatialflow_generated.ReportsApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_devices_api_reports_report_attendance**](ReportsApi.md#apps_devices_api_reports_report_attendance) | **GET** /api/v1/reports/attendance | Shift attendance report
[**apps_devices_api_reports_report_detention**](ReportsApi.md#apps_devices_api_reports_report_detention) | **GET** /api/v1/reports/detention | Detention report — one row per facility visit with billable overage
[**apps_devices_api_reports_report_idle_stops**](ReportsApi.md#apps_devices_api_reports_report_idle_stops) | **GET** /api/v1/reports/idle-stops | Idle/stop summary report
[**apps_devices_api_reports_report_mileage**](ReportsApi.md#apps_devices_api_reports_report_mileage) | **GET** /api/v1/reports/mileage | Mileage summary report
[**apps_devices_api_reports_report_time_on_site**](ReportsApi.md#apps_devices_api_reports_report_time_on_site) | **GET** /api/v1/reports/time-on-site | Time-on-site / job-site report
[**apps_devices_api_reports_report_trips**](ReportsApi.md#apps_devices_api_reports_report_trips) | **GET** /api/v1/reports/trips | Trip history report


# **apps_devices_api_reports_report_attendance**
> ReportOut apps_devices_api_reports_report_attendance(start=start, end=end, device_id=device_id, group=group, format=format)

Shift attendance report

Per device per workspace-tz day: first shift start, last shift end, total on-shift seconds, shift count.  An active (open) session contributes an open interval clamped to \"now\".

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.report_out import ReportOut
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.ReportsApi(api_client)
    start = '2013-10-20' # date |  (optional)
    end = '2013-10-20' # date |  (optional)
    device_id = 'device_id_example' # str |  (optional)
    group = 'group_example' # str |  (optional)
    format = 'json' # str |  (optional) (default to 'json')

    try:
        # Shift attendance report
        api_response = await api_instance.apps_devices_api_reports_report_attendance(start=start, end=end, device_id=device_id, group=group, format=format)
        print("The response of ReportsApi->apps_devices_api_reports_report_attendance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->apps_devices_api_reports_report_attendance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**|  | [optional] 
 **end** | **date**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to &#39;json&#39;]

### Return type

[**ReportOut**](ReportOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_reports_report_detention**
> ReportOut apps_devices_api_reports_report_detention(start=start, end=end, device_id=device_id, group=group, free_time_minutes=free_time_minutes, rate_per_hour_cents=rate_per_hour_cents, format=format)

Detention report — one row per facility visit with billable overage

Per-VISIT detention rows: arrival, departure, time on site, billable overage.  A carrier bills detention when a truck waits at a shipper or receiver beyond the contracted free window. The claim needs a timestamped arrival and departure for a single visit, so this report emits exactly one row per visit — a visit that spans midnight, or several days, stays ONE row. (`/reports/time-on-site` buckets by (device, geofence, local day) instead, which is the right shape for job-site utilisation and the wrong shape for a claim.)  Visits come from GeofenceEvent entry/exit pairing (`_pair_geofence_visits`), which scans SYMMETRICALLY past both ends of the window: it seeds a visit that was already open when the window began, and resolves a visit that closes after the window ends. Both matter because a truck that arrives at 18:00 and leaves at 03:00 is one claim, and clipping either end understates the invoice. Dwell SignalEvents are deliberately NOT used here: a dwell signal has no departure event, and a claim without a departure timestamp is not payable.  NOT clipped to shift sessions. `report_time_on_site` applies `_clip_to_shifts` because a van parked at a job site after the crew clocks out is not working time. Detention is the exact opposite: a truck still sitting at a receiver after the driver's shift ends is precisely the time being billed, and clipping it would delete the claim. Do not \"consistency-fix\" this to match time-on-site.  A visit with no exit event splits into two distinct states. If a later re-entry proves the truck left, the row is `departure_inferred=true` (NOT open) with `seconds_on_site` bounded at that re-entry. Otherwise it is `is_open=true` with `seconds_on_site` measured to the earlier of now and the range end — never a silent whole-day figure. Both keep `exited_at=null`, because there is no departure event to cite. `summary.open_visit_count` therefore counts only trucks still on site; inferred departures are counted separately.  An open visit is only as good as the device behind it, and only while that device had CONTINUOUS contact. A silence longer than `settings.DETENTION_STALE_CONTACT_HOURS` anywhere inside the visit ends the evidence there and flags the row `contact_lost=true`. Contact comes from `DeviceSession.last_contact_at` (see `_contact_intervals`) — never from `Device.last_location_time`, which a reconnect refreshes, and never from DeviceLocation rows, which the distance filter skips for a parked truck. Those rows are counted and priced in their own bucket (`contact_lost_visit_count` / `contact_lost_unresolved_cents`) and are excluded from `open_visit_count` and from the owed total.  A visit that outlives its shift therefore stops being evidenced once the shift's telemetry does. That is not a clip to shift windows — the dwell keeps running and the money is still reported — but the platform cannot claim a truck was on site during hours it was not permitted to hear from the device (the device location routes reject off-shift fixes), so that portion sits in the unresolved bucket with its floor amount rather than in the claim total.  Money is integer cents end to end. `over_free_time_seconds` is `max(0, seconds_on_site - free_time_minutes * 60)`; `amount_owed_cents` applies `rate_per_hour_cents` to it under the rounding rule in `_detention_amount_cents`. The default rate of 0 yields 0 owed, so an unpriced report shows no dollar figure rather than a fabricated one.  Evidenced money and unresolved money never mix. `summary.total_amount_owed_cents` and `summary.total_over_free_time_seconds` cover evidenced and LIVE open visits only. The two excluded magnitudes point in OPPOSITE directions and must not be described alike: `inferred_max_additional_cents` is a CEILING (the truck may have left right after arriving), while `contact_lost_unresolved_cents` is a FLOOR (the vehicle was there at least that long and may have stayed far longer — the stop is unresolved, not cheap). Per row the split is `amount_owed_cents` versus `evidenced_amount_owed_cents` (0 in both cases), so a CSV export can be summed without silently billing a guess.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.report_out import ReportOut
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.ReportsApi(api_client)
    start = '2013-10-20' # date |  (optional)
    end = '2013-10-20' # date |  (optional)
    device_id = 'device_id_example' # str |  (optional)
    group = 'group_example' # str |  (optional)
    free_time_minutes = 120 # int |  (optional) (default to 120)
    rate_per_hour_cents = 0 # int |  (optional) (default to 0)
    format = 'json' # str |  (optional) (default to 'json')

    try:
        # Detention report — one row per facility visit with billable overage
        api_response = await api_instance.apps_devices_api_reports_report_detention(start=start, end=end, device_id=device_id, group=group, free_time_minutes=free_time_minutes, rate_per_hour_cents=rate_per_hour_cents, format=format)
        print("The response of ReportsApi->apps_devices_api_reports_report_detention:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->apps_devices_api_reports_report_detention: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**|  | [optional] 
 **end** | **date**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **free_time_minutes** | **int**|  | [optional] [default to 120]
 **rate_per_hour_cents** | **int**|  | [optional] [default to 0]
 **format** | **str**|  | [optional] [default to &#39;json&#39;]

### Return type

[**ReportOut**](ReportOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_reports_report_idle_stops**
> ReportOut apps_devices_api_reports_report_idle_stops(start=start, end=end, device_id=device_id, group=group, threshold_minutes=threshold_minutes, format=format)

Idle/stop summary report

Idle/stop rows derived from non-heartbeat DeviceLocation runs per session.  A stop = a maximal run of points within ``STOP_RADIUS_METERS`` (50 m) of the run anchor whose span >= ``threshold_minutes`` (default 5). Pure-Python haversine over fetched points — no raw geometry SQL.  Retention caveat: stops are only derivable within ``location_retention_days`` (~90d) before raw DeviceLocation is cleaned.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.report_out import ReportOut
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.ReportsApi(api_client)
    start = '2013-10-20' # date |  (optional)
    end = '2013-10-20' # date |  (optional)
    device_id = 'device_id_example' # str |  (optional)
    group = 'group_example' # str |  (optional)
    threshold_minutes = 5 # int |  (optional) (default to 5)
    format = 'json' # str |  (optional) (default to 'json')

    try:
        # Idle/stop summary report
        api_response = await api_instance.apps_devices_api_reports_report_idle_stops(start=start, end=end, device_id=device_id, group=group, threshold_minutes=threshold_minutes, format=format)
        print("The response of ReportsApi->apps_devices_api_reports_report_idle_stops:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->apps_devices_api_reports_report_idle_stops: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**|  | [optional] 
 **end** | **date**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **threshold_minutes** | **int**|  | [optional] [default to 5]
 **format** | **str**|  | [optional] [default to &#39;json&#39;]

### Return type

[**ReportOut**](ReportOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_reports_report_mileage**
> ReportOut apps_devices_api_reports_report_mileage(start=start, end=end, device_id=device_id, group=group, format=format)

Mileage summary report

Per-device mileage = ``Sum(DeviceSession.distance_meters)`` over the range.  Excludes active sessions (``distance_meters`` is null while a shift is active), matching the device-list behavior. Only devices with qualifying sessions appear as rows.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.report_out import ReportOut
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.ReportsApi(api_client)
    start = '2013-10-20' # date |  (optional)
    end = '2013-10-20' # date |  (optional)
    device_id = 'device_id_example' # str |  (optional)
    group = 'group_example' # str |  (optional)
    format = 'json' # str |  (optional) (default to 'json')

    try:
        # Mileage summary report
        api_response = await api_instance.apps_devices_api_reports_report_mileage(start=start, end=end, device_id=device_id, group=group, format=format)
        print("The response of ReportsApi->apps_devices_api_reports_report_mileage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->apps_devices_api_reports_report_mileage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**|  | [optional] 
 **end** | **date**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to &#39;json&#39;]

### Return type

[**ReportOut**](ReportOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_reports_report_time_on_site**
> ReportOut apps_devices_api_reports_report_time_on_site(start=start, end=end, device_id=device_id, group=group, format=format)

Time-on-site / job-site report

Time on each job-site geofence per device per workspace-tz day.  Derived from ``GeofenceEvent`` entry/exit pairing (event_type \"entry\"/\"exit\", NOT \"enter\"). Each entry pairs with the NEXT exit per (device, geofence); an entry still open at range end clamps its exit to ``range_end`` (open interval, not dropped). SignalEvent ``signal_type=\"dwell\"`` enriches the totals where entry/exit pairing is incomplete.  Precedence: entry/exit-derived seconds are PRIMARY. A dwell signal supplements a (device, geofence, day) bucket only when no entry/exit pairing produced a visit there (so a workflow-only dwell still surfaces job-site time).  `visit_count` counts visits that STARTED on the row's local day, so a row for a continuation day carries seconds with a zero count; `is_continuation` flags those rows so nothing can render \"a full day on site, zero visits\". For per-visit arrival/departure timestamps and billable overage, use `/reports/detention`.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.report_out import ReportOut
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.ReportsApi(api_client)
    start = '2013-10-20' # date |  (optional)
    end = '2013-10-20' # date |  (optional)
    device_id = 'device_id_example' # str |  (optional)
    group = 'group_example' # str |  (optional)
    format = 'json' # str |  (optional) (default to 'json')

    try:
        # Time-on-site / job-site report
        api_response = await api_instance.apps_devices_api_reports_report_time_on_site(start=start, end=end, device_id=device_id, group=group, format=format)
        print("The response of ReportsApi->apps_devices_api_reports_report_time_on_site:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->apps_devices_api_reports_report_time_on_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**|  | [optional] 
 **end** | **date**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to &#39;json&#39;]

### Return type

[**ReportOut**](ReportOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_reports_report_trips**
> ReportOut apps_devices_api_reports_report_trips(start=start, end=end, device_id=device_id, group=group, format=format)

Trip history report

Trip-history rows for completed/active trips in range, identity-enriched.  ``stop_count`` is the count of derived stops (``_derive_stops``) over each trip's ``session`` window; a trip with no session keeps ``stop_count = 0``. Note the per-trip location fetch is N+1-over-trips, which is acceptable for a fleet report bounded by MAX_REPORT_ROWS and the date range.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.report_out import ReportOut
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.ReportsApi(api_client)
    start = '2013-10-20' # date |  (optional)
    end = '2013-10-20' # date |  (optional)
    device_id = 'device_id_example' # str |  (optional)
    group = 'group_example' # str |  (optional)
    format = 'json' # str |  (optional) (default to 'json')

    try:
        # Trip history report
        api_response = await api_instance.apps_devices_api_reports_report_trips(start=start, end=end, device_id=device_id, group=group, format=format)
        print("The response of ReportsApi->apps_devices_api_reports_report_trips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->apps_devices_api_reports_report_trips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **date**|  | [optional] 
 **end** | **date**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **format** | **str**|  | [optional] [default to &#39;json&#39;]

### Return type

[**ReportOut**](ReportOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

