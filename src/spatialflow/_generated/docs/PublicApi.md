# spatialflow_generated.PublicApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_public_api_contact_sales**](PublicApi.md#apps_public_api_contact_sales) | **POST** /api/v1/public/contact | Contact Sales
[**apps_public_api_get_api_docs**](PublicApi.md#apps_public_api_get_api_docs) | **GET** /api/v1/public/docs | Get Api Docs
[**apps_public_api_get_websocket_routes**](PublicApi.md#apps_public_api_get_websocket_routes) | **GET** /api/v1/public/websocket-routes | Get Websocket Routes
[**apps_public_api_health_check**](PublicApi.md#apps_public_api_health_check) | **GET** /api/v1/public/health | Health Check
[**apps_public_api_runtime_config**](PublicApi.md#apps_public_api_runtime_config) | **GET** /api/v1/public/runtime-config | Runtime Config
[**apps_public_api_signup**](PublicApi.md#apps_public_api_signup) | **POST** /api/v1/public/signup | Signup
[**apps_public_api_status**](PublicApi.md#apps_public_api_status) | **GET** /api/v1/public/status | Status
[**apps_public_api_swagger_ui**](PublicApi.md#apps_public_api_swagger_ui) | **GET** /api/v1/public/docs/ui | Swagger Ui


# **apps_public_api_contact_sales**
> Dict[str, object] apps_public_api_contact_sales(contact_request)

Contact Sales

Submit a contact/sales inquiry.  Sends an internal notification to the sales team and a confirmation auto-reply to the submitter. Stateless - no database writes.  Rate limited: 10/hour per IP, 3/hour per email.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.contact_request import ContactRequest
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
    contact_request = spatialflow_generated.ContactRequest() # ContactRequest | 

    try:
        # Contact Sales
        api_response = await api_instance.apps_public_api_contact_sales(contact_request)
        print("The response of PublicApi->apps_public_api_contact_sales:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_contact_sales: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_request** | [**ContactRequest**](ContactRequest.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_public_api_get_api_docs**
> ApiDocsOut apps_public_api_get_api_docs()

Get Api Docs

Returns the complete OpenAPI 3.0 specification

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.api_docs_out import ApiDocsOut
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
        api_response = await api_instance.apps_public_api_get_api_docs()
        print("The response of PublicApi->apps_public_api_get_api_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_get_api_docs: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiDocsOut**](ApiDocsOut.md)

### Authorization

No authorization required

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

# **apps_public_api_get_websocket_routes**
> WebSocketRoutesOut apps_public_api_get_websocket_routes()

Get Websocket Routes

Returns documentation for all available WebSocket endpoints.  This endpoint helps developers discover and understand the WebSocket routes available in the SpatialFlow API.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.web_socket_routes_out import WebSocketRoutesOut
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
        api_response = await api_instance.apps_public_api_get_websocket_routes()
        print("The response of PublicApi->apps_public_api_get_websocket_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_get_websocket_routes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebSocketRoutesOut**](WebSocketRoutesOut.md)

### Authorization

No authorization required

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

# **apps_public_api_health_check**
> HealthOut apps_public_api_health_check()

Health Check

Health check endpoint for public service

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.health_out import HealthOut
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
        api_response = await api_instance.apps_public_api_health_check()
        print("The response of PublicApi->apps_public_api_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthOut**](HealthOut.md)

### Authorization

No authorization required

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

# **apps_public_api_runtime_config**
> RuntimeConfigOut apps_public_api_runtime_config()

Runtime Config

Get runtime configuration for frontend applications.  This endpoint provides dynamic configuration that was previously only available as build-time environment variables. Allows Admin UI to control feature toggles without requiring frontend rebuilds (Issue #119).  Response includes only safe-to-expose public configuration: - Feature toggles (Route Tester, admin approval) - Analytics configuration (enabled flag, host URL - NOT API keys)  Note: API keys and sensitive values are NEVER returned from this endpoint.  Rate limited: 120/minute per IP to prevent abuse while allowing frequent frontend polling (e.g., SPA init, tab reopens).  Caching: Response is cached for 30 seconds to reduce database lookups. ConfigurationService also has its own 5-minute cache layer.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.runtime_config_out import RuntimeConfigOut
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
        # Runtime Config
        api_response = await api_instance.apps_public_api_runtime_config()
        print("The response of PublicApi->apps_public_api_runtime_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_runtime_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RuntimeConfigOut**](RuntimeConfigOut.md)

### Authorization

No authorization required

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

# **apps_public_api_signup**
> Dict[str, object] apps_public_api_signup(signup_request)

Signup

Register for SpatialFlow.io  Rate limited: 10/hour per IP, 3/hour per email (Issue #67 security hardening).

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
**201** | Created |  -  |
**400** | Bad Request |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_public_api_status**
> StatusOut apps_public_api_status()

Status

Public status endpoint with admin approval information.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.status_out import StatusOut
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
        api_response = await api_instance.apps_public_api_status()
        print("The response of PublicApi->apps_public_api_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StatusOut**](StatusOut.md)

### Authorization

No authorization required

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

# **apps_public_api_swagger_ui**
> DocsUiOut apps_public_api_swagger_ui()

Swagger Ui

Interactive Swagger UI for exploring and testing the API  Note: In production, this would serve an HTML page with Swagger UI. For now, returning a redirect to the docs endpoint.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.docs_ui_out import DocsUiOut
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
        api_response = await api_instance.apps_public_api_swagger_ui()
        print("The response of PublicApi->apps_public_api_swagger_ui:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->apps_public_api_swagger_ui: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DocsUiOut**](DocsUiOut.md)

### Authorization

No authorization required

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

