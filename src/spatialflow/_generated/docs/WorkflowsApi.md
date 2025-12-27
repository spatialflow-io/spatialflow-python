# spatialflow_generated.WorkflowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_workflows_api_activate_workflow**](WorkflowsApi.md#apps_workflows_api_activate_workflow) | **POST** /api/v1/workflows/{workflow_id}/activate | Activate Workflow
[**apps_workflows_api_create_workflow**](WorkflowsApi.md#apps_workflows_api_create_workflow) | **POST** /api/v1/workflows | Create Workflow
[**apps_workflows_api_create_workflow_from_template**](WorkflowsApi.md#apps_workflows_api_create_workflow_from_template) | **POST** /api/v1/workflows/templates/{template_id}/use | Create Workflow From Template
[**apps_workflows_api_delete_workflow**](WorkflowsApi.md#apps_workflows_api_delete_workflow) | **DELETE** /api/v1/workflows/{workflow_id} | Delete Workflow
[**apps_workflows_api_duplicate_workflow**](WorkflowsApi.md#apps_workflows_api_duplicate_workflow) | **POST** /api/v1/workflows/{workflow_id}/duplicate | Duplicate Workflow
[**apps_workflows_api_execute_workflow**](WorkflowsApi.md#apps_workflows_api_execute_workflow) | **POST** /api/v1/workflows/{workflow_id}/execute | Execute Workflow
[**apps_workflows_api_export_workflow**](WorkflowsApi.md#apps_workflows_api_export_workflow) | **GET** /api/v1/workflows/{workflow_id}/export | Export Workflow
[**apps_workflows_api_get_available_retry_policies**](WorkflowsApi.md#apps_workflows_api_get_available_retry_policies) | **GET** /api/v1/workflows/retry-policies | Get Available Retry Policies
[**apps_workflows_api_get_execution_details**](WorkflowsApi.md#apps_workflows_api_get_execution_details) | **GET** /api/v1/workflows/executions/{execution_id} | Get Execution Details
[**apps_workflows_api_get_system_performance_summary**](WorkflowsApi.md#apps_workflows_api_get_system_performance_summary) | **GET** /api/v1/workflows/performance/summary | Get System Performance Summary
[**apps_workflows_api_get_version_diff**](WorkflowsApi.md#apps_workflows_api_get_version_diff) | **GET** /api/v1/workflows/{workflow_id}/versions/{version_number}/diff | Get Version Diff
[**apps_workflows_api_get_workflow**](WorkflowsApi.md#apps_workflows_api_get_workflow) | **GET** /api/v1/workflows/{workflow_id} | Get Workflow
[**apps_workflows_api_get_workflow_bottlenecks**](WorkflowsApi.md#apps_workflows_api_get_workflow_bottlenecks) | **GET** /api/v1/workflows/{workflow_id}/performance/bottlenecks | Get Workflow Bottlenecks
[**apps_workflows_api_get_workflow_execution_detail**](WorkflowsApi.md#apps_workflows_api_get_workflow_execution_detail) | **GET** /api/v1/workflows/{workflow_id}/executions/{execution_id} | Get Workflow Execution Detail
[**apps_workflows_api_get_workflow_executions**](WorkflowsApi.md#apps_workflows_api_get_workflow_executions) | **GET** /api/v1/workflows/{workflow_id}/executions | Get Workflow Executions
[**apps_workflows_api_get_workflow_performance**](WorkflowsApi.md#apps_workflows_api_get_workflow_performance) | **GET** /api/v1/workflows/{workflow_id}/performance | Get Workflow Performance
[**apps_workflows_api_get_workflow_retry_policy**](WorkflowsApi.md#apps_workflows_api_get_workflow_retry_policy) | **GET** /api/v1/workflows/{workflow_id}/retry-policy | Get Workflow Retry Policy
[**apps_workflows_api_get_workflow_statistics**](WorkflowsApi.md#apps_workflows_api_get_workflow_statistics) | **GET** /api/v1/workflows/{workflow_id}/statistics | Get Workflow Statistics
[**apps_workflows_api_get_workflow_step_performance**](WorkflowsApi.md#apps_workflows_api_get_workflow_step_performance) | **GET** /api/v1/workflows/{workflow_id}/performance/steps | Get Workflow Step Performance
[**apps_workflows_api_get_workflow_template**](WorkflowsApi.md#apps_workflows_api_get_workflow_template) | **GET** /api/v1/workflows/templates/{template_id} | Get Workflow Template
[**apps_workflows_api_health_check**](WorkflowsApi.md#apps_workflows_api_health_check) | **GET** /api/v1/workflows/health | Health Check
[**apps_workflows_api_import_workflow**](WorkflowsApi.md#apps_workflows_api_import_workflow) | **POST** /api/v1/workflows/import | Import Workflow
[**apps_workflows_api_list_workflow_executions**](WorkflowsApi.md#apps_workflows_api_list_workflow_executions) | **GET** /api/v1/workflows/executions | List Workflow Executions
[**apps_workflows_api_list_workflow_templates**](WorkflowsApi.md#apps_workflows_api_list_workflow_templates) | **GET** /api/v1/workflows/templates | List Workflow Templates
[**apps_workflows_api_list_workflow_versions**](WorkflowsApi.md#apps_workflows_api_list_workflow_versions) | **GET** /api/v1/workflows/{workflow_id}/versions | List Workflow Versions
[**apps_workflows_api_list_workflows**](WorkflowsApi.md#apps_workflows_api_list_workflows) | **GET** /api/v1/workflows | List Workflows
[**apps_workflows_api_restore_workflow_version**](WorkflowsApi.md#apps_workflows_api_restore_workflow_version) | **POST** /api/v1/workflows/{workflow_id}/versions/{version_number}/restore | Restore Workflow Version
[**apps_workflows_api_test_workflow**](WorkflowsApi.md#apps_workflows_api_test_workflow) | **POST** /api/v1/workflows/{workflow_id}/test | Test Workflow
[**apps_workflows_api_toggle_workflow**](WorkflowsApi.md#apps_workflows_api_toggle_workflow) | **POST** /api/v1/workflows/{workflow_id}/toggle | Toggle Workflow
[**apps_workflows_api_update_workflow**](WorkflowsApi.md#apps_workflows_api_update_workflow) | **PUT** /api/v1/workflows/{workflow_id} | Update Workflow
[**apps_workflows_api_update_workflow_retry_policy**](WorkflowsApi.md#apps_workflows_api_update_workflow_retry_policy) | **PUT** /api/v1/workflows/{workflow_id}/retry-policy | Update Workflow Retry Policy


# **apps_workflows_api_activate_workflow**
> WorkflowOut apps_workflows_api_activate_workflow(workflow_id)

Activate Workflow

Activate a draft workflow for production use.

Transitions a workflow from draft status to active status.
Idempotent: Returns 200 if workflow is already active.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workflow_out import WorkflowOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Activate Workflow
        api_response = await api_instance.apps_workflows_api_activate_workflow(workflow_id)
        print("The response of WorkflowsApi->apps_workflows_api_activate_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_activate_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 

### Return type

[**WorkflowOut**](WorkflowOut.md)

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

# **apps_workflows_api_create_workflow**
> WorkflowOut apps_workflows_api_create_workflow(workflow_in)

Create Workflow

Create a new workflow.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workflow_in import WorkflowIn
from spatialflow_generated.models.workflow_out import WorkflowOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_in = spatialflow_generated.WorkflowIn() # WorkflowIn | 

    try:
        # Create Workflow
        api_response = await api_instance.apps_workflows_api_create_workflow(workflow_in)
        print("The response of WorkflowsApi->apps_workflows_api_create_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_create_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_in** | [**WorkflowIn**](WorkflowIn.md)|  | 

### Return type

[**WorkflowOut**](WorkflowOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workflows_api_create_workflow_from_template**
> WorkflowOut apps_workflows_api_create_workflow_from_template(template_id, create_from_template_in)

Create Workflow From Template

Create a workflow from a template.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.create_from_template_in import CreateFromTemplateIn
from spatialflow_generated.models.workflow_out import WorkflowOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    template_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    create_from_template_in = spatialflow_generated.CreateFromTemplateIn() # CreateFromTemplateIn | 

    try:
        # Create Workflow From Template
        api_response = await api_instance.apps_workflows_api_create_workflow_from_template(template_id, create_from_template_in)
        print("The response of WorkflowsApi->apps_workflows_api_create_workflow_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_create_workflow_from_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**|  | 
 **create_from_template_in** | [**CreateFromTemplateIn**](CreateFromTemplateIn.md)|  | 

### Return type

[**WorkflowOut**](WorkflowOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workflows_api_delete_workflow**
> Dict[str, object] apps_workflows_api_delete_workflow(workflow_id)

Delete Workflow

Delete a workflow.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Workflow
        api_response = await api_instance.apps_workflows_api_delete_workflow(workflow_id)
        print("The response of WorkflowsApi->apps_workflows_api_delete_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_delete_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 

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

# **apps_workflows_api_duplicate_workflow**
> WorkflowOut apps_workflows_api_duplicate_workflow(workflow_id, name)

Duplicate Workflow

Duplicate an existing workflow.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workflow_out import WorkflowOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    name = 'name_example' # str | 

    try:
        # Duplicate Workflow
        api_response = await api_instance.apps_workflows_api_duplicate_workflow(workflow_id, name)
        print("The response of WorkflowsApi->apps_workflows_api_duplicate_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_duplicate_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 
 **name** | **str**|  | 

### Return type

[**WorkflowOut**](WorkflowOut.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workflows_api_execute_workflow**
> Dict[str, object] apps_workflows_api_execute_workflow(workflow_id, test_data=test_data)

Execute Workflow

Manually execute a workflow.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    test_data = None # Dict[str, object] |  (optional)

    try:
        # Execute Workflow
        api_response = await api_instance.apps_workflows_api_execute_workflow(workflow_id, test_data=test_data)
        print("The response of WorkflowsApi->apps_workflows_api_execute_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_execute_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 
 **test_data** | [**Dict[str, object]**](object.md)|  | [optional] 

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workflows_api_export_workflow**
> Dict[str, object] apps_workflows_api_export_workflow(workflow_id)

Export Workflow

Export workflow as JSON.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Export Workflow
        api_response = await api_instance.apps_workflows_api_export_workflow(workflow_id)
        print("The response of WorkflowsApi->apps_workflows_api_export_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_export_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 

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

# **apps_workflows_api_get_available_retry_policies**
> RetryPolicyResponseSchema apps_workflows_api_get_available_retry_policies()

Get Available Retry Policies

Get available retry policies and configuration options.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.retry_policy_response_schema import RetryPolicyResponseSchema
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)

    try:
        # Get Available Retry Policies
        api_response = await api_instance.apps_workflows_api_get_available_retry_policies()
        print("The response of WorkflowsApi->apps_workflows_api_get_available_retry_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_available_retry_policies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RetryPolicyResponseSchema**](RetryPolicyResponseSchema.md)

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

# **apps_workflows_api_get_execution_details**
> Dict[str, object] apps_workflows_api_get_execution_details(execution_id)

Get Execution Details

Get detailed execution information including steps.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    execution_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Execution Details
        api_response = await api_instance.apps_workflows_api_get_execution_details(execution_id)
        print("The response of WorkflowsApi->apps_workflows_api_get_execution_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_execution_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **execution_id** | **UUID**|  | 

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

# **apps_workflows_api_get_system_performance_summary**
> Dict[str, object] apps_workflows_api_get_system_performance_summary()

Get System Performance Summary

Get overall system performance summary for the user.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)

    try:
        # Get System Performance Summary
        api_response = await api_instance.apps_workflows_api_get_system_performance_summary()
        print("The response of WorkflowsApi->apps_workflows_api_get_system_performance_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_system_performance_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **apps_workflows_api_get_version_diff**
> Dict[str, object] apps_workflows_api_get_version_diff(workflow_id, version_number)

Get Version Diff

Compare a specific version with the current workflow state.

Returns a diff showing what changed between the version and current state.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    version_number = 56 # int | 

    try:
        # Get Version Diff
        api_response = await api_instance.apps_workflows_api_get_version_diff(workflow_id, version_number)
        print("The response of WorkflowsApi->apps_workflows_api_get_version_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_version_diff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 
 **version_number** | **int**|  | 

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

# **apps_workflows_api_get_workflow**
> WorkflowOut apps_workflows_api_get_workflow(workflow_id)

Get Workflow

Get workflow details.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workflow_out import WorkflowOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Workflow
        api_response = await api_instance.apps_workflows_api_get_workflow(workflow_id)
        print("The response of WorkflowsApi->apps_workflows_api_get_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 

### Return type

[**WorkflowOut**](WorkflowOut.md)

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

# **apps_workflows_api_get_workflow_bottlenecks**
> List[Optional[Dict[str, object]]] apps_workflows_api_get_workflow_bottlenecks(workflow_id)

Get Workflow Bottlenecks

Identify performance bottlenecks in a workflow.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Workflow Bottlenecks
        api_response = await api_instance.apps_workflows_api_get_workflow_bottlenecks(workflow_id)
        print("The response of WorkflowsApi->apps_workflows_api_get_workflow_bottlenecks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_workflow_bottlenecks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 

### Return type

**List[Optional[Dict[str, object]]]**

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

# **apps_workflows_api_get_workflow_execution_detail**
> Dict[str, object] apps_workflows_api_get_workflow_execution_detail(workflow_id, execution_id)

Get Workflow Execution Detail

Get detailed execution information for a specific workflow execution.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    execution_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Workflow Execution Detail
        api_response = await api_instance.apps_workflows_api_get_workflow_execution_detail(workflow_id, execution_id)
        print("The response of WorkflowsApi->apps_workflows_api_get_workflow_execution_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_workflow_execution_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 
 **execution_id** | **UUID**|  | 

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

# **apps_workflows_api_get_workflow_executions**
> List[ExecutionOut] apps_workflows_api_get_workflow_executions(workflow_id, status=status, limit=limit, offset=offset)

Get Workflow Executions

Get execution history for a specific workflow.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.execution_out import ExecutionOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    status = 'status_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Workflow Executions
        api_response = await api_instance.apps_workflows_api_get_workflow_executions(workflow_id, status=status, limit=limit, offset=offset)
        print("The response of WorkflowsApi->apps_workflows_api_get_workflow_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_workflow_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 
 **status** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[ExecutionOut]**](ExecutionOut.md)

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

# **apps_workflows_api_get_workflow_performance**
> Dict[str, object] apps_workflows_api_get_workflow_performance(workflow_id, start_date=start_date, end_date=end_date)

Get Workflow Performance

Get performance metrics for a workflow.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    start_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get Workflow Performance
        api_response = await api_instance.apps_workflows_api_get_workflow_performance(workflow_id, start_date=start_date, end_date=end_date)
        print("The response of WorkflowsApi->apps_workflows_api_get_workflow_performance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_workflow_performance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 
 **start_date** | **datetime**|  | [optional] 
 **end_date** | **datetime**|  | [optional] 

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

# **apps_workflows_api_get_workflow_retry_policy**
> Dict[str, object] apps_workflows_api_get_workflow_retry_policy(workflow_id)

Get Workflow Retry Policy

Get retry policy configuration for a workflow.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Workflow Retry Policy
        api_response = await api_instance.apps_workflows_api_get_workflow_retry_policy(workflow_id)
        print("The response of WorkflowsApi->apps_workflows_api_get_workflow_retry_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_workflow_retry_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 

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

# **apps_workflows_api_get_workflow_statistics**
> Dict[str, object] apps_workflows_api_get_workflow_statistics(workflow_id)

Get Workflow Statistics

Get detailed statistics for a workflow.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Workflow Statistics
        api_response = await api_instance.apps_workflows_api_get_workflow_statistics(workflow_id)
        print("The response of WorkflowsApi->apps_workflows_api_get_workflow_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_workflow_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 

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

# **apps_workflows_api_get_workflow_step_performance**
> List[Optional[Dict[str, object]]] apps_workflows_api_get_workflow_step_performance(workflow_id)

Get Workflow Step Performance

Get performance breakdown by workflow step.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Workflow Step Performance
        api_response = await api_instance.apps_workflows_api_get_workflow_step_performance(workflow_id)
        print("The response of WorkflowsApi->apps_workflows_api_get_workflow_step_performance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_workflow_step_performance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 

### Return type

**List[Optional[Dict[str, object]]]**

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

# **apps_workflows_api_get_workflow_template**
> Dict[str, object] apps_workflows_api_get_workflow_template(template_id)

Get Workflow Template

Get workflow template details.

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    template_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Workflow Template
        api_response = await api_instance.apps_workflows_api_get_workflow_template(template_id)
        print("The response of WorkflowsApi->apps_workflows_api_get_workflow_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_get_workflow_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **UUID**|  | 

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

# **apps_workflows_api_health_check**
> apps_workflows_api_health_check()

Health Check

Health check endpoint.

### Example


```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.WorkflowsApi(api_client)

    try:
        # Health Check
        await api_instance.apps_workflows_api_health_check()
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_health_check: %s\n" % e)
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

# **apps_workflows_api_import_workflow**
> WorkflowOut apps_workflows_api_import_workflow(workflow_import_schema)

Import Workflow

Import workflow from JSON.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workflow_import_schema import WorkflowImportSchema
from spatialflow_generated.models.workflow_out import WorkflowOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_import_schema = spatialflow_generated.WorkflowImportSchema() # WorkflowImportSchema | 

    try:
        # Import Workflow
        api_response = await api_instance.apps_workflows_api_import_workflow(workflow_import_schema)
        print("The response of WorkflowsApi->apps_workflows_api_import_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_import_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_import_schema** | [**WorkflowImportSchema**](WorkflowImportSchema.md)|  | 

### Return type

[**WorkflowOut**](WorkflowOut.md)

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

# **apps_workflows_api_list_workflow_executions**
> List[ExecutionOut] apps_workflows_api_list_workflow_executions(workflow_id=workflow_id, status=status, limit=limit, offset=offset)

List Workflow Executions

List workflow executions with filtering.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.execution_out import ExecutionOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    status = 'status_example' # str |  (optional)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List Workflow Executions
        api_response = await api_instance.apps_workflows_api_list_workflow_executions(workflow_id=workflow_id, status=status, limit=limit, offset=offset)
        print("The response of WorkflowsApi->apps_workflows_api_list_workflow_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_list_workflow_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | [optional] 
 **status** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**List[ExecutionOut]**](ExecutionOut.md)

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

# **apps_workflows_api_list_workflow_templates**
> List[TemplateOut] apps_workflows_api_list_workflow_templates(category=category)

List Workflow Templates

List available workflow templates.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.template_out import TemplateOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    category = 'category_example' # str |  (optional)

    try:
        # List Workflow Templates
        api_response = await api_instance.apps_workflows_api_list_workflow_templates(category=category)
        print("The response of WorkflowsApi->apps_workflows_api_list_workflow_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_list_workflow_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | [optional] 

### Return type

[**List[TemplateOut]**](TemplateOut.md)

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

# **apps_workflows_api_list_workflow_versions**
> List[Dict[str, object]] apps_workflows_api_list_workflow_versions(workflow_id)

List Workflow Versions

List all versions of a workflow.

Returns versions in descending order (newest first).

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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # List Workflow Versions
        api_response = await api_instance.apps_workflows_api_list_workflow_versions(workflow_id)
        print("The response of WorkflowsApi->apps_workflows_api_list_workflow_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_list_workflow_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 

### Return type

**List[Dict[str, object]]**

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

# **apps_workflows_api_list_workflows**
> WorkflowListResponse apps_workflows_api_list_workflows(limit=limit, offset=offset, is_active=is_active, category=category, search=search)

List Workflows

List user's workflows with filtering.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workflow_list_response import WorkflowListResponse
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    is_active = True # bool |  (optional)
    category = 'category_example' # str |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # List Workflows
        api_response = await api_instance.apps_workflows_api_list_workflows(limit=limit, offset=offset, is_active=is_active, category=category, search=search)
        print("The response of WorkflowsApi->apps_workflows_api_list_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_list_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **is_active** | **bool**|  | [optional] 
 **category** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**WorkflowListResponse**](WorkflowListResponse.md)

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

# **apps_workflows_api_restore_workflow_version**
> WorkflowOut apps_workflows_api_restore_workflow_version(workflow_id, version_number)

Restore Workflow Version

Restore a workflow to a previous version.

This creates a new version with the snapshot data from the specified version.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workflow_out import WorkflowOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    version_number = 56 # int | 

    try:
        # Restore Workflow Version
        api_response = await api_instance.apps_workflows_api_restore_workflow_version(workflow_id, version_number)
        print("The response of WorkflowsApi->apps_workflows_api_restore_workflow_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_restore_workflow_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 
 **version_number** | **int**|  | 

### Return type

[**WorkflowOut**](WorkflowOut.md)

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

# **apps_workflows_api_test_workflow**
> Dict[str, object] apps_workflows_api_test_workflow(workflow_id, test_workflow_in)

Test Workflow

Test workflow configuration with sample data.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.test_workflow_in import TestWorkflowIn
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    test_workflow_in = spatialflow_generated.TestWorkflowIn() # TestWorkflowIn | 

    try:
        # Test Workflow
        api_response = await api_instance.apps_workflows_api_test_workflow(workflow_id, test_workflow_in)
        print("The response of WorkflowsApi->apps_workflows_api_test_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_test_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 
 **test_workflow_in** | [**TestWorkflowIn**](TestWorkflowIn.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workflows_api_toggle_workflow**
> WorkflowOut apps_workflows_api_toggle_workflow(workflow_id)

Toggle Workflow

Toggle workflow between active and paused states.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workflow_out import WorkflowOut
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Toggle Workflow
        api_response = await api_instance.apps_workflows_api_toggle_workflow(workflow_id)
        print("The response of WorkflowsApi->apps_workflows_api_toggle_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_toggle_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 

### Return type

[**WorkflowOut**](WorkflowOut.md)

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

# **apps_workflows_api_update_workflow**
> WorkflowOut apps_workflows_api_update_workflow(workflow_id, workflow_update)

Update Workflow

Update workflow configuration.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workflow_out import WorkflowOut
from spatialflow_generated.models.workflow_update import WorkflowUpdate
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    workflow_update = spatialflow_generated.WorkflowUpdate() # WorkflowUpdate | 

    try:
        # Update Workflow
        api_response = await api_instance.apps_workflows_api_update_workflow(workflow_id, workflow_update)
        print("The response of WorkflowsApi->apps_workflows_api_update_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_update_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 
 **workflow_update** | [**WorkflowUpdate**](WorkflowUpdate.md)|  | 

### Return type

[**WorkflowOut**](WorkflowOut.md)

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
**422** | Unprocessable Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workflows_api_update_workflow_retry_policy**
> Dict[str, object] apps_workflows_api_update_workflow_retry_policy(workflow_id, workflow_retry_policy_update_schema)

Update Workflow Retry Policy

Update retry policy configuration for a workflow.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workflow_retry_policy_update_schema import WorkflowRetryPolicyUpdateSchema
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
    api_instance = spatialflow_generated.WorkflowsApi(api_client)
    workflow_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    workflow_retry_policy_update_schema = spatialflow_generated.WorkflowRetryPolicyUpdateSchema() # WorkflowRetryPolicyUpdateSchema | 

    try:
        # Update Workflow Retry Policy
        api_response = await api_instance.apps_workflows_api_update_workflow_retry_policy(workflow_id, workflow_retry_policy_update_schema)
        print("The response of WorkflowsApi->apps_workflows_api_update_workflow_retry_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->apps_workflows_api_update_workflow_retry_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **UUID**|  | 
 **workflow_retry_policy_update_schema** | [**WorkflowRetryPolicyUpdateSchema**](WorkflowRetryPolicyUpdateSchema.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

