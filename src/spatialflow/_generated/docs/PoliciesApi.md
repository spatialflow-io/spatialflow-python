# spatialflow_generated.PoliciesApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_devices_api_policies_create_policy**](PoliciesApi.md#apps_devices_api_policies_create_policy) | **POST** /api/v1/policies/ | Create policy
[**apps_devices_api_policies_delete_policy**](PoliciesApi.md#apps_devices_api_policies_delete_policy) | **DELETE** /api/v1/policies/{policy_id}/ | Delete policy
[**apps_devices_api_policies_get_policy**](PoliciesApi.md#apps_devices_api_policies_get_policy) | **GET** /api/v1/policies/{policy_id}/ | Get policy detail
[**apps_devices_api_policies_list_policies**](PoliciesApi.md#apps_devices_api_policies_list_policies) | **GET** /api/v1/policies/ | List policies
[**apps_devices_api_policies_list_templates**](PoliciesApi.md#apps_devices_api_policies_list_templates) | **GET** /api/v1/policies/templates | List policy templates
[**apps_devices_api_policies_update_policy**](PoliciesApi.md#apps_devices_api_policies_update_policy) | **PUT** /api/v1/policies/{policy_id}/ | Update policy


# **apps_devices_api_policies_create_policy**
> PolicyOut apps_devices_api_policies_create_policy(policy_create_in)

Create policy

Create a new policy. Requires owner or manager role.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.policy_create_in import PolicyCreateIn
from spatialflow_generated.models.policy_out import PolicyOut
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
    api_instance = spatialflow_generated.PoliciesApi(api_client)
    policy_create_in = spatialflow_generated.PolicyCreateIn() # PolicyCreateIn | 

    try:
        # Create policy
        api_response = await api_instance.apps_devices_api_policies_create_policy(policy_create_in)
        print("The response of PoliciesApi->apps_devices_api_policies_create_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->apps_devices_api_policies_create_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_create_in** | [**PolicyCreateIn**](PolicyCreateIn.md)|  | 

### Return type

[**PolicyOut**](PolicyOut.md)

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
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_policies_delete_policy**
> apps_devices_api_policies_delete_policy(policy_id)

Delete policy

Delete a policy. Requires owner or manager role.

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
    api_instance = spatialflow_generated.PoliciesApi(api_client)
    policy_id = 'policy_id_example' # str | 

    try:
        # Delete policy
        await api_instance.apps_devices_api_policies_delete_policy(policy_id)
    except Exception as e:
        print("Exception when calling PoliciesApi->apps_devices_api_policies_delete_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

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
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_devices_api_policies_get_policy**
> PolicyOut apps_devices_api_policies_get_policy(policy_id)

Get policy detail

Get a single policy by ID.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.policy_out import PolicyOut
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
    api_instance = spatialflow_generated.PoliciesApi(api_client)
    policy_id = 'policy_id_example' # str | 

    try:
        # Get policy detail
        api_response = await api_instance.apps_devices_api_policies_get_policy(policy_id)
        print("The response of PoliciesApi->apps_devices_api_policies_get_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->apps_devices_api_policies_get_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 

### Return type

[**PolicyOut**](PolicyOut.md)

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

# **apps_devices_api_policies_list_policies**
> PolicyListOut apps_devices_api_policies_list_policies(enabled_only=enabled_only, limit=limit, offset=offset)

List policies

List all policies for the current workspace.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.policy_list_out import PolicyListOut
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
    api_instance = spatialflow_generated.PoliciesApi(api_client)
    enabled_only = False # bool |  (optional) (default to False)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # List policies
        api_response = await api_instance.apps_devices_api_policies_list_policies(enabled_only=enabled_only, limit=limit, offset=offset)
        print("The response of PoliciesApi->apps_devices_api_policies_list_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->apps_devices_api_policies_list_policies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled_only** | **bool**|  | [optional] [default to False]
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**PolicyListOut**](PolicyListOut.md)

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

# **apps_devices_api_policies_list_templates**
> List[PolicyTemplateOut] apps_devices_api_policies_list_templates()

List policy templates

List pre-built policy templates.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.policy_template_out import PolicyTemplateOut
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
    api_instance = spatialflow_generated.PoliciesApi(api_client)

    try:
        # List policy templates
        api_response = await api_instance.apps_devices_api_policies_list_templates()
        print("The response of PoliciesApi->apps_devices_api_policies_list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->apps_devices_api_policies_list_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PolicyTemplateOut]**](PolicyTemplateOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

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

# **apps_devices_api_policies_update_policy**
> PolicyOut apps_devices_api_policies_update_policy(policy_id, policy_update_in)

Update policy

Update an existing policy. Requires owner or manager role.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.policy_out import PolicyOut
from spatialflow_generated.models.policy_update_in import PolicyUpdateIn
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
    api_instance = spatialflow_generated.PoliciesApi(api_client)
    policy_id = 'policy_id_example' # str | 
    policy_update_in = spatialflow_generated.PolicyUpdateIn() # PolicyUpdateIn | 

    try:
        # Update policy
        api_response = await api_instance.apps_devices_api_policies_update_policy(policy_id, policy_update_in)
        print("The response of PoliciesApi->apps_devices_api_policies_update_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->apps_devices_api_policies_update_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **str**|  | 
 **policy_update_in** | [**PolicyUpdateIn**](PolicyUpdateIn.md)|  | 

### Return type

[**PolicyOut**](PolicyOut.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

