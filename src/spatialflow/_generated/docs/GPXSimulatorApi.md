# spatialflow_generated.GPXSimulatorApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_devices_api_gpx_cancel_gpx_playback**](GPXSimulatorApi.md#apps_devices_api_gpx_cancel_gpx_playback) | **POST** /api/v1/gpx/playbacks/{playback_id}/cancel | Cancel Gpx Playback
[**apps_devices_api_gpx_delete_gpx_route**](GPXSimulatorApi.md#apps_devices_api_gpx_delete_gpx_route) | **DELETE** /api/v1/gpx/routes/{route_id} | Delete Gpx Route
[**apps_devices_api_gpx_get_gpx_playback**](GPXSimulatorApi.md#apps_devices_api_gpx_get_gpx_playback) | **GET** /api/v1/gpx/playbacks/{playback_id} | Get Gpx Playback
[**apps_devices_api_gpx_get_gpx_route**](GPXSimulatorApi.md#apps_devices_api_gpx_get_gpx_route) | **GET** /api/v1/gpx/routes/{route_id} | Get Gpx Route
[**apps_devices_api_gpx_list_gpx_playbacks**](GPXSimulatorApi.md#apps_devices_api_gpx_list_gpx_playbacks) | **GET** /api/v1/gpx/playbacks | List Gpx Playbacks
[**apps_devices_api_gpx_list_gpx_routes**](GPXSimulatorApi.md#apps_devices_api_gpx_list_gpx_routes) | **GET** /api/v1/gpx/routes | List Gpx Routes
[**apps_devices_api_gpx_pause_gpx_playback**](GPXSimulatorApi.md#apps_devices_api_gpx_pause_gpx_playback) | **POST** /api/v1/gpx/playbacks/{playback_id}/pause | Pause Gpx Playback
[**apps_devices_api_gpx_resume_gpx_playback**](GPXSimulatorApi.md#apps_devices_api_gpx_resume_gpx_playback) | **POST** /api/v1/gpx/playbacks/{playback_id}/resume | Resume Gpx Playback
[**apps_devices_api_gpx_start_gpx_playback**](GPXSimulatorApi.md#apps_devices_api_gpx_start_gpx_playback) | **POST** /api/v1/gpx/routes/{route_id}/playback | Start Gpx Playback
[**apps_devices_api_gpx_upload_gpx_route**](GPXSimulatorApi.md#apps_devices_api_gpx_upload_gpx_route) | **POST** /api/v1/gpx/routes/upload | Upload Gpx Route


# **apps_devices_api_gpx_cancel_gpx_playback**
> Dict[str, object] apps_devices_api_gpx_cancel_gpx_playback(playback_id)

Cancel Gpx Playback

Cancel an active or paused playback.  The playback cannot be resumed after cancellation.

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
    api_instance = spatialflow_generated.GPXSimulatorApi(api_client)
    playback_id = 'playback_id_example' # str | 

    try:
        # Cancel Gpx Playback
        api_response = await api_instance.apps_devices_api_gpx_cancel_gpx_playback(playback_id)
        print("The response of GPXSimulatorApi->apps_devices_api_gpx_cancel_gpx_playback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPXSimulatorApi->apps_devices_api_gpx_cancel_gpx_playback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**|  | 

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

# **apps_devices_api_gpx_delete_gpx_route**
> Dict[str, object] apps_devices_api_gpx_delete_gpx_route(route_id)

Delete Gpx Route

Delete (deactivate) a GPX route.

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
    api_instance = spatialflow_generated.GPXSimulatorApi(api_client)
    route_id = 'route_id_example' # str | 

    try:
        # Delete Gpx Route
        api_response = await api_instance.apps_devices_api_gpx_delete_gpx_route(route_id)
        print("The response of GPXSimulatorApi->apps_devices_api_gpx_delete_gpx_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPXSimulatorApi->apps_devices_api_gpx_delete_gpx_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **str**|  | 

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

# **apps_devices_api_gpx_get_gpx_playback**
> GPXPlaybackOut apps_devices_api_gpx_get_gpx_playback(playback_id)

Get Gpx Playback

Get details of a specific playback session.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.gpx_playback_out import GPXPlaybackOut
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
    api_instance = spatialflow_generated.GPXSimulatorApi(api_client)
    playback_id = 'playback_id_example' # str | 

    try:
        # Get Gpx Playback
        api_response = await api_instance.apps_devices_api_gpx_get_gpx_playback(playback_id)
        print("The response of GPXSimulatorApi->apps_devices_api_gpx_get_gpx_playback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPXSimulatorApi->apps_devices_api_gpx_get_gpx_playback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**|  | 

### Return type

[**GPXPlaybackOut**](GPXPlaybackOut.md)

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

# **apps_devices_api_gpx_get_gpx_route**
> GPXRouteOut apps_devices_api_gpx_get_gpx_route(route_id)

Get Gpx Route

Get details of a specific GPX route.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.gpx_route_out import GPXRouteOut
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
    api_instance = spatialflow_generated.GPXSimulatorApi(api_client)
    route_id = 'route_id_example' # str | 

    try:
        # Get Gpx Route
        api_response = await api_instance.apps_devices_api_gpx_get_gpx_route(route_id)
        print("The response of GPXSimulatorApi->apps_devices_api_gpx_get_gpx_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPXSimulatorApi->apps_devices_api_gpx_get_gpx_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **str**|  | 

### Return type

[**GPXRouteOut**](GPXRouteOut.md)

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

# **apps_devices_api_gpx_list_gpx_playbacks**
> List[GPXPlaybackOut] apps_devices_api_gpx_list_gpx_playbacks(status=status, limit=limit, offset=offset)

List Gpx Playbacks

List GPX playback sessions.  Args:     status: Optional filter by status (running, paused, completed, cancelled, failed)     limit: Maximum number of results     offset: Pagination offset  Returns:     List of playback sessions

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.gpx_playback_out import GPXPlaybackOut
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
    api_instance = spatialflow_generated.GPXSimulatorApi(api_client)
    status = 'status_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Gpx Playbacks
        api_response = await api_instance.apps_devices_api_gpx_list_gpx_playbacks(status=status, limit=limit, offset=offset)
        print("The response of GPXSimulatorApi->apps_devices_api_gpx_list_gpx_playbacks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPXSimulatorApi->apps_devices_api_gpx_list_gpx_playbacks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[GPXPlaybackOut]**](GPXPlaybackOut.md)

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

# **apps_devices_api_gpx_list_gpx_routes**
> List[GPXRouteOut] apps_devices_api_gpx_list_gpx_routes(device_id=device_id, limit=limit, offset=offset)

List Gpx Routes

List GPX routes for the authenticated user.  Args:     device_id: Optional filter by device     limit: Maximum number of results     offset: Pagination offset  Returns:     List of GPX routes

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.gpx_route_out import GPXRouteOut
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
    api_instance = spatialflow_generated.GPXSimulatorApi(api_client)
    device_id = 'device_id_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Gpx Routes
        api_response = await api_instance.apps_devices_api_gpx_list_gpx_routes(device_id=device_id, limit=limit, offset=offset)
        print("The response of GPXSimulatorApi->apps_devices_api_gpx_list_gpx_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPXSimulatorApi->apps_devices_api_gpx_list_gpx_routes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[GPXRouteOut]**](GPXRouteOut.md)

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

# **apps_devices_api_gpx_pause_gpx_playback**
> GPXPlaybackOut apps_devices_api_gpx_pause_gpx_playback(playback_id)

Pause Gpx Playback

Pause an active playback.  The playback will stop at the current point and can be resumed later.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.gpx_playback_out import GPXPlaybackOut
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
    api_instance = spatialflow_generated.GPXSimulatorApi(api_client)
    playback_id = 'playback_id_example' # str | 

    try:
        # Pause Gpx Playback
        api_response = await api_instance.apps_devices_api_gpx_pause_gpx_playback(playback_id)
        print("The response of GPXSimulatorApi->apps_devices_api_gpx_pause_gpx_playback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPXSimulatorApi->apps_devices_api_gpx_pause_gpx_playback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**|  | 

### Return type

[**GPXPlaybackOut**](GPXPlaybackOut.md)

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

# **apps_devices_api_gpx_resume_gpx_playback**
> GPXPlaybackOut apps_devices_api_gpx_resume_gpx_playback(playback_id)

Resume Gpx Playback

Resume a paused playback.  Continues from the point where it was paused.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.gpx_playback_out import GPXPlaybackOut
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
    api_instance = spatialflow_generated.GPXSimulatorApi(api_client)
    playback_id = 'playback_id_example' # str | 

    try:
        # Resume Gpx Playback
        api_response = await api_instance.apps_devices_api_gpx_resume_gpx_playback(playback_id)
        print("The response of GPXSimulatorApi->apps_devices_api_gpx_resume_gpx_playback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPXSimulatorApi->apps_devices_api_gpx_resume_gpx_playback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**|  | 

### Return type

[**GPXPlaybackOut**](GPXPlaybackOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_gpx_start_gpx_playback**
> GPXPlaybackOut apps_devices_api_gpx_start_gpx_playback(route_id, start_playback_request)

Start Gpx Playback

Start playback of a GPX route.  Creates a playback session and starts the Celery task to simulate device movement along the route.  Args:     route_id: ID of the route to play     data: Playback configuration (speed, loop)  Returns:     201: Created playback session     400: Invalid request or playback already active     404: Route not found

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.gpx_playback_out import GPXPlaybackOut
from spatialflow_generated.models.start_playback_request import StartPlaybackRequest
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
    api_instance = spatialflow_generated.GPXSimulatorApi(api_client)
    route_id = 'route_id_example' # str | 
    start_playback_request = spatialflow_generated.StartPlaybackRequest() # StartPlaybackRequest | 

    try:
        # Start Gpx Playback
        api_response = await api_instance.apps_devices_api_gpx_start_gpx_playback(route_id, start_playback_request)
        print("The response of GPXSimulatorApi->apps_devices_api_gpx_start_gpx_playback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPXSimulatorApi->apps_devices_api_gpx_start_gpx_playback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **str**|  | 
 **start_playback_request** | [**StartPlaybackRequest**](StartPlaybackRequest.md)|  | 

### Return type

[**GPXPlaybackOut**](GPXPlaybackOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_gpx_upload_gpx_route**
> GPXRouteOut apps_devices_api_gpx_upload_gpx_route(device_id, name, file, description=description)

Upload Gpx Route

Upload and parse a GPX file to create a new route.  The GPX file is parsed, validated, and stored in S3. Track points are extracted and saved for efficient playback.  Args:     device_id: Device to associate with this route     name: Name for the route     file: GPX file upload     description: Optional route description  Returns:     201: Created route details     400: Invalid GPX file or device     401: Unauthorized

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.gpx_route_out import GPXRouteOut
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
    api_instance = spatialflow_generated.GPXSimulatorApi(api_client)
    device_id = 'device_id_example' # str | 
    name = 'name_example' # str | 
    file = None # bytearray | 
    description = '' # str |  (optional) (default to '')

    try:
        # Upload Gpx Route
        api_response = await api_instance.apps_devices_api_gpx_upload_gpx_route(device_id, name, file, description=description)
        print("The response of GPXSimulatorApi->apps_devices_api_gpx_upload_gpx_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GPXSimulatorApi->apps_devices_api_gpx_upload_gpx_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | 
 **name** | **str**|  | 
 **file** | **bytearray**|  | 
 **description** | **str**|  | [optional] [default to &#39;&#39;]

### Return type

[**GPXRouteOut**](GPXRouteOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

