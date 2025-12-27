# spatialflow_generated.GeofencesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_geofences_api_bulk_create_geofences**](GeofencesApi.md#apps_geofences_api_bulk_create_geofences) | **POST** /api/v1/geofences/bulk | Bulk Create Geofences
[**apps_geofences_api_create_geofence**](GeofencesApi.md#apps_geofences_api_create_geofence) | **POST** /api/v1/geofences/ | Create Geofence
[**apps_geofences_api_delete_geofence**](GeofencesApi.md#apps_geofences_api_delete_geofence) | **DELETE** /api/v1/geofences/{geofence_id} | Delete Geofence
[**apps_geofences_api_geofence_health_check**](GeofencesApi.md#apps_geofences_api_geofence_health_check) | **GET** /api/v1/geofences/health | Geofence Health Check
[**apps_geofences_api_get_active_geofences_summary**](GeofencesApi.md#apps_geofences_api_get_active_geofences_summary) | **GET** /api/v1/geofences/active-summary | Get Active Geofences Summary
[**apps_geofences_api_get_geofence**](GeofencesApi.md#apps_geofences_api_get_geofence) | **GET** /api/v1/geofences/{geofence_id} | Get Geofence
[**apps_geofences_api_get_test_event_history**](GeofencesApi.md#apps_geofences_api_get_test_event_history) | **GET** /api/v1/geofences/{geofence_id}/test-events | Get Test Event History
[**apps_geofences_api_get_upload_job_status**](GeofencesApi.md#apps_geofences_api_get_upload_job_status) | **GET** /api/v1/geofences/upload/{job_id}/status | Get Upload Job Status
[**apps_geofences_api_list_geofence_groups**](GeofencesApi.md#apps_geofences_api_list_geofence_groups) | **GET** /api/v1/geofences/groups | List Geofence Groups
[**apps_geofences_api_list_geofences**](GeofencesApi.md#apps_geofences_api_list_geofences) | **GET** /api/v1/geofences/ | List Geofences
[**apps_geofences_api_list_group_geofences**](GeofencesApi.md#apps_geofences_api_list_group_geofences) | **GET** /api/v1/geofences/groups/{group_id}/geofences | List Group Geofences
[**apps_geofences_api_test_group_point**](GeofencesApi.md#apps_geofences_api_test_group_point) | **POST** /api/v1/geofences/groups/{group_id}/test-point | Test Group Point
[**apps_geofences_api_test_point**](GeofencesApi.md#apps_geofences_api_test_point) | **POST** /api/v1/geofences/test-point | Test Point
[**apps_geofences_api_trigger_test_event**](GeofencesApi.md#apps_geofences_api_trigger_test_event) | **POST** /api/v1/geofences/{geofence_id}/test-event | Trigger Test Event
[**apps_geofences_api_update_geofence**](GeofencesApi.md#apps_geofences_api_update_geofence) | **PUT** /api/v1/geofences/{geofence_id} | Update Geofence
[**apps_geofences_api_update_geofence_group**](GeofencesApi.md#apps_geofences_api_update_geofence_group) | **PUT** /api/v1/geofences/{geofence_id}/group | Update Geofence Group
[**apps_geofences_api_upload_geofences_async**](GeofencesApi.md#apps_geofences_api_upload_geofences_async) | **POST** /api/v1/geofences/upload | Upload Geofences Async


# **apps_geofences_api_bulk_create_geofences**
> Dict[str, object] apps_geofences_api_bulk_create_geofences(bulk_geofence_request)

Bulk Create Geofences

Bulk create multiple geofences.

This endpoint allows users with the BATCH_OPERATIONS feature to create multiple
geofences in a single request. Maximum 100 geofences per request.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.bulk_geofence_request import BulkGeofenceRequest
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    bulk_geofence_request = spatialflow_generated.BulkGeofenceRequest() # BulkGeofenceRequest | 

    try:
        # Bulk Create Geofences
        api_response = await api_instance.apps_geofences_api_bulk_create_geofences(bulk_geofence_request)
        print("The response of GeofencesApi->apps_geofences_api_bulk_create_geofences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_bulk_create_geofences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_geofence_request** | [**BulkGeofenceRequest**](BulkGeofenceRequest.md)|  | 

### Return type

**Dict[str, object]**

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_create_geofence**
> GeofenceResponse apps_geofences_api_create_geofence(create_geofence_request)

Create Geofence

Create new polygon geofence.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.create_geofence_request import CreateGeofenceRequest
from spatialflow_generated.models.geofence_response import GeofenceResponse
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    create_geofence_request = spatialflow_generated.CreateGeofenceRequest() # CreateGeofenceRequest | 

    try:
        # Create Geofence
        api_response = await api_instance.apps_geofences_api_create_geofence(create_geofence_request)
        print("The response of GeofencesApi->apps_geofences_api_create_geofence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_create_geofence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_geofence_request** | [**CreateGeofenceRequest**](CreateGeofenceRequest.md)|  | 

### Return type

[**GeofenceResponse**](GeofenceResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**502** | Bad Gateway |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_delete_geofence**
> Dict[str, object] apps_geofences_api_delete_geofence(geofence_id)

Delete Geofence

Delete (deactivate) geofence.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    geofence_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Geofence
        api_response = await api_instance.apps_geofences_api_delete_geofence(geofence_id)
        print("The response of GeofencesApi->apps_geofences_api_delete_geofence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_delete_geofence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **UUID**|  | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**502** | Bad Gateway |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_geofence_health_check**
> Dict[str, object] apps_geofences_api_geofence_health_check()

Geofence Health Check

Health check for geofence service.

### Example


```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.GeofencesApi(api_client)

    try:
        # Geofence Health Check
        api_response = await api_instance.apps_geofences_api_geofence_health_check()
        print("The response of GeofencesApi->apps_geofences_api_geofence_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_geofence_health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_get_active_geofences_summary**
> Dict[str, object] apps_geofences_api_get_active_geofences_summary()

Get Active Geofences Summary

Get summary of active geofences with event counts for dashboard map widget.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)

    try:
        # Get Active Geofences Summary
        api_response = await api_instance.apps_geofences_api_get_active_geofences_summary()
        print("The response of GeofencesApi->apps_geofences_api_get_active_geofences_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_get_active_geofences_summary: %s\n" % e)
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

# **apps_geofences_api_get_geofence**
> GeofenceResponse apps_geofences_api_get_geofence(geofence_id)

Get Geofence

Get a specific geofence by its ID.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.geofence_response import GeofenceResponse
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    geofence_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Geofence
        api_response = await api_instance.apps_geofences_api_get_geofence(geofence_id)
        print("The response of GeofencesApi->apps_geofences_api_get_geofence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_get_geofence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **UUID**|  | 

### Return type

[**GeofenceResponse**](GeofenceResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**502** | Bad Gateway |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_get_test_event_history**
> apps_geofences_api_get_test_event_history(geofence_id, limit=limit, offset=offset)

Get Test Event History

Get test event history for a geofence.

Args:
    geofence_id: ID of the geofence
    limit: Maximum number of events to return (default 50, max 100)
    offset: Number of events to skip (for pagination)

Returns:
    List of test events with execution details

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    geofence_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Test Event History
        await api_instance.apps_geofences_api_get_test_event_history(geofence_id, limit=limit, offset=offset)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_get_test_event_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **UUID**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_get_upload_job_status**
> UploadJobStatus apps_geofences_api_get_upload_job_status(job_id)

Get Upload Job Status

Get the status of a geofence upload job.

Returns current status, progress, and results (when completed) of the upload job.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.upload_job_status import UploadJobStatus
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    job_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Upload Job Status
        api_response = await api_instance.apps_geofences_api_get_upload_job_status(job_id)
        print("The response of GeofencesApi->apps_geofences_api_get_upload_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_get_upload_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **UUID**|  | 

### Return type

[**UploadJobStatus**](UploadJobStatus.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**502** | Bad Gateway |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_list_geofence_groups**
> Dict[str, object] apps_geofences_api_list_geofence_groups()

List Geofence Groups

List all unique groups for the current user.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)

    try:
        # List Geofence Groups
        api_response = await api_instance.apps_geofences_api_list_geofence_groups()
        print("The response of GeofencesApi->apps_geofences_api_list_geofence_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_list_geofence_groups: %s\n" % e)
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

# **apps_geofences_api_list_geofences**
> GeofenceListResponse apps_geofences_api_list_geofences(limit=limit, offset=offset, active_only=active_only)

List Geofences

Get user's polygon geofences.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.geofence_list_response import GeofenceListResponse
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    active_only = True # bool |  (optional) (default to True)

    try:
        # List Geofences
        api_response = await api_instance.apps_geofences_api_list_geofences(limit=limit, offset=offset, active_only=active_only)
        print("The response of GeofencesApi->apps_geofences_api_list_geofences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_list_geofences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **active_only** | **bool**|  | [optional] [default to True]

### Return type

[**GeofenceListResponse**](GeofenceListResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**502** | Bad Gateway |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_list_group_geofences**
> Dict[str, object] apps_geofences_api_list_group_geofences(group_id)

List Group Geofences

List all geofences in a specific group.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    group_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # List Group Geofences
        api_response = await api_instance.apps_geofences_api_list_group_geofences(group_id)
        print("The response of GeofencesApi->apps_geofences_api_list_group_geofences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_list_group_geofences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **UUID**|  | 

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

# **apps_geofences_api_test_group_point**
> Dict[str, object] apps_geofences_api_test_group_point(group_id, test_point_request)

Test Group Point

Test a point against all geofences in a group.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.test_point_request import TestPointRequest
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    group_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    test_point_request = spatialflow_generated.TestPointRequest() # TestPointRequest | 

    try:
        # Test Group Point
        api_response = await api_instance.apps_geofences_api_test_group_point(group_id, test_point_request)
        print("The response of GeofencesApi->apps_geofences_api_test_group_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_test_group_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **UUID**|  | 
 **test_point_request** | [**TestPointRequest**](TestPointRequest.md)|  | 

### Return type

**Dict[str, object]**

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

# **apps_geofences_api_test_point**
> TestPointResponse apps_geofences_api_test_point(test_point_request)

Test Point

Test a point against user's geofences.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.test_point_request import TestPointRequest
from spatialflow_generated.models.test_point_response import TestPointResponse
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    test_point_request = spatialflow_generated.TestPointRequest() # TestPointRequest | 

    try:
        # Test Point
        api_response = await api_instance.apps_geofences_api_test_point(test_point_request)
        print("The response of GeofencesApi->apps_geofences_api_test_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_test_point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_point_request** | [**TestPointRequest**](TestPointRequest.md)|  | 

### Return type

[**TestPointResponse**](TestPointResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**502** | Bad Gateway |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_trigger_test_event**
> Dict[str, object] apps_geofences_api_trigger_test_event(geofence_id, event_type, test_event_request=test_event_request)

Trigger Test Event

Trigger a simulated test event for a geofence.

This allows users to test their webhooks and workflows without physically
entering or exiting the geofence.

Args:
    geofence_id: ID of the geofence
    event_type: Type of event to simulate ('enter' or 'exit')
    test_metadata: Optional metadata to include in the test event

Returns:
    Test event details including triggered webhooks and workflows

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.test_event_request import TestEventRequest
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    geofence_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    event_type = 'event_type_example' # str | 
    test_event_request = spatialflow_generated.TestEventRequest() # TestEventRequest |  (optional)

    try:
        # Trigger Test Event
        api_response = await api_instance.apps_geofences_api_trigger_test_event(geofence_id, event_type, test_event_request=test_event_request)
        print("The response of GeofencesApi->apps_geofences_api_trigger_test_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_trigger_test_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **UUID**|  | 
 **event_type** | **str**|  | 
 **test_event_request** | [**TestEventRequest**](TestEventRequest.md)|  | [optional] 

### Return type

**Dict[str, object]**

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**502** | Bad Gateway |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_update_geofence**
> GeofenceResponse apps_geofences_api_update_geofence(geofence_id, update_geofence_request)

Update Geofence

Update existing polygon geofence.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.geofence_response import GeofenceResponse
from spatialflow_generated.models.update_geofence_request import UpdateGeofenceRequest
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    geofence_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_geofence_request = spatialflow_generated.UpdateGeofenceRequest() # UpdateGeofenceRequest | 

    try:
        # Update Geofence
        api_response = await api_instance.apps_geofences_api_update_geofence(geofence_id, update_geofence_request)
        print("The response of GeofencesApi->apps_geofences_api_update_geofence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_update_geofence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **UUID**|  | 
 **update_geofence_request** | [**UpdateGeofenceRequest**](UpdateGeofenceRequest.md)|  | 

### Return type

[**GeofenceResponse**](GeofenceResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**502** | Bad Gateway |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_geofences_api_update_geofence_group**
> Dict[str, object] apps_geofences_api_update_geofence_group(geofence_id, group_name=group_name)

Update Geofence Group

Assign or update a geofence's group.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    geofence_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    group_name = 'group_name_example' # str |  (optional)

    try:
        # Update Geofence Group
        api_response = await api_instance.apps_geofences_api_update_geofence_group(geofence_id, group_name=group_name)
        print("The response of GeofencesApi->apps_geofences_api_update_geofence_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_update_geofence_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **geofence_id** | **UUID**|  | 
 **group_name** | **str**|  | [optional] 

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

# **apps_geofences_api_upload_geofences_async**
> AsyncUploadGeofencesResponse apps_geofences_api_upload_geofences_async(upload_geofences_request)

Upload Geofences Async

Upload geofences from a file (asynchronous).

This endpoint queues a background job to process geofence imports from various file formats:
- GeoJSON (.geojson, .json) - Standard geospatial format
- KML (.kml) - Google Earth format
- GPX (.gpx) - GPS track format (converted to polygon buffers)

The file must first be uploaded using the storage API to get a file_id.
All imported geofences can optionally be assigned to a group.

Returns a job ID to track the import progress.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.async_upload_geofences_response import AsyncUploadGeofencesResponse
from spatialflow_generated.models.upload_geofences_request import UploadGeofencesRequest
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
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
    api_instance = spatialflow_generated.GeofencesApi(api_client)
    upload_geofences_request = spatialflow_generated.UploadGeofencesRequest() # UploadGeofencesRequest | 

    try:
        # Upload Geofences Async
        api_response = await api_instance.apps_geofences_api_upload_geofences_async(upload_geofences_request)
        print("The response of GeofencesApi->apps_geofences_api_upload_geofences_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeofencesApi->apps_geofences_api_upload_geofences_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_geofences_request** | [**UploadGeofencesRequest**](UploadGeofencesRequest.md)|  | 

### Return type

[**AsyncUploadGeofencesResponse**](AsyncUploadGeofencesResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**501** | Not Implemented |  -  |
**502** | Bad Gateway |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

