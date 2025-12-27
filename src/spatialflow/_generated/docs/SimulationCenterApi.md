# spatialflow_generated.SimulationCenterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_devices_api_simulation_create_simulation**](SimulationCenterApi.md#apps_devices_api_simulation_create_simulation) | **POST** /api/v1/simulations | Create Simulation
[**apps_devices_api_simulation_delete_simulation**](SimulationCenterApi.md#apps_devices_api_simulation_delete_simulation) | **DELETE** /api/v1/simulations/{simulation_id} | Delete Simulation
[**apps_devices_api_simulation_get_route_track_points**](SimulationCenterApi.md#apps_devices_api_simulation_get_route_track_points) | **GET** /api/v1/simulations/{simulation_id}/routes/{route_id}/track-points | Get Route Track Points
[**apps_devices_api_simulation_get_simulation**](SimulationCenterApi.md#apps_devices_api_simulation_get_simulation) | **GET** /api/v1/simulations/{simulation_id} | Get Simulation
[**apps_devices_api_simulation_list_simulation_events**](SimulationCenterApi.md#apps_devices_api_simulation_list_simulation_events) | **GET** /api/v1/simulations/{simulation_id}/events | List Simulation Events
[**apps_devices_api_simulation_list_simulations**](SimulationCenterApi.md#apps_devices_api_simulation_list_simulations) | **GET** /api/v1/simulations | List Simulations
[**apps_devices_api_simulation_pause_simulation**](SimulationCenterApi.md#apps_devices_api_simulation_pause_simulation) | **POST** /api/v1/simulations/{simulation_id}/pause | Pause Simulation
[**apps_devices_api_simulation_remove_route**](SimulationCenterApi.md#apps_devices_api_simulation_remove_route) | **DELETE** /api/v1/simulations/{simulation_id}/routes/{route_id} | Remove Route
[**apps_devices_api_simulation_reset_simulation**](SimulationCenterApi.md#apps_devices_api_simulation_reset_simulation) | **POST** /api/v1/simulations/{simulation_id}/reset | Reset Simulation
[**apps_devices_api_simulation_resume_simulation**](SimulationCenterApi.md#apps_devices_api_simulation_resume_simulation) | **POST** /api/v1/simulations/{simulation_id}/resume | Resume Simulation
[**apps_devices_api_simulation_start_simulation**](SimulationCenterApi.md#apps_devices_api_simulation_start_simulation) | **POST** /api/v1/simulations/{simulation_id}/start | Start Simulation
[**apps_devices_api_simulation_stop_simulation**](SimulationCenterApi.md#apps_devices_api_simulation_stop_simulation) | **POST** /api/v1/simulations/{simulation_id}/stop | Stop Simulation
[**apps_devices_api_simulation_update_simulation**](SimulationCenterApi.md#apps_devices_api_simulation_update_simulation) | **PATCH** /api/v1/simulations/{simulation_id} | Update Simulation
[**apps_devices_api_simulation_upload_csv_route**](SimulationCenterApi.md#apps_devices_api_simulation_upload_csv_route) | **POST** /api/v1/simulations/{simulation_id}/routes/upload-csv | Upload Csv Route
[**apps_devices_api_simulation_upload_gpx_route**](SimulationCenterApi.md#apps_devices_api_simulation_upload_gpx_route) | **POST** /api/v1/simulations/{simulation_id}/routes/upload-gpx | Upload Gpx Route


# **apps_devices_api_simulation_create_simulation**
> SimulationOut apps_devices_api_simulation_create_simulation(create_simulation_request)

Create Simulation

Create a new simulation session.

Simulations start in 'draft' status. Add routes, then start the simulation.

Returns:
    201: Created simulation
    400: Invalid request
    401: Unauthorized

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.create_simulation_request import CreateSimulationRequest
from spatialflow_generated.models.simulation_out import SimulationOut
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    create_simulation_request = spatialflow_generated.CreateSimulationRequest() # CreateSimulationRequest | 

    try:
        # Create Simulation
        api_response = await api_instance.apps_devices_api_simulation_create_simulation(create_simulation_request)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_create_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_create_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_simulation_request** | [**CreateSimulationRequest**](CreateSimulationRequest.md)|  | 

### Return type

[**SimulationOut**](SimulationOut.md)

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

# **apps_devices_api_simulation_delete_simulation**
> Dict[str, object] apps_devices_api_simulation_delete_simulation(simulation_id)

Delete Simulation

Delete a simulation and all associated data.

Running simulations will be cancelled first.

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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Simulation
        api_response = await api_instance.apps_devices_api_simulation_delete_simulation(simulation_id)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_delete_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_delete_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 

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

# **apps_devices_api_simulation_get_route_track_points**
> RouteTrackPointsOut apps_devices_api_simulation_get_route_track_points(simulation_id, route_id)

Get Route Track Points

Get track points for a simulation route.

Returns the full list of coordinates for drawing the route on a map.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.route_track_points_out import RouteTrackPointsOut
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    route_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Route Track Points
        api_response = await api_instance.apps_devices_api_simulation_get_route_track_points(simulation_id, route_id)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_get_route_track_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_get_route_track_points: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 
 **route_id** | **UUID**|  | 

### Return type

[**RouteTrackPointsOut**](RouteTrackPointsOut.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_simulation_get_simulation**
> SimulationDetailOut apps_devices_api_simulation_get_simulation(simulation_id)

Get Simulation

Get detailed simulation info including routes and recent events.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.simulation_detail_out import SimulationDetailOut
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Simulation
        api_response = await api_instance.apps_devices_api_simulation_get_simulation(simulation_id)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_get_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_get_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 

### Return type

[**SimulationDetailOut**](SimulationDetailOut.md)

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

# **apps_devices_api_simulation_list_simulation_events**
> List[SimulationEventOut] apps_devices_api_simulation_list_simulation_events(simulation_id, event_type=event_type, limit=limit, offset=offset)

List Simulation Events

List events from a simulation.

Args:
    event_type: Optional filter by event type
    limit: Maximum number of results
    offset: Pagination offset

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.simulation_event_out import SimulationEventOut
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    event_type = 'event_type_example' # str |  (optional)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Simulation Events
        api_response = await api_instance.apps_devices_api_simulation_list_simulation_events(simulation_id, event_type=event_type, limit=limit, offset=offset)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_list_simulation_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_list_simulation_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 
 **event_type** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[SimulationEventOut]**](SimulationEventOut.md)

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

# **apps_devices_api_simulation_list_simulations**
> List[SimulationOut] apps_devices_api_simulation_list_simulations(status=status, limit=limit, offset=offset)

List Simulations

List simulations for the authenticated user.

Args:
    status: Optional filter by status
    limit: Maximum number of results
    offset: Pagination offset

Returns:
    List of simulations

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.simulation_out import SimulationOut
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    status = 'status_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Simulations
        api_response = await api_instance.apps_devices_api_simulation_list_simulations(status=status, limit=limit, offset=offset)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_list_simulations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_list_simulations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[SimulationOut]**](SimulationOut.md)

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

# **apps_devices_api_simulation_pause_simulation**
> SimulationOut apps_devices_api_simulation_pause_simulation(simulation_id)

Pause Simulation

Pause simulation playback.

All routes will stop at their current point and can be resumed.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.simulation_out import SimulationOut
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Pause Simulation
        api_response = await api_instance.apps_devices_api_simulation_pause_simulation(simulation_id)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_pause_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_pause_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 

### Return type

[**SimulationOut**](SimulationOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_simulation_remove_route**
> Dict[str, object] apps_devices_api_simulation_remove_route(simulation_id, route_id)

Remove Route

Remove a route from the simulation.

Can only remove routes when simulation is in 'draft' or 'ready' state.

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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    route_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Remove Route
        api_response = await api_instance.apps_devices_api_simulation_remove_route(simulation_id, route_id)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_remove_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_remove_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 
 **route_id** | **UUID**|  | 

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_simulation_reset_simulation**
> SimulationOut apps_devices_api_simulation_reset_simulation(simulation_id)

Reset Simulation

Reset a completed/cancelled/failed simulation to 'ready' state.

Clears all events and resets route progress.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.simulation_out import SimulationOut
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Reset Simulation
        api_response = await api_instance.apps_devices_api_simulation_reset_simulation(simulation_id)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_reset_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_reset_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 

### Return type

[**SimulationOut**](SimulationOut.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_simulation_resume_simulation**
> SimulationOut apps_devices_api_simulation_resume_simulation(simulation_id)

Resume Simulation

Resume a paused simulation.

Routes continue from their checkpointed positions.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.simulation_out import SimulationOut
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Resume Simulation
        api_response = await api_instance.apps_devices_api_simulation_resume_simulation(simulation_id)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_resume_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_resume_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 

### Return type

[**SimulationOut**](SimulationOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_simulation_start_simulation**
> SimulationOut apps_devices_api_simulation_start_simulation(simulation_id)

Start Simulation

Start simulation playback.

Creates transient devices and queues Celery tasks for each route.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.simulation_out import SimulationOut
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Start Simulation
        api_response = await api_instance.apps_devices_api_simulation_start_simulation(simulation_id)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_start_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_start_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 

### Return type

[**SimulationOut**](SimulationOut.md)

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
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_simulation_stop_simulation**
> SimulationOut apps_devices_api_simulation_stop_simulation(simulation_id)

Stop Simulation

Stop simulation and reset all routes.

Running tasks will be cancelled. Routes are reset to start positions.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.simulation_out import SimulationOut
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Stop Simulation
        api_response = await api_instance.apps_devices_api_simulation_stop_simulation(simulation_id)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_stop_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_stop_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 

### Return type

[**SimulationOut**](SimulationOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_simulation_update_simulation**
> SimulationOut apps_devices_api_simulation_update_simulation(simulation_id, update_simulation_request)

Update Simulation

Update simulation settings.

Can only update simulations in 'draft' or 'ready' state.
Speed multiplier can be updated during 'running' state.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.simulation_out import SimulationOut
from spatialflow_generated.models.update_simulation_request import UpdateSimulationRequest
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_simulation_request = spatialflow_generated.UpdateSimulationRequest() # UpdateSimulationRequest | 

    try:
        # Update Simulation
        api_response = await api_instance.apps_devices_api_simulation_update_simulation(simulation_id, update_simulation_request)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_update_simulation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_update_simulation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 
 **update_simulation_request** | [**UpdateSimulationRequest**](UpdateSimulationRequest.md)|  | 

### Return type

[**SimulationOut**](SimulationOut.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_simulation_upload_csv_route**
> RouteUploadResponse apps_devices_api_simulation_upload_csv_route(simulation_id, file, simulated_device_name=simulated_device_name, simulated_device_type=simulated_device_type)

Upload Csv Route

Upload a CSV time-series file and add it as a route to the simulation.

CSV must have columns: latitude, longitude, timestamp
Optional columns: elevation, speed, heading

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.route_upload_response import RouteUploadResponse
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    file = None # bytearray | 
    simulated_device_name = '' # str |  (optional) (default to '')
    simulated_device_type = 'simulation' # str |  (optional) (default to 'simulation')

    try:
        # Upload Csv Route
        api_response = await api_instance.apps_devices_api_simulation_upload_csv_route(simulation_id, file, simulated_device_name=simulated_device_name, simulated_device_type=simulated_device_type)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_upload_csv_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_upload_csv_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 
 **file** | **bytearray**|  | 
 **simulated_device_name** | **str**|  | [optional] [default to &#39;&#39;]
 **simulated_device_type** | **str**|  | [optional] [default to &#39;simulation&#39;]

### Return type

[**RouteUploadResponse**](RouteUploadResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_simulation_upload_gpx_route**
> RouteUploadResponse apps_devices_api_simulation_upload_gpx_route(simulation_id, file, simulated_device_name=simulated_device_name, simulated_device_type=simulated_device_type)

Upload Gpx Route

Upload a GPX file and add it as a route to the simulation.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.route_upload_response import RouteUploadResponse
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
    api_instance = spatialflow_generated.SimulationCenterApi(api_client)
    simulation_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    file = None # bytearray | 
    simulated_device_name = '' # str |  (optional) (default to '')
    simulated_device_type = 'simulation' # str |  (optional) (default to 'simulation')

    try:
        # Upload Gpx Route
        api_response = await api_instance.apps_devices_api_simulation_upload_gpx_route(simulation_id, file, simulated_device_name=simulated_device_name, simulated_device_type=simulated_device_type)
        print("The response of SimulationCenterApi->apps_devices_api_simulation_upload_gpx_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimulationCenterApi->apps_devices_api_simulation_upload_gpx_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **UUID**|  | 
 **file** | **bytearray**|  | 
 **simulated_device_name** | **str**|  | [optional] [default to &#39;&#39;]
 **simulated_device_type** | **str**|  | [optional] [default to &#39;simulation&#39;]

### Return type

[**RouteUploadResponse**](RouteUploadResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

