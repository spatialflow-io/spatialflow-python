# spatialflow_generated.SystemApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_core_health_api_health_check**](SystemApi.md#apps_core_health_api_health_check) | **GET** /api/v1/health | Api Health Check
[**apps_core_health_api_health_check_ready**](SystemApi.md#apps_core_health_api_health_check_ready) | **GET** /api/v1/health/ready | Api Health Check Ready


# **apps_core_health_api_health_check**
> Dict[str, object] apps_core_health_api_health_check()

Api Health Check

Basic health check for API.

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
    api_instance = spatialflow_generated.SystemApi(api_client)

    try:
        # Api Health Check
        api_response = await api_instance.apps_core_health_api_health_check()
        print("The response of SystemApi->apps_core_health_api_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->apps_core_health_api_health_check: %s\n" % e)
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

# **apps_core_health_api_health_check_ready**
> Dict[str, object] apps_core_health_api_health_check_ready()

Api Health Check Ready

Readiness check for API with dependency checks.

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
    api_instance = spatialflow_generated.SystemApi(api_client)

    try:
        # Api Health Check Ready
        api_response = await api_instance.apps_core_health_api_health_check_ready()
        print("The response of SystemApi->apps_core_health_api_health_check_ready:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemApi->apps_core_health_api_health_check_ready: %s\n" % e)
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
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

