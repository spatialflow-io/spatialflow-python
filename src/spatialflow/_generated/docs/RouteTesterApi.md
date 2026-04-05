# spatialflow_generated.RouteTesterApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_devices_api_route_tester_create_route_test**](RouteTesterApi.md#apps_devices_api_route_tester_create_route_test) | **POST** /api/v1/route-tester/test | Run route test
[**apps_devices_api_route_tester_get_route_test**](RouteTesterApi.md#apps_devices_api_route_tester_get_route_test) | **GET** /api/v1/route-tester/test/{test_id} | Get route test status/results


# **apps_devices_api_route_tester_create_route_test**
> RouteTestResultsOut apps_devices_api_route_tester_create_route_test(file)

Run route test

     Upload a GPX or CSV route file and test it against your geofences and workflows.      For small routes (≤500 points): Returns results immediately (200).     For large routes (>500 points): Returns pending status with test_id to poll (202).      Results include:     - Geofence events (enter, exit, dwell)     - Workflows that would trigger     - Payload previews for each action (secrets redacted)      No external actions are executed - this is preview only.     

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.route_test_results_out import RouteTestResultsOut
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
    api_instance = spatialflow_generated.RouteTesterApi(api_client)
    file = None # bytearray | 

    try:
        # Run route test
        api_response = await api_instance.apps_devices_api_route_tester_create_route_test(file)
        print("The response of RouteTesterApi->apps_devices_api_route_tester_create_route_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteTesterApi->apps_devices_api_route_tester_create_route_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 

### Return type

[**RouteTestResultsOut**](RouteTestResultsOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_route_tester_get_route_test**
> RouteTestStatusOut apps_devices_api_route_tester_get_route_test(test_id)

Get route test status/results

Get the status or results of a route test. For async tests, poll this endpoint.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.route_test_status_out import RouteTestStatusOut
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
    api_instance = spatialflow_generated.RouteTesterApi(api_client)
    test_id = 'test_id_example' # str | 

    try:
        # Get route test status/results
        api_response = await api_instance.apps_devices_api_route_tester_get_route_test(test_id)
        print("The response of RouteTesterApi->apps_devices_api_route_tester_get_route_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteTesterApi->apps_devices_api_route_tester_get_route_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_id** | **str**|  | 

### Return type

[**RouteTestStatusOut**](RouteTestStatusOut.md)

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
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

