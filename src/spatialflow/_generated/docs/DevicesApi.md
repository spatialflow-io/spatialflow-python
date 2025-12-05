# spatialflow_generated.DevicesApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_devices_api_activate_device**](DevicesApi.md#apps_devices_api_activate_device) | **POST** /api/v1/devices/{device_id}/activate | Activate Device
[**apps_devices_api_batch_update_locations**](DevicesApi.md#apps_devices_api_batch_update_locations) | **POST** /api/v1/devices/batch-update | Batch Update Locations
[**apps_devices_api_create_device**](DevicesApi.md#apps_devices_api_create_device) | **POST** /api/v1/devices/ | Create Device
[**apps_devices_api_deactivate_device**](DevicesApi.md#apps_devices_api_deactivate_device) | **POST** /api/v1/devices/{device_id}/deactivate | Deactivate Device
[**apps_devices_api_delete_device**](DevicesApi.md#apps_devices_api_delete_device) | **DELETE** /api/v1/devices/{device_id} | Delete Device
[**apps_devices_api_export_events_endpoint**](DevicesApi.md#apps_devices_api_export_events_endpoint) | **GET** /api/v1/devices/events/export | Export Events Endpoint
[**apps_devices_api_get_device**](DevicesApi.md#apps_devices_api_get_device) | **GET** /api/v1/devices/{device_id} | Get Device
[**apps_devices_api_get_device_events**](DevicesApi.md#apps_devices_api_get_device_events) | **GET** /api/v1/devices/{device_id}/events | Get Device Events
[**apps_devices_api_get_import_job**](DevicesApi.md#apps_devices_api_get_import_job) | **GET** /api/v1/devices/locations/import/{job_id} | Get Import Job
[**apps_devices_api_get_location_stats**](DevicesApi.md#apps_devices_api_get_location_stats) | **GET** /api/v1/devices/stats | Get Location Stats
[**apps_devices_api_get_recent_events**](DevicesApi.md#apps_devices_api_get_recent_events) | **GET** /api/v1/devices/events/recent | Get Recent Events
[**apps_devices_api_list_devices**](DevicesApi.md#apps_devices_api_list_devices) | **GET** /api/v1/devices/ | List Devices
[**apps_devices_api_update_device_location**](DevicesApi.md#apps_devices_api_update_device_location) | **POST** /api/v1/devices/{device_id}/location | Update Device Location
[**apps_devices_api_upload_csv_import**](DevicesApi.md#apps_devices_api_upload_csv_import) | **POST** /api/v1/devices/locations/import | Upload Csv Import


# **apps_devices_api_activate_device**
> DeviceOut apps_devices_api_activate_device(device_id)

Activate Device

Activate a device (resume tracking).

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_batch_update_locations**
> List[LocationUpdateOut] apps_devices_api_batch_update_locations(batch_location_update_in)

Batch Update Locations

Update locations for multiple devices in batch.

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
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_deactivate_device**
> DeviceOut apps_devices_api_deactivate_device(device_id)

Deactivate Device

Deactivate a device (stop tracking).

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_delete_device**
> apps_devices_api_delete_device(device_id)

Delete Device

Delete a device.

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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_device**
> DeviceOut apps_devices_api_get_device(device_id)

Get Device

Get device details by device_id.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_device_events**
> List[Dict[str, object]] apps_devices_api_get_device_events(device_id, limit=limit, offset=offset)

Get Device Events

Get geofence events for a device.

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

**List[Dict[str, object]]**

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_location_stats**
> Dict[str, object] apps_devices_api_get_location_stats()

Get Location Stats

Get location activity statistics for the user.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_get_recent_events**
> List[Dict[str, object]] apps_devices_api_get_recent_events(limit=limit, offset=offset, device_id=device_id, geofence_id=geofence_id, event_type=event_type)

Get Recent Events

Get recent geofence events across all user's devices.

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
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    device_id = 'device_id_example' # str |  (optional)
    geofence_id = 'geofence_id_example' # str |  (optional)
    event_type = 'event_type_example' # str |  (optional)

    try:
        # Get Recent Events
        api_response = await api_instance.apps_devices_api_get_recent_events(limit=limit, offset=offset, device_id=device_id, geofence_id=geofence_id, event_type=event_type)
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

### Return type

**List[Dict[str, object]]**

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_list_devices**
> List[DeviceOut] apps_devices_api_list_devices(is_active=is_active)

List Devices

List user's devices.

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

    try:
        # List Devices
        api_response = await api_instance.apps_devices_api_list_devices(is_active=is_active)
        print("The response of DevicesApi->apps_devices_api_list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->apps_devices_api_list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_active** | **bool**|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_update_device_location**
> LocationUpdateOut apps_devices_api_update_device_location(device_id, location_update_in)

Update Device Location

Update device location and trigger geofence events.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

