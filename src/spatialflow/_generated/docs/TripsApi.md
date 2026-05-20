# spatialflow_generated.TripsApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_devices_api_trips_cancel_trip**](TripsApi.md#apps_devices_api_trips_cancel_trip) | **POST** /api/v1/trips/{trip_id}/cancel | Cancel a planned trip
[**apps_devices_api_trips_create_trip**](TripsApi.md#apps_devices_api_trips_create_trip) | **POST** /api/v1/trips/ | Create a planned trip
[**apps_devices_api_trips_get_trip**](TripsApi.md#apps_devices_api_trips_get_trip) | **GET** /api/v1/trips/{trip_id} | Get trip detail
[**apps_devices_api_trips_list_trips**](TripsApi.md#apps_devices_api_trips_list_trips) | **GET** /api/v1/trips/ | List trips
[**apps_devices_api_trips_update_trip**](TripsApi.md#apps_devices_api_trips_update_trip) | **PUT** /api/v1/trips/{trip_id} | Update a trip


# **apps_devices_api_trips_cancel_trip**
> TripOut apps_devices_api_trips_cancel_trip(trip_id)

Cancel a planned trip

Cancel a planned trip. Only trips with status 'planned' can be cancelled.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.trip_out import TripOut
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
    api_instance = spatialflow_generated.TripsApi(api_client)
    trip_id = 'trip_id_example' # str | 

    try:
        # Cancel a planned trip
        api_response = await api_instance.apps_devices_api_trips_cancel_trip(trip_id)
        print("The response of TripsApi->apps_devices_api_trips_cancel_trip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TripsApi->apps_devices_api_trips_cancel_trip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trip_id** | **str**|  | 

### Return type

[**TripOut**](TripOut.md)

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

# **apps_devices_api_trips_create_trip**
> TripOut apps_devices_api_trips_create_trip(trip_create_in)

Create a planned trip

Create a new planned trip for a device with an optional route.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.trip_create_in import TripCreateIn
from spatialflow_generated.models.trip_out import TripOut
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
    api_instance = spatialflow_generated.TripsApi(api_client)
    trip_create_in = spatialflow_generated.TripCreateIn() # TripCreateIn | 

    try:
        # Create a planned trip
        api_response = await api_instance.apps_devices_api_trips_create_trip(trip_create_in)
        print("The response of TripsApi->apps_devices_api_trips_create_trip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TripsApi->apps_devices_api_trips_create_trip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trip_create_in** | [**TripCreateIn**](TripCreateIn.md)|  | 

### Return type

[**TripOut**](TripOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_trips_get_trip**
> TripDetailOut apps_devices_api_trips_get_trip(trip_id)

Get trip detail

Retrieve a single trip with planned route and track geometry.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.trip_detail_out import TripDetailOut
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
    api_instance = spatialflow_generated.TripsApi(api_client)
    trip_id = 'trip_id_example' # str | 

    try:
        # Get trip detail
        api_response = await api_instance.apps_devices_api_trips_get_trip(trip_id)
        print("The response of TripsApi->apps_devices_api_trips_get_trip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TripsApi->apps_devices_api_trips_get_trip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trip_id** | **str**|  | 

### Return type

[**TripDetailOut**](TripDetailOut.md)

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

# **apps_devices_api_trips_list_trips**
> TripsListOut apps_devices_api_trips_list_trips(device_id=device_id, status=status, start_date=start_date, end_date=end_date, limit=limit, offset=offset)

List trips

List trips for the authenticated user's workspace with optional filtering.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.trips_list_out import TripsListOut
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
    api_instance = spatialflow_generated.TripsApi(api_client)
    device_id = 'device_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List trips
        api_response = await api_instance.apps_devices_api_trips_list_trips(device_id=device_id, status=status, start_date=start_date, end_date=end_date, limit=limit, offset=offset)
        print("The response of TripsApi->apps_devices_api_trips_list_trips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TripsApi->apps_devices_api_trips_list_trips: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**TripsListOut**](TripsListOut.md)

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

# **apps_devices_api_trips_update_trip**
> TripOut apps_devices_api_trips_update_trip(trip_id, trip_update_in)

Update a trip

Update a trip's name, planned route, or metadata.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.trip_out import TripOut
from spatialflow_generated.models.trip_update_in import TripUpdateIn
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
    api_instance = spatialflow_generated.TripsApi(api_client)
    trip_id = 'trip_id_example' # str | 
    trip_update_in = spatialflow_generated.TripUpdateIn() # TripUpdateIn | 

    try:
        # Update a trip
        api_response = await api_instance.apps_devices_api_trips_update_trip(trip_id, trip_update_in)
        print("The response of TripsApi->apps_devices_api_trips_update_trip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TripsApi->apps_devices_api_trips_update_trip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trip_id** | **str**|  | 
 **trip_update_in** | [**TripUpdateIn**](TripUpdateIn.md)|  | 

### Return type

[**TripOut**](TripOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

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

