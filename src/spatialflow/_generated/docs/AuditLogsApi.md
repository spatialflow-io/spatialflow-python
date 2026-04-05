# spatialflow_generated.AuditLogsApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_workspaces_api_audit_export_audit_logs**](AuditLogsApi.md#apps_workspaces_api_audit_export_audit_logs) | **GET** /api/v1/audit-logs/export/ | Export Audit Logs
[**apps_workspaces_api_audit_list_audit_logs**](AuditLogsApi.md#apps_workspaces_api_audit_list_audit_logs) | **GET** /api/v1/audit-logs/ | List Audit Logs


# **apps_workspaces_api_audit_export_audit_logs**
> apps_workspaces_api_audit_export_audit_logs(export_format=export_format, action=action, user_id=user_id, resource_type=resource_type, date_from=date_from, date_to=date_to, search=search)

Export Audit Logs

Export audit logs as CSV or JSON.  Available to workspace owners and managers. Exports up to 10,000 records matching the filters. The `changes` field is excluded from exports to limit memory usage.

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
    api_instance = spatialflow_generated.AuditLogsApi(api_client)
    export_format = csv # str |  (optional) (default to csv)
    action = 'action_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    resource_type = 'resource_type_example' # str |  (optional)
    date_from = 'date_from_example' # str |  (optional)
    date_to = 'date_to_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # Export Audit Logs
        await api_instance.apps_workspaces_api_audit_export_audit_logs(export_format=export_format, action=action, user_id=user_id, resource_type=resource_type, date_from=date_from, date_to=date_to, search=search)
    except Exception as e:
        print("Exception when calling AuditLogsApi->apps_workspaces_api_audit_export_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_format** | **str**|  | [optional] [default to csv]
 **action** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **resource_type** | **str**|  | [optional] 
 **date_from** | **str**|  | [optional] 
 **date_to** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_audit_list_audit_logs**
> AuditLogListResponse apps_workspaces_api_audit_list_audit_logs(action=action, user_id=user_id, resource_type=resource_type, date_from=date_from, date_to=date_to, search=search, page=page, page_size=page_size)

List Audit Logs

List audit logs for the workspace with optional filtering.  Available to workspace owners and managers.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.audit_log_list_response import AuditLogListResponse
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
    api_instance = spatialflow_generated.AuditLogsApi(api_client)
    action = 'action_example' # str |  (optional)
    user_id = 'user_id_example' # str |  (optional)
    resource_type = 'resource_type_example' # str |  (optional)
    date_from = 'date_from_example' # str |  (optional)
    date_to = 'date_to_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    page_size = 50 # int |  (optional) (default to 50)

    try:
        # List Audit Logs
        api_response = await api_instance.apps_workspaces_api_audit_list_audit_logs(action=action, user_id=user_id, resource_type=resource_type, date_from=date_from, date_to=date_to, search=search, page=page, page_size=page_size)
        print("The response of AuditLogsApi->apps_workspaces_api_audit_list_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditLogsApi->apps_workspaces_api_audit_list_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | [optional] 
 **user_id** | **str**|  | [optional] 
 **resource_type** | **str**|  | [optional] 
 **date_from** | **str**|  | [optional] 
 **date_to** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 50]

### Return type

[**AuditLogListResponse**](AuditLogListResponse.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

