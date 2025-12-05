# spatialflow_generated.PublicApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_public_api_get_api_docs**](PublicApi.md#apps_public_api_get_api_docs) | **GET** /api/v1/public/docs | Get Api Docs
[**apps_public_api_get_websocket_routes**](PublicApi.md#apps_public_api_get_websocket_routes) | **GET** /api/v1/public/websocket-routes | Get Websocket Routes
[**apps_public_api_health_check**](PublicApi.md#apps_public_api_health_check) | **GET** /api/v1/public/health | Health Check
[**apps_public_api_signup**](PublicApi.md#apps_public_api_signup) | **POST** /api/v1/public/signup | Signup
[**apps_public_api_status**](PublicApi.md#apps_public_api_status) | **GET** /api/v1/public/status | Status
[**apps_public_api_swagger_ui**](PublicApi.md#apps_public_api_swagger_ui) | **GET** /api/v1/public/docs/ui | Swagger Ui


# **apps_public_api_get_api_docs**
> apps_public_api_get_api_docs()

Get Api Docs

Returns the complete OpenAPI 3.0 specification

### Example


```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.PublicApi(api_client)

    try:
        # Get Api Docs
        await api_instance.apps_public_api_get_api_docs()
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_get_api_docs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_public_api_get_websocket_routes**
> apps_public_api_get_websocket_routes()

Get Websocket Routes

Returns documentation for all available WebSocket endpoints.  This endpoint helps developers discover and understand the WebSocket routes available in the SpatialFlow API.

### Example


```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.PublicApi(api_client)

    try:
        # Get Websocket Routes
        await api_instance.apps_public_api_get_websocket_routes()
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_get_websocket_routes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_public_api_health_check**
> apps_public_api_health_check()

Health Check

Health check endpoint for public service

### Example


```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.PublicApi(api_client)

    try:
        # Health Check
        await api_instance.apps_public_api_health_check()
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_public_api_signup**
> Dict[str, object] apps_public_api_signup(signup_request)

Signup

Register for SpatialFlow.io

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.signup_request import SignupRequest
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.PublicApi(api_client)
    signup_request = spatialflow_generated.SignupRequest() # SignupRequest | 

    try:
        # Signup
        api_response = await api_instance.apps_public_api_signup(signup_request)
        print("The response of PublicApi->apps_public_api_signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_signup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_request** | [**SignupRequest**](SignupRequest.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_public_api_status**
> apps_public_api_status()

Status

Public status endpoint with beta program information.

### Example


```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.PublicApi(api_client)

    try:
        # Status
        await api_instance.apps_public_api_status()
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_public_api_swagger_ui**
> apps_public_api_swagger_ui()

Swagger Ui

Interactive Swagger UI for exploring and testing the API  Note: In production, this would serve an HTML page with Swagger UI. For now, returning a redirect to the docs endpoint.

### Example


```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.PublicApi(api_client)

    try:
        # Swagger Ui
        await api_instance.apps_public_api_swagger_ui()
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_swagger_ui: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

