# spatialflow_generated.SignalsApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_devices_api_signals_get_signal**](SignalsApi.md#apps_devices_api_signals_get_signal) | **GET** /api/v1/signals/{signal_id} | Get signal event detail
[**apps_devices_api_signals_list_signals**](SignalsApi.md#apps_devices_api_signals_list_signals) | **GET** /api/v1/signals/ | List signal events


# **apps_devices_api_signals_get_signal**
> SignalEventDetailOut apps_devices_api_signals_get_signal(signal_id)

Get signal event detail

Retrieve a single signal event with contributing locations and geofence geometry.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.signal_event_detail_out import SignalEventDetailOut
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
    api_instance = spatialflow_generated.SignalsApi(api_client)
    signal_id = 'signal_id_example' # str | 

    try:
        # Get signal event detail
        api_response = await api_instance.apps_devices_api_signals_get_signal(signal_id)
        print("The response of SignalsApi->apps_devices_api_signals_get_signal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignalsApi->apps_devices_api_signals_get_signal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_id** | **str**|  | 

### Return type

[**SignalEventDetailOut**](SignalEventDetailOut.md)

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

# **apps_devices_api_signals_list_signals**
> SignalEventsListOut apps_devices_api_signals_list_signals(signal_type=signal_type, state=state, device_id=device_id, geofence_id=geofence_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

List signal events

List signal events for the authenticated user's workspace with optional filtering.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.signal_events_list_out import SignalEventsListOut
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
    api_instance = spatialflow_generated.SignalsApi(api_client)
    signal_type = 'signal_type_example' # str |  (optional)
    state = 'state_example' # str |  (optional)
    device_id = 'device_id_example' # str |  (optional)
    geofence_id = 'geofence_id_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List signal events
        api_response = await api_instance.apps_devices_api_signals_list_signals(signal_type=signal_type, state=state, device_id=device_id, geofence_id=geofence_id, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of SignalsApi->apps_devices_api_signals_list_signals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SignalsApi->apps_devices_api_signals_list_signals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signal_type** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **geofence_id** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**SignalEventsListOut**](SignalEventsListOut.md)

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

