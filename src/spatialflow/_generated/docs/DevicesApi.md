# spatialflow_generated.DevicesApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_devices_api_activate_device**](DevicesApi.md#apps_devices_api_activate_device) | **POST** /api/v1/devices/{device_id}/activate | Activate Device
[**apps_devices_api_batch_update_locations**](DevicesApi.md#apps_devices_api_batch_update_locations) | **POST** /api/v1/devices/batch-update | Batch Update Locations
[**apps_devices_api_create_device**](DevicesApi.md#apps_devices_api_create_device) | **POST** /api/v1/devices/ | Create Device
[**apps_devices_api_create_manager_session_note**](DevicesApi.md#apps_devices_api_create_manager_session_note) | **POST** /api/v1/devices/{device_uuid}/sessions/{session_id}/notes | Create Manager Session Note
[**apps_devices_api_deactivate_device**](DevicesApi.md#apps_devices_api_deactivate_device) | **POST** /api/v1/devices/{device_id}/deactivate | Deactivate Device
[**apps_devices_api_delete_device**](DevicesApi.md#apps_devices_api_delete_device) | **DELETE** /api/v1/devices/{device_id} | Delete Device
[**apps_devices_api_end_shift**](DevicesApi.md#apps_devices_api_end_shift) | **POST** /api/v1/devices/{device_id}/end-shift | End Shift
[**apps_devices_api_export_events_endpoint**](DevicesApi.md#apps_devices_api_export_events_endpoint) | **GET** /api/v1/devices/events/export | Export Events Endpoint
[**apps_devices_api_get_active_session**](DevicesApi.md#apps_devices_api_get_active_session) | **GET** /api/v1/devices/{device_uuid}/active-session | Get Active Session
[**apps_devices_api_get_dashboard_stats**](DevicesApi.md#apps_devices_api_get_dashboard_stats) | **GET** /api/v1/devices/dashboard-stats | Get Dashboard Stats
[**apps_devices_api_get_dashboard_stats_timeline**](DevicesApi.md#apps_devices_api_get_dashboard_stats_timeline) | **GET** /api/v1/devices/dashboard-stats/timeline | Get Dashboard Stats Timeline
[**apps_devices_api_get_device**](DevicesApi.md#apps_devices_api_get_device) | **GET** /api/v1/devices/{device_id} | Get Device
[**apps_devices_api_get_device_events**](DevicesApi.md#apps_devices_api_get_device_events) | **GET** /api/v1/devices/{device_id}/events | Get Device Events
[**apps_devices_api_get_device_sessions**](DevicesApi.md#apps_devices_api_get_device_sessions) | **GET** /api/v1/devices/{device_id}/sessions | Get Device Sessions
[**apps_devices_api_get_event_detail**](DevicesApi.md#apps_devices_api_get_event_detail) | **GET** /api/v1/devices/events/{event_id} | Get Event Detail
[**apps_devices_api_get_import_job**](DevicesApi.md#apps_devices_api_get_import_job) | **GET** /api/v1/devices/locations/import/{job_id} | Get Import Job
[**apps_devices_api_get_location_stats**](DevicesApi.md#apps_devices_api_get_location_stats) | **GET** /api/v1/devices/stats | Get Location Stats
[**apps_devices_api_get_recent_events**](DevicesApi.md#apps_devices_api_get_recent_events) | **GET** /api/v1/devices/events/recent | Get Recent Events
[**apps_devices_api_get_recent_locations**](DevicesApi.md#apps_devices_api_get_recent_locations) | **GET** /api/v1/devices/{device_id}/locations/recent | Get Recent Locations
[**apps_devices_api_get_session_detail**](DevicesApi.md#apps_devices_api_get_session_detail) | **GET** /api/v1/devices/{device_id}/sessions/{session_id} | Get Session Detail
[**apps_devices_api_get_session_locations**](DevicesApi.md#apps_devices_api_get_session_locations) | **GET** /api/v1/devices/{device_id}/sessions/{session_id}/locations | Get Session Locations
[**apps_devices_api_list_devices**](DevicesApi.md#apps_devices_api_list_devices) | **GET** /api/v1/devices/ | List Devices
[**apps_devices_api_list_session_attachments**](DevicesApi.md#apps_devices_api_list_session_attachments) | **GET** /api/v1/devices/{device_uuid}/sessions/{session_id}/attachments | List Session Attachments
[**apps_devices_api_list_session_notes**](DevicesApi.md#apps_devices_api_list_session_notes) | **GET** /api/v1/devices/{device_uuid}/sessions/{session_id}/notes | List Session Notes
[**apps_devices_api_list_session_photos**](DevicesApi.md#apps_devices_api_list_session_photos) | **GET** /api/v1/devices/{device_uuid}/sessions/{session_id}/photos | List Session Photos
[**apps_devices_api_list_workspace_photos**](DevicesApi.md#apps_devices_api_list_workspace_photos) | **GET** /api/v1/devices/photos | List Workspace Photos
[**apps_devices_api_pause_shift**](DevicesApi.md#apps_devices_api_pause_shift) | **POST** /api/v1/devices/{device_id}/pause-shift | Pause Shift
[**apps_devices_api_resume_shift**](DevicesApi.md#apps_devices_api_resume_shift) | **POST** /api/v1/devices/{device_id}/resume-shift | Resume Shift
[**apps_devices_api_start_shift**](DevicesApi.md#apps_devices_api_start_shift) | **POST** /api/v1/devices/{device_id}/start-shift | Start Shift
[**apps_devices_api_update_device**](DevicesApi.md#apps_devices_api_update_device) | **PUT** /api/v1/devices/{device_id} | Update Device
[**apps_devices_api_update_device_location**](DevicesApi.md#apps_devices_api_update_device_location) | **POST** /api/v1/devices/{device_id}/location | Update Device Location
[**apps_devices_api_update_session_notes**](DevicesApi.md#apps_devices_api_update_session_notes) | **POST** /api/v1/devices/{device_id}/notes | Update Session Notes
[**apps_devices_api_upload_csv_import**](DevicesApi.md#apps_devices_api_upload_csv_import) | **POST** /api/v1/devices/locations/import | Upload Csv Import


# **apps_devices_api_activate_device**
> DeviceOut apps_devices_api_activate_device(device_id)

Activate Device

Activate a device - admin/manager action (PRD §4.2).  This is an administrative action that enables the device. - Managers/owners: Can activate any workspace device - Field workers: Can only activate their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.device_out import DeviceOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Activate Device
        api_response = await api_instance.apps_devices_api_activate_device(device_id)
        print("The response of DevicesApi->apps_devices_api_activate_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_activate_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceOut**](DeviceOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_batch_update_locations**
> List[LocationUpdateOut] apps_devices_api_batch_update_locations(batch_location_update_in)

Batch Update Locations

Update locations for multiple devices in batch.  PRD §5.3: Server-side shift enforcement - Device must be enabled (is_active) - Shift must be active, OR timestamp falls within past shift window - Only device owner can upload locations (BYOD security)

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.batch_location_update_in import BatchLocationUpdateIn
from spatialflow_generated.models.location_update_out import LocationUpdateOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    batch_location_update_in = [spatialflow_generated.BatchLocationUpdateIn()] # List[BatchLocationUpdateIn] | 

    try:
        # Batch Update Locations
        api_response = await api_instance.apps_devices_api_batch_update_locations(batch_location_update_in)
        print("The response of DevicesApi->apps_devices_api_batch_update_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_batch_update_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_location_update_in** | [**List[BatchLocationUpdateIn]**](BatchLocationUpdateIn.md)|  | 

### Return type

[**List[LocationUpdateOut]**](LocationUpdateOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_create_device**
> DeviceOut apps_devices_api_create_device(device_in)

Create Device

Register a new device for tracking.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.device_in import DeviceIn
from spatialflow_generated.models.device_out import DeviceOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_in = spatialflow_generated.DeviceIn() # DeviceIn | 

    try:
        # Create Device
        api_response = await api_instance.apps_devices_api_create_device(device_in)
        print("The response of DevicesApi->apps_devices_api_create_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_create_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_in** | [**DeviceIn**](DeviceIn.md)|  | 

### Return type

[**DeviceOut**](DeviceOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_create_manager_session_note**
> SessionNoteOut apps_devices_api_create_manager_session_note(device_uuid, session_id, session_note_in)

Create Manager Session Note

Append a manager-authored SessionNote (manager + owner only per D-04, append-only per D-03).  Body is truncated to 2000 chars to match the field-worker constraint. Allowed on active OR closed sessions (D-03 supports retroactive annotation). Each POST inserts a NEW SessionNote row — no upsert.  WR-05: returns 201 Created (RFC 7231 §6.3.2) since this is genuine resource creation. The mobile NotesUpdateOut endpoint still returns 200 because it is an upsert, not a create.  WR-06: rejects an empty / whitespace-only body with 400 + error_code=\"EMPTY_BODY\" rather than inserting a noise row.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.session_note_in import SessionNoteIn
from spatialflow_generated.models.session_note_out import SessionNoteOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_uuid = 'device_uuid_example' # str | 
    session_id = 'session_id_example' # str | 
    session_note_in = spatialflow_generated.SessionNoteIn() # SessionNoteIn | 

    try:
        # Create Manager Session Note
        api_response = await api_instance.apps_devices_api_create_manager_session_note(device_uuid, session_id, session_note_in)
        print("The response of DevicesApi->apps_devices_api_create_manager_session_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_create_manager_session_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **str**|  | 
 **session_id** | **str**|  | 
 **session_note_in** | [**SessionNoteIn**](SessionNoteIn.md)|  | 

### Return type

[**SessionNoteOut**](SessionNoteOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_deactivate_device**
> DeviceOut apps_devices_api_deactivate_device(device_id)

Deactivate Device

Deactivate a device - admin/manager action (PRD §4.2).  This is an administrative action that disables the device entirely. - Managers/owners: Can deactivate any workspace device - Field workers: Can only deactivate their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.device_out import DeviceOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Deactivate Device
        api_response = await api_instance.apps_devices_api_deactivate_device(device_id)
        print("The response of DevicesApi->apps_devices_api_deactivate_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_deactivate_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceOut**](DeviceOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_delete_device**
> apps_devices_api_delete_device(device_id)

Delete Device

Delete a device (PRD §4.2).  - Managers/owners: Can delete any workspace device - Field workers: Can only delete their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Delete Device
        await api_instance.apps_devices_api_delete_device(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_delete_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_end_shift**
> ShiftActionOut apps_devices_api_end_shift(device_id)

End Shift

End a tracking shift (PRD §5.3).  BYOD Security: Only the device owner can end their shift. Location uploads stop. Offline-buffered locations with timestamps within the shift window will still be accepted.  State transition: ACTIVE → OFF (or PAUSED → OFF)

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.shift_action_out import ShiftActionOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # End Shift
        api_response = await api_instance.apps_devices_api_end_shift(device_id)
        print("The response of DevicesApi->apps_devices_api_end_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_end_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**ShiftActionOut**](ShiftActionOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_export_events_endpoint**
> Dict[str, object] apps_devices_api_export_events_endpoint(format, from_date=from_date, to_date=to_date, device_ids=device_ids, geofence_ids=geofence_ids, event_type=event_type)

Export Events Endpoint

Export events endpoint - delegates to api_export module

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
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
    api_instance = spatialflow_generated.DevicesApi(api_client)
    format = 'format_example' # str | 
    from_date = 'from_date_example' # str |  (optional)
    to_date = 'to_date_example' # str |  (optional)
    device_ids = 'device_ids_example' # str |  (optional)
    geofence_ids = 'geofence_ids_example' # str |  (optional)
    event_type = 'event_type_example' # str |  (optional)

    try:
        # Export Events Endpoint
        api_response = await api_instance.apps_devices_api_export_events_endpoint(format, from_date=from_date, to_date=to_date, device_ids=device_ids, geofence_ids=geofence_ids, event_type=event_type)
        print("The response of DevicesApi->apps_devices_api_export_events_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_export_events_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | 
 **from_date** | **str**|  | [optional] 
 **to_date** | **str**|  | [optional] 
 **device_ids** | **str**|  | [optional] 
 **geofence_ids** | **str**|  | [optional] 
 **event_type** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_active_session**
> DeviceSessionOut apps_devices_api_get_active_session(device_uuid)

Get Active Session

Get the open DeviceSession for the device's current shift.  Returns 200 + DeviceSessionOut when the device has an open session (ended_at IS NULL). Returns 404 when the device is not currently on shift (shift_status='off').  Lazy-creates a session row for legacy in-flight v1.19 shifts (device.shift_status='active' but no open DeviceSession row), using device.shift_started_at as the started_at value. This reconciliation is idempotent: a second call returns the same session row.  Role scoping (via get_device_with_permission): - field_worker: only own device (other device → 404) - manager/owner: any workspace device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.device_session_out import DeviceSessionOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_uuid = 'device_uuid_example' # str | 

    try:
        # Get Active Session
        api_response = await api_instance.apps_devices_api_get_active_session(device_uuid)
        print("The response of DevicesApi->apps_devices_api_get_active_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_active_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **str**|  | 

### Return type

[**DeviceSessionOut**](DeviceSessionOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_dashboard_stats**
> DashboardStatsOut apps_devices_api_get_dashboard_stats()

Get Dashboard Stats

Get KPI statistics for the dashboard ops view.  Returns counts for: - live_count: Devices with location update in the last 10 minutes - offline_stale_count: Active devices without recent location - in_geofence_count: Devices currently inside a geofence - alerts_open: Open alert notifications (dashboard alerts) - workflow_failures_1h: Failed workflow executions in the last hour - webhook_retries_1h: Webhook deliveries pending retry in the last hour  - Managers/owners: See stats for all workspace devices - Field workers: See stats for only their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.dashboard_stats_out import DashboardStatsOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)

    try:
        # Get Dashboard Stats
        api_response = await api_instance.apps_devices_api_get_dashboard_stats()
        print("The response of DevicesApi->apps_devices_api_get_dashboard_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_dashboard_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DashboardStatsOut**](DashboardStatsOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_dashboard_stats_timeline**
> DashboardStatsTimelineOut apps_devices_api_get_dashboard_stats_timeline(time_range=time_range, start_date=start_date, end_date=end_date)

Get Dashboard Stats Timeline

Get time-bucketed KPI counts for sparkline rendering and delta indicators.  Returns hourly-bucketed counts (today), 6-hour buckets (7d), or daily buckets (30d) for live, offline/stale, and in-geofence metrics, plus previous-period comparison values.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.dashboard_stats_timeline_out import DashboardStatsTimelineOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    time_range = 'today' # str | Time range: today, 7d, 30d, or custom (optional) (default to 'today')
    start_date = 'start_date_example' # str | Custom start date (ISO 8601) (optional)
    end_date = 'end_date_example' # str | Custom end date (ISO 8601) (optional)

    try:
        # Get Dashboard Stats Timeline
        api_response = await api_instance.apps_devices_api_get_dashboard_stats_timeline(time_range=time_range, start_date=start_date, end_date=end_date)
        print("The response of DevicesApi->apps_devices_api_get_dashboard_stats_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_dashboard_stats_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_range** | **str**| Time range: today, 7d, 30d, or custom | [optional] [default to &#39;today&#39;]
 **start_date** | **str**| Custom start date (ISO 8601) | [optional] 
 **end_date** | **str**| Custom end date (ISO 8601) | [optional] 

### Return type

[**DashboardStatsTimelineOut**](DashboardStatsTimelineOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_device**
> DeviceOut apps_devices_api_get_device(device_id)

Get Device

Get device details by UUID (PRD §4).  - Managers/owners: Can view any workspace device - Field workers: Can only view their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.device_out import DeviceOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Get Device
        api_response = await api_instance.apps_devices_api_get_device(device_id)
        print("The response of DevicesApi->apps_devices_api_get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**DeviceOut**](DeviceOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_device_events**
> List[GeofenceEventOut] apps_devices_api_get_device_events(device_id, limit=limit, offset=offset)

Get Device Events

Get geofence events for a device (PRD §4).  - Managers/owners: Can view events for any workspace device - Field workers: Can only view events for their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.geofence_event_out import GeofenceEventOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Device Events
        api_response = await api_instance.apps_devices_api_get_device_events(device_id, limit=limit, offset=offset)
        print("The response of DevicesApi->apps_devices_api_get_device_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_device_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[GeofenceEventOut]**](GeofenceEventOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_device_sessions**
> DeviceSessionsOut apps_devices_api_get_device_sessions(device_id, limit=limit, offset=offset)

Get Device Sessions

Get completed session history for a device.  Returns a list of all completed tracking sessions (shifts) with computed stats like duration, location count, and distance traveled.  - Managers/owners: Can view sessions for any workspace device - Field workers: Can only view sessions for their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.device_sessions_out import DeviceSessionsOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = 20 # int |  (optional) (default to 20)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Device Sessions
        api_response = await api_instance.apps_devices_api_get_device_sessions(device_id, limit=limit, offset=offset)
        print("The response of DevicesApi->apps_devices_api_get_device_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_device_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 20]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**DeviceSessionsOut**](DeviceSessionsOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_event_detail**
> Dict[str, object] apps_devices_api_get_event_detail(event_id)

Get Event Detail

Get a single geofence event by ID (PRD §4).  Uses workspace-scoped RBAC — same rules as get_recent_events.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    event_id = 'event_id_example' # str | 

    try:
        # Get Event Detail
        api_response = await api_instance.apps_devices_api_get_event_detail(event_id)
        print("The response of DevicesApi->apps_devices_api_get_event_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_event_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_import_job**
> LocationImportResponse apps_devices_api_get_import_job(job_id)

Get Import Job

Get status of a location import job.  Returns the current status, progress, and error details of an import job. Poll this endpoint to track job execution.  **Authentication:** JWT token required **Authorization:** Must be in the same organization as the job  **Job Statuses:** - `pending`: Job queued, not yet started - `processing`: Job is parsing CSV and queueing locations - `completed`: Job finished successfully (locations queued for processing) - `failed`: Job encountered an error (see error_message)  **Error Handling:** If error_rate > 1%, the job will fail with first 100 errors listed.  **PRD Reference:** §3.1.2 CSV Import Schema

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.location_import_response import LocationImportResponse
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
    api_instance = spatialflow_generated.DevicesApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get Import Job
        api_response = await api_instance.apps_devices_api_get_import_job(job_id)
        print("The response of DevicesApi->apps_devices_api_get_import_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_import_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**LocationImportResponse**](LocationImportResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_location_stats**
> DeviceStatsOut apps_devices_api_get_location_stats()

Get Location Stats

Get location activity statistics based on user's workspace role (PRD §4).  - Managers/owners: See stats for all workspace devices - Field workers: See stats for only their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.device_stats_out import DeviceStatsOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)

    try:
        # Get Location Stats
        api_response = await api_instance.apps_devices_api_get_location_stats()
        print("The response of DevicesApi->apps_devices_api_get_location_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_location_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeviceStatsOut**](DeviceStatsOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_recent_events**
> RecentEventsOut apps_devices_api_get_recent_events(limit=limit, offset=offset, device_id=device_id, geofence_id=geofence_id, event_type=event_type, time_range=time_range, start_date=start_date, end_date=end_date, sort=sort)

Get Recent Events

Get recent geofence events based on user's workspace role (PRD §4).  - Managers/owners: See events for all workspace devices - Field workers: See events for only their own devices

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.recent_events_out import RecentEventsOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    device_id = 'device_id_example' # str |  (optional)
    geofence_id = 'geofence_id_example' # str |  (optional)
    event_type = 'event_type_example' # str |  (optional)
    time_range = 'time_range_example' # str | Time range: today, 7d, 30d, or custom (optional)
    start_date = 'start_date_example' # str | Custom start date (YYYY-MM-DD) (optional)
    end_date = 'end_date_example' # str | Custom end date (YYYY-MM-DD) (optional)
    sort = 'sort_example' # str | Sort order: -timestamp (default) or timestamp (optional)

    try:
        # Get Recent Events
        api_response = await api_instance.apps_devices_api_get_recent_events(limit=limit, offset=offset, device_id=device_id, geofence_id=geofence_id, event_type=event_type, time_range=time_range, start_date=start_date, end_date=end_date, sort=sort)
        print("The response of DevicesApi->apps_devices_api_get_recent_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_recent_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **device_id** | **str**|  | [optional] 
 **geofence_id** | **str**|  | [optional] 
 **event_type** | **str**|  | [optional] 
 **time_range** | **str**| Time range: today, 7d, 30d, or custom | [optional] 
 **start_date** | **str**| Custom start date (YYYY-MM-DD) | [optional] 
 **end_date** | **str**| Custom end date (YYYY-MM-DD) | [optional] 
 **sort** | **str**| Sort order: -timestamp (default) or timestamp | [optional] 

### Return type

[**RecentEventsOut**](RecentEventsOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_recent_locations**
> RecentLocationsOut apps_devices_api_get_recent_locations(device_id, limit=limit)

Get Recent Locations

Get recent locations for a device, independent of sessions.  Returns the most recent GPS points for the device, ordered newest-first. Useful for rendering device trails when no session history exists (e.g. devices that haven't started shifts).  - Managers/owners: Can view locations for any workspace device - Field workers: Can only view locations for their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.recent_locations_out import RecentLocationsOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    limit = 500 # int |  (optional) (default to 500)

    try:
        # Get Recent Locations
        api_response = await api_instance.apps_devices_api_get_recent_locations(device_id, limit=limit)
        print("The response of DevicesApi->apps_devices_api_get_recent_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_recent_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 500]

### Return type

[**RecentLocationsOut**](RecentLocationsOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_session_detail**
> DeviceSessionOut apps_devices_api_get_session_detail(device_id, session_id)

Get Session Detail

Get single session details.  Returns detailed information about a specific completed session, including time bounds needed for location queries.  - Managers/owners: Can view sessions for any workspace device - Field workers: Can only view sessions for their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.device_session_out import DeviceSessionOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    session_id = 'session_id_example' # str | 

    try:
        # Get Session Detail
        api_response = await api_instance.apps_devices_api_get_session_detail(device_id, session_id)
        print("The response of DevicesApi->apps_devices_api_get_session_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_session_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

[**DeviceSessionOut**](DeviceSessionOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_session_locations**
> SessionLocationsOut apps_devices_api_get_session_locations(device_id, session_id, limit=limit, offset=offset, max_points=max_points)

Get Session Locations

Get locations for a specific session with pagination or simplification.  Returns GPS track points recorded during the session.  **Pagination mode** (default): Use `limit` and `offset` to paginate through all points.  **Simplification mode**: Set `max_points` to return a simplified track using Douglas-Peucker algorithm (PostGIS ST_Simplify). Useful for rendering long tracks without loading all points. When `max_points` is set, pagination is ignored.  Important notes for simplification mode: - `max_points` is a **target**, not a hard cap. Actual count may vary based on track shape. - When `simplified=true`, timestamps are **linearly interpolated** between session   start/end and should not be used for speed or pause analysis. - Accuracy, speed, and heading are lost during simplification (returned as null).  Note: Track history only includes location updates that pass quality filters (accuracy <= 100m, minimum movement distance). This ensures clean GPS tracks without jitter or poor-quality readings.  - Managers/owners: Can view locations for any workspace device - Field workers: Can only view locations for their own device

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.session_locations_out import SessionLocationsOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    session_id = 'session_id_example' # str | 
    limit = 1000 # int |  (optional) (default to 1000)
    offset = 0 # int |  (optional) (default to 0)
    max_points = 56 # int |  (optional)

    try:
        # Get Session Locations
        api_response = await api_instance.apps_devices_api_get_session_locations(device_id, session_id, limit=limit, offset=offset, max_points=max_points)
        print("The response of DevicesApi->apps_devices_api_get_session_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_get_session_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **session_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 1000]
 **offset** | **int**|  | [optional] [default to 0]
 **max_points** | **int**|  | [optional] 

### Return type

[**SessionLocationsOut**](SessionLocationsOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_list_devices**
> List[DeviceOut] apps_devices_api_list_devices(is_active=is_active, include_geofences=include_geofences)

List Devices

List devices based on user's workspace role (PRD §4).  - Managers/owners: See all workspace devices - Field workers: See only their own device  Args:     is_active: Filter by device active status     include_geofences: Include in_geofence_ids for each device (default False, opt-in for dashboard)

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.device_out import DeviceOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    is_active = True # bool |  (optional)
    include_geofences = False # bool |  (optional) (default to False)

    try:
        # List Devices
        api_response = await api_instance.apps_devices_api_list_devices(is_active=is_active, include_geofences=include_geofences)
        print("The response of DevicesApi->apps_devices_api_list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_active** | **bool**|  | [optional] 
 **include_geofences** | **bool**|  | [optional] [default to False]

### Return type

[**List[DeviceOut]**](DeviceOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_list_session_attachments**
> List[StoredFileAttachmentOut] apps_devices_api_list_session_attachments(device_uuid, session_id)

List Session Attachments

List attachments (StoredFile records) linked to a device session.  Role scoping (D-09): - field_worker: sees only attachments from their own sessions. - manager/owner: sees all workspace-wide attachments for the session.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.stored_file_attachment_out import StoredFileAttachmentOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_uuid = 'device_uuid_example' # str | 
    session_id = 'session_id_example' # str | 

    try:
        # List Session Attachments
        api_response = await api_instance.apps_devices_api_list_session_attachments(device_uuid, session_id)
        print("The response of DevicesApi->apps_devices_api_list_session_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_list_session_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

[**List[StoredFileAttachmentOut]**](StoredFileAttachmentOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_list_session_notes**
> List[SessionNoteOut] apps_devices_api_list_session_notes(device_uuid, session_id)

List Session Notes

List SessionNote rows for a session (oldest first per D-20).  Role scoping (D-09 / D-14): - field_worker: only own device's session notes - manager/owner: any workspace device's session notes  Returns a uniform 403 for non-existent / cross-device / cross-workspace / unauthorized-field-worker cases (prevents session-ID enumeration via differential 403 vs 404).

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.session_note_out import SessionNoteOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_uuid = 'device_uuid_example' # str | 
    session_id = 'session_id_example' # str | 

    try:
        # List Session Notes
        api_response = await api_instance.apps_devices_api_list_session_notes(device_uuid, session_id)
        print("The response of DevicesApi->apps_devices_api_list_session_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_list_session_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

[**List[SessionNoteOut]**](SessionNoteOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_list_session_photos**
> List[PhotoOut] apps_devices_api_list_session_photos(device_uuid, session_id)

List Session Photos

List image-typed StoredFile attachments for a session with derived GPS coords.  Phase 120-04 (D-11). Each row is a PhotoOut whose lat/lon are resolved per D-07 (nearest DeviceLocation within ±60s of captured_at, falling back to PostGIS ST_LineInterpolatePoint on the session's track_geometry for closed sessions, falling back to null). Newest-first ordering (D-17). Presigned download URL with TTL=3600 (D-18).  Coexists with GET .../sessions/{session_id}/attachments which returns ALL attachment types — that endpoint is preserved unchanged for the v1.20 mobile consumer (Plan 105) per CONTEXT D-11.  Role scoping (D-12 = v1.20 D-09): - field_worker: only own device's photos - manager/owner: any workspace device's photos

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.photo_out import PhotoOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_uuid = 'device_uuid_example' # str | 
    session_id = 'session_id_example' # str | 

    try:
        # List Session Photos
        api_response = await api_instance.apps_devices_api_list_session_photos(device_uuid, session_id)
        print("The response of DevicesApi->apps_devices_api_list_session_photos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_list_session_photos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_uuid** | **str**|  | 
 **session_id** | **str**|  | 

### Return type

[**List[PhotoOut]**](PhotoOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_list_workspace_photos**
> WorkspacePhotosOut apps_devices_api_list_workspace_photos(var_from=var_from, to=to, device_ids=device_ids, limit=limit)

List Workspace Photos

List workspace-wide photos with renderable GPS coords (Phase 122-01).  Returns the newest ``limit`` photos (max 500) whose captured_at is in [from, to] across all workspace devices the requester can see. Photos whose coordinate resolution returns null are excluded (D-05) — only renderable photos cross the wire for the dashboard map layer.  Role scoping (D-04 / v1.20 D-09): - field_worker: only own device's photos - manager/owner: all workspace devices  Cross-workspace ``device_ids`` are silently filtered out (no information leak via differential 403). Over 50 ``device_ids`` returns 400 TOO_MANY_DEVICE_IDS to bound query parameter abuse.  Coexists with GET /devices/{uuid}/sessions/{sid}/photos which is preserved unchanged (Phase 120-04). The two endpoints have intentionally different null-coord semantics: per-session keeps null-coord rows (still listed in the session detail panel), workspace-wide drops them (can't render).

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_photos_out import WorkspacePhotosOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Earliest captured_at (default: now - 24h) (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Latest captured_at (default: now) (optional)
    device_ids = ['device_ids_example'] # List[Optional[str]] | Restrict to these device IDs (max 50) (optional)
    limit = 500 # int | Soft cap; max 500 newest (optional) (default to 500)

    try:
        # List Workspace Photos
        api_response = await api_instance.apps_devices_api_list_workspace_photos(var_from=var_from, to=to, device_ids=device_ids, limit=limit)
        print("The response of DevicesApi->apps_devices_api_list_workspace_photos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_list_workspace_photos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **datetime**| Earliest captured_at (default: now - 24h) | [optional] 
 **to** | **datetime**| Latest captured_at (default: now) | [optional] 
 **device_ids** | [**List[Optional[str]]**](str.md)| Restrict to these device IDs (max 50) | [optional] 
 **limit** | **int**| Soft cap; max 500 newest | [optional] [default to 500]

### Return type

[**WorkspacePhotosOut**](WorkspacePhotosOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_pause_shift**
> ShiftActionOut apps_devices_api_pause_shift(device_id)

Pause Shift

Pause a tracking shift (PRD §5.3).  BYOD Security: Only the device owner can pause their shift. Location uploads are paused until resumed.  State transition: ACTIVE → PAUSED

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.shift_action_out import ShiftActionOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Pause Shift
        api_response = await api_instance.apps_devices_api_pause_shift(device_id)
        print("The response of DevicesApi->apps_devices_api_pause_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_pause_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**ShiftActionOut**](ShiftActionOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_resume_shift**
> ShiftActionOut apps_devices_api_resume_shift(device_id)

Resume Shift

Resume a paused tracking shift (PRD §5.3).  BYOD Security: Only the device owner can resume their shift. Location uploads resume.  State transition: PAUSED → ACTIVE

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.shift_action_out import ShiftActionOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Resume Shift
        api_response = await api_instance.apps_devices_api_resume_shift(device_id)
        print("The response of DevicesApi->apps_devices_api_resume_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_resume_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**ShiftActionOut**](ShiftActionOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_start_shift**
> ShiftActionOut apps_devices_api_start_shift(device_id)

Start Shift

Start a tracking shift (PRD §5.3).  BYOD Security: Only the device owner can start their shift. This enables location uploads for this device.  State transition: OFF → ACTIVE Note: If paused, use resume-shift instead.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.shift_action_out import ShiftActionOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 

    try:
        # Start Shift
        api_response = await api_instance.apps_devices_api_start_shift(device_id)
        print("The response of DevicesApi->apps_devices_api_start_shift:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_start_shift: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 

### Return type

[**ShiftActionOut**](ShiftActionOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_update_device**
> DeviceOut apps_devices_api_update_device(device_id, update_device_in)

Update Device

Update device name, type, or metadata.  - Managers/owners: Can edit any workspace device - Field workers: Can only edit their own device  Note: device_id (external identifier) is NOT editable for BYOD security.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.device_out import DeviceOut
from spatialflow_generated.models.update_device_in import UpdateDeviceIn
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    update_device_in = spatialflow_generated.UpdateDeviceIn() # UpdateDeviceIn | 

    try:
        # Update Device
        api_response = await api_instance.apps_devices_api_update_device(device_id, update_device_in)
        print("The response of DevicesApi->apps_devices_api_update_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_update_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **update_device_in** | [**UpdateDeviceIn**](UpdateDeviceIn.md)|  | 

### Return type

[**DeviceOut**](DeviceOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_update_device_location**
> LocationUpdateOut apps_devices_api_update_device_location(device_id, location_update_in)

Update Device Location

Update device location and trigger geofence events.  PRD §4.2 & §5.3: BYOD Security + Shift Enforcement - Only device owner can upload locations - Device must be enabled (is_active) - Shift must be active, OR timestamp falls within past shift window

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.location_update_in import LocationUpdateIn
from spatialflow_generated.models.location_update_out import LocationUpdateOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    location_update_in = spatialflow_generated.LocationUpdateIn() # LocationUpdateIn | 

    try:
        # Update Device Location
        api_response = await api_instance.apps_devices_api_update_device_location(device_id, location_update_in)
        print("The response of DevicesApi->apps_devices_api_update_device_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_update_device_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **location_update_in** | [**LocationUpdateIn**](LocationUpdateIn.md)|  | 

### Return type

[**LocationUpdateOut**](LocationUpdateOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_update_session_notes**
> NotesUpdateOut apps_devices_api_update_session_notes(device_id, notes_update_in)

Update Session Notes

Update notes for the current active session.  Mobile-facing endpoint (preserved contract from v1.20). Each call:   1. Truncates the payload to 2000 chars.   2. Writes the truncated body to device.current_session_notes (mobile pre-fill cache).   3. Upserts a SessionNote row keyed on (active_session, author=request.auth)      so the manager-side GET in v1.23 sees an authored note row.  The upsert is idempotent across repeated POSTs during the same shift — calls 2..N update the same row's body and refresh created_at. A new shift gets a new SessionNote because the (session, author) key differs.  Concurrency (CR-01): the (session, author) upsert is serialized via select_for_update() on the Device row inside transaction.atomic(). Two concurrent POSTs from the same authenticated user (offline-buffered flush, mobile retry storm, multi-tab race) block at the lock so the second caller sees the first caller's row via update_or_create.get() and falls into the UPDATE branch — preventing duplicate (session, author) rows. The Device row lock serializes per-device POSTs without holding a workspace-wide lock.  BYOD Security: Only the device owner can update notes (enforced by get_device_with_permission(require_write=True)). Must have an active or paused shift to update notes.  Notes are limited to 2000 characters.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.notes_update_in import NotesUpdateIn
from spatialflow_generated.models.notes_update_out import NotesUpdateOut
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

# Configure API key authorization: APIKeyBearer
configuration.api_key['APIKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyBearer'] = 'Bearer'

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.DevicesApi(api_client)
    device_id = 'device_id_example' # str | 
    notes_update_in = spatialflow_generated.NotesUpdateIn() # NotesUpdateIn | 

    try:
        # Update Session Notes
        api_response = await api_instance.apps_devices_api_update_session_notes(device_id, notes_update_in)
        print("The response of DevicesApi->apps_devices_api_update_session_notes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_update_session_notes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **notes_update_in** | [**NotesUpdateIn**](NotesUpdateIn.md)|  | 

### Return type

[**NotesUpdateOut**](NotesUpdateOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_upload_csv_import**
> LocationImportResponse apps_devices_api_upload_csv_import(file)

Upload Csv Import

Upload CSV file for bulk location import.  This endpoint accepts a CSV file with location data and queues it for async processing. Useful for customer migrations or bulk historical data imports.  **Authentication:** JWT token required **Max File Size:** 50 MB **Max Rows:** 500,000  **CSV Format:** ```csv device_id,ts,lat,lon,accuracy_m,speed_mps,heading_deg,meta_driver truck-005,2025-10-01T14:12:03Z,42.651,-73.756,9.2,12.4,180,alice truck-006,2025-10-01T14:13:00Z,42.652,-73.757,8.5,15.0,175,bob ```  **Required Columns:** - `device_id`: Unique device identifier - `ts`: ISO-8601 timestamp - `lat`: Latitude (-90 to 90) - `lon`: Longitude (-180 to 180)  **Optional Columns:** - `accuracy_m`: GPS accuracy in meters - `speed_mps`: Speed in meters per second - `heading_deg`: Heading in degrees (0-359) - `meta_*`: Metadata columns (e.g., meta_driver, meta_cargo)  **Validation Rules:** - Rejects entire import if >1% rows are invalid - Rejects timestamps > 5 minutes in the future - Warns for timestamps > 30 days old  **PRD Reference:** §3.1.2 CSV Import Schema **Roadmap:** Phase 2, Task 2.2

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.location_import_response import LocationImportResponse
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
    api_instance = spatialflow_generated.DevicesApi(api_client)
    file = None # bytearray | 

    try:
        # Upload Csv Import
        api_response = await api_instance.apps_devices_api_upload_csv_import(file)
        print("The response of DevicesApi->apps_devices_api_upload_csv_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_upload_csv_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

### Return type

[**LocationImportResponse**](LocationImportResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

