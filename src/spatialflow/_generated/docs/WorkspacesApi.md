# spatialflow_generated.WorkspacesApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_workspaces_api_get_workspace**](WorkspacesApi.md#apps_workspaces_api_get_workspace) | **GET** /api/v1/workspaces/ | Get Workspace
[**apps_workspaces_api_get_workspace_usage**](WorkspacesApi.md#apps_workspaces_api_get_workspace_usage) | **GET** /api/v1/workspaces/usage | Get Workspace Usage
[**apps_workspaces_api_update_workspace**](WorkspacesApi.md#apps_workspaces_api_update_workspace) | **PUT** /api/v1/workspaces/ | Update Workspace


# **apps_workspaces_api_get_workspace**
> WorkspaceOut apps_workspaces_api_get_workspace()

Get Workspace

Get the user's workspace.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_out import WorkspaceOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # Get Workspace
        api_response = await api_instance.apps_workspaces_api_get_workspace()
        print("The response of WorkspacesApi->apps_workspaces_api_get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_get_workspace: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkspaceOut**](WorkspaceOut.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_get_workspace_usage**
> UsageResponse apps_workspaces_api_get_workspace_usage()

Get Workspace Usage

Get current period usage metrics for billing.  Returns aggregated usage for the current day (midnight to now). Usage is calculated hourly and includes: - Location events (DeviceLocation records) - Action deliveries (successful webhook deliveries) - Event units (locations + 0.5 * actions)  **Event Units Calculation (PRD §7):** - 1 location event = 1 event unit - 1 action delivery = 0.5 event units  **Tier Limits (PRD §7):** - Developer: 500,000 event units/month - Pro: 5,000,000 event units/month - Enterprise: Unlimited  **Example Response:** ```json {     \"location_events\": 10000,     \"action_deliveries\": 5000,     \"event_units\": 12500,     \"tier\": \"developer\",     \"tier_limit\": 500000,     \"period_start\": \"2025-10-01T00:00:00Z\",     \"period_end\": \"2025-10-01T23:59:59Z\" } ```  PRD Reference: §7 Pricing & Packaging Roadmap: Phase 2, Task 2.3

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.usage_response import UsageResponse
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # Get Workspace Usage
        api_response = await api_instance.apps_workspaces_api_get_workspace_usage()
        print("The response of WorkspacesApi->apps_workspaces_api_get_workspace_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_get_workspace_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UsageResponse**](UsageResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_update_workspace**
> WorkspaceOut apps_workspaces_api_update_workspace(workspace_in)

Update Workspace

Update the user's workspace.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_in import WorkspaceIn
from spatialflow_generated.models.workspace_out import WorkspaceOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    workspace_in = spatialflow_generated.WorkspaceIn() # WorkspaceIn | 

    try:
        # Update Workspace
        api_response = await api_instance.apps_workspaces_api_update_workspace(workspace_in)
        print("The response of WorkspacesApi->apps_workspaces_api_update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_in** | [**WorkspaceIn**](WorkspaceIn.md)|  | 

### Return type

[**WorkspaceOut**](WorkspaceOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

