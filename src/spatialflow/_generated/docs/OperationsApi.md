# spatialflow_generated.OperationsApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_operations_api_acknowledge_incident**](OperationsApi.md#apps_operations_api_acknowledge_incident) | **POST** /api/v1/incidents/{incident_id}/ack | Acknowledge Incident
[**apps_operations_api_bulk_update_incidents**](OperationsApi.md#apps_operations_api_bulk_update_incidents) | **POST** /api/v1/incidents/bulk | Bulk Update Incidents
[**apps_operations_api_create_saved_view**](OperationsApi.md#apps_operations_api_create_saved_view) | **POST** /api/v1/saved-views/ | Create Saved View
[**apps_operations_api_delete_saved_view**](OperationsApi.md#apps_operations_api_delete_saved_view) | **DELETE** /api/v1/saved-views/{view_id} | Delete Saved View
[**apps_operations_api_get_incident**](OperationsApi.md#apps_operations_api_get_incident) | **GET** /api/v1/incidents/{incident_id} | Get Incident
[**apps_operations_api_get_overview**](OperationsApi.md#apps_operations_api_get_overview) | **GET** /api/v1/overview | Get Overview
[**apps_operations_api_list_incident_groups**](OperationsApi.md#apps_operations_api_list_incident_groups) | **GET** /api/v1/incidents/groups | List Incident Groups
[**apps_operations_api_list_incidents**](OperationsApi.md#apps_operations_api_list_incidents) | **GET** /api/v1/incidents/ | List Incidents
[**apps_operations_api_list_saved_views**](OperationsApi.md#apps_operations_api_list_saved_views) | **GET** /api/v1/saved-views/ | List Saved Views
[**apps_operations_api_mute_incident**](OperationsApi.md#apps_operations_api_mute_incident) | **POST** /api/v1/incidents/{incident_id}/mute | Mute Incident
[**apps_operations_api_resolve_incident**](OperationsApi.md#apps_operations_api_resolve_incident) | **POST** /api/v1/incidents/{incident_id}/resolve | Resolve Incident
[**apps_operations_api_stream_badges**](OperationsApi.md#apps_operations_api_stream_badges) | **GET** /api/v1/stream/badges | Stream Badges
[**apps_operations_api_update_saved_view**](OperationsApi.md#apps_operations_api_update_saved_view) | **PATCH** /api/v1/saved-views/{view_id} | Update Saved View


# **apps_operations_api_acknowledge_incident**
> IncidentOut apps_operations_api_acknowledge_incident(incident_id, incident_ack_in)

Acknowledge Incident

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.incident_ack_in import IncidentAckIn
from spatialflow_generated.models.incident_out import IncidentOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    incident_id = 'incident_id_example' # str | 
    incident_ack_in = spatialflow_generated.IncidentAckIn() # IncidentAckIn | 

    try:
        # Acknowledge Incident
        api_response = await api_instance.apps_operations_api_acknowledge_incident(incident_id, incident_ack_in)
        print("The response of OperationsApi->apps_operations_api_acknowledge_incident:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_acknowledge_incident: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**|  | 
 **incident_ack_in** | [**IncidentAckIn**](IncidentAckIn.md)|  | 

### Return type

[**IncidentOut**](IncidentOut.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_bulk_update_incidents**
> IncidentBulkOut apps_operations_api_bulk_update_incidents(incident_bulk_in)

Bulk Update Incidents

Acknowledge or resolve many incidents with the per-incident rules.  Same role as `/ack` and `/resolve`, and the same visibility: an incident the caller cannot see is never touched. Resolved incidents are skipped, as are incidents already acknowledged for `ack`, so a repeat call changes nothing. The caller's role is rechecked, and held, while the rows are locked, so a demotion that lands during the request cannot be overtaken by the write. With `expected_count`, the locked selection must be exactly that many incidents, or nothing is written and the answer is 409.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.incident_bulk_in import IncidentBulkIn
from spatialflow_generated.models.incident_bulk_out import IncidentBulkOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    incident_bulk_in = spatialflow_generated.IncidentBulkIn() # IncidentBulkIn | 

    try:
        # Bulk Update Incidents
        api_response = await api_instance.apps_operations_api_bulk_update_incidents(incident_bulk_in)
        print("The response of OperationsApi->apps_operations_api_bulk_update_incidents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_bulk_update_incidents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_bulk_in** | [**IncidentBulkIn**](IncidentBulkIn.md)|  | 

### Return type

[**IncidentBulkOut**](IncidentBulkOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_create_saved_view**
> SavedViewOut apps_operations_api_create_saved_view(saved_view_in)

Create Saved View

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.saved_view_in import SavedViewIn
from spatialflow_generated.models.saved_view_out import SavedViewOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    saved_view_in = spatialflow_generated.SavedViewIn() # SavedViewIn | 

    try:
        # Create Saved View
        api_response = await api_instance.apps_operations_api_create_saved_view(saved_view_in)
        print("The response of OperationsApi->apps_operations_api_create_saved_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_create_saved_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saved_view_in** | [**SavedViewIn**](SavedViewIn.md)|  | 

### Return type

[**SavedViewOut**](SavedViewOut.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_delete_saved_view**
> SavedViewDeleteOut apps_operations_api_delete_saved_view(view_id)

Delete Saved View

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.saved_view_delete_out import SavedViewDeleteOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    view_id = 'view_id_example' # str | 

    try:
        # Delete Saved View
        api_response = await api_instance.apps_operations_api_delete_saved_view(view_id)
        print("The response of OperationsApi->apps_operations_api_delete_saved_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_delete_saved_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 

### Return type

[**SavedViewDeleteOut**](SavedViewDeleteOut.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_get_incident**
> IncidentOut apps_operations_api_get_incident(incident_id)

Get Incident

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.incident_out import IncidentOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    incident_id = 'incident_id_example' # str | 

    try:
        # Get Incident
        api_response = await api_instance.apps_operations_api_get_incident(incident_id)
        print("The response of OperationsApi->apps_operations_api_get_incident:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_get_incident: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**|  | 

### Return type

[**IncidentOut**](IncidentOut.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_get_overview**
> OverviewOut apps_operations_api_get_overview()

Get Overview

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.overview_out import OverviewOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)

    try:
        # Get Overview
        api_response = await api_instance.apps_operations_api_get_overview()
        print("The response of OperationsApi->apps_operations_api_get_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_get_overview: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OverviewOut**](OverviewOut.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_list_incident_groups**
> IncidentGroupListOut apps_operations_api_list_incident_groups(status=status, severity=severity)

List Incident Groups

Incidents counted by cause, so a surface can triage without paging them all.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.incident_group_list_out import IncidentGroupListOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    status = open # str |  (optional) (default to open)
    severity = 'severity_example' # str |  (optional)

    try:
        # List Incident Groups
        api_response = await api_instance.apps_operations_api_list_incident_groups(status=status, severity=severity)
        print("The response of OperationsApi->apps_operations_api_list_incident_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_list_incident_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] [default to open]
 **severity** | **str**|  | [optional] 

### Return type

[**IncidentGroupListOut**](IncidentGroupListOut.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_list_incidents**
> IncidentListOut apps_operations_api_list_incidents(status=status, severity=severity, owner=owner, signal_type=signal_type, cursor=cursor, limit=limit)

List Incidents

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.incident_list_out import IncidentListOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    status = open # str |  (optional) (default to open)
    severity = 'severity_example' # str |  (optional)
    owner = 'owner_example' # str |  (optional)
    signal_type = 'signal_type_example' # str |  (optional)
    cursor = 'cursor_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)

    try:
        # List Incidents
        api_response = await api_instance.apps_operations_api_list_incidents(status=status, severity=severity, owner=owner, signal_type=signal_type, cursor=cursor, limit=limit)
        print("The response of OperationsApi->apps_operations_api_list_incidents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_list_incidents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**|  | [optional] [default to open]
 **severity** | **str**|  | [optional] 
 **owner** | **str**|  | [optional] 
 **signal_type** | **str**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]

### Return type

[**IncidentListOut**](IncidentListOut.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_list_saved_views**
> List[SavedViewOut] apps_operations_api_list_saved_views(surface)

List Saved Views

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.saved_view_out import SavedViewOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    surface = 'surface_example' # str | 

    try:
        # List Saved Views
        api_response = await api_instance.apps_operations_api_list_saved_views(surface)
        print("The response of OperationsApi->apps_operations_api_list_saved_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_list_saved_views: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surface** | **str**|  | 

### Return type

[**List[SavedViewOut]**](SavedViewOut.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_mute_incident**
> IncidentOut apps_operations_api_mute_incident(incident_id, incident_mute_in)

Mute Incident

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.incident_mute_in import IncidentMuteIn
from spatialflow_generated.models.incident_out import IncidentOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    incident_id = 'incident_id_example' # str | 
    incident_mute_in = spatialflow_generated.IncidentMuteIn() # IncidentMuteIn | 

    try:
        # Mute Incident
        api_response = await api_instance.apps_operations_api_mute_incident(incident_id, incident_mute_in)
        print("The response of OperationsApi->apps_operations_api_mute_incident:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_mute_incident: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**|  | 
 **incident_mute_in** | [**IncidentMuteIn**](IncidentMuteIn.md)|  | 

### Return type

[**IncidentOut**](IncidentOut.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_resolve_incident**
> IncidentOut apps_operations_api_resolve_incident(incident_id)

Resolve Incident

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.incident_out import IncidentOut
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    incident_id = 'incident_id_example' # str | 

    try:
        # Resolve Incident
        api_response = await api_instance.apps_operations_api_resolve_incident(incident_id)
        print("The response of OperationsApi->apps_operations_api_resolve_incident:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_resolve_incident: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **incident_id** | **str**|  | 

### Return type

[**IncidentOut**](IncidentOut.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_stream_badges**
> str apps_operations_api_stream_badges()

Stream Badges

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
    api_instance = spatialflow_generated.OperationsApi(api_client)

    try:
        # Stream Badges
        api_response = await api_instance.apps_operations_api_stream_badges()
        print("The response of OperationsApi->apps_operations_api_stream_badges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_stream_badges: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Live badge counts as server-sent events. dlq_pending is null unless the caller is a workspace owner or manager. The session and membership are rechecked before every poll; the stream ends when either lapses, and after an hour. Clients reconnect. |  * Cache-Control -  <br>  * X-Accel-Buffering -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_operations_api_update_saved_view**
> SavedViewOut apps_operations_api_update_saved_view(view_id, saved_view_patch_in)

Update Saved View

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.saved_view_out import SavedViewOut
from spatialflow_generated.models.saved_view_patch_in import SavedViewPatchIn
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
    api_instance = spatialflow_generated.OperationsApi(api_client)
    view_id = 'view_id_example' # str | 
    saved_view_patch_in = spatialflow_generated.SavedViewPatchIn() # SavedViewPatchIn | 

    try:
        # Update Saved View
        api_response = await api_instance.apps_operations_api_update_saved_view(view_id, saved_view_patch_in)
        print("The response of OperationsApi->apps_operations_api_update_saved_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->apps_operations_api_update_saved_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 
 **saved_view_patch_in** | [**SavedViewPatchIn**](SavedViewPatchIn.md)|  | 

### Return type

[**SavedViewOut**](SavedViewOut.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

