# spatialflow_generated.IntegrationsApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_integrations_api_bulk_export_integrations**](IntegrationsApi.md#apps_integrations_api_bulk_export_integrations) | **POST** /api/v1/integrations/bulk-export | Bulk Export Integrations
[**apps_integrations_api_bulk_import_integrations**](IntegrationsApi.md#apps_integrations_api_bulk_import_integrations) | **POST** /api/v1/integrations/bulk-import | Bulk Import Integrations
[**apps_integrations_api_create_config_field**](IntegrationsApi.md#apps_integrations_api_create_config_field) | **POST** /api/v1/integrations/admin/integration-types/{integration_type_id}/fields | Create Config Field
[**apps_integrations_api_create_integration**](IntegrationsApi.md#apps_integrations_api_create_integration) | **POST** /api/v1/integrations/ | Create Integration
[**apps_integrations_api_create_integration_type**](IntegrationsApi.md#apps_integrations_api_create_integration_type) | **POST** /api/v1/integrations/admin/integration-types | Create Integration Type
[**apps_integrations_api_delete_config_field**](IntegrationsApi.md#apps_integrations_api_delete_config_field) | **DELETE** /api/v1/integrations/admin/integration-types/{integration_type_id}/fields/{field_id} | Delete Config Field
[**apps_integrations_api_delete_integration**](IntegrationsApi.md#apps_integrations_api_delete_integration) | **DELETE** /api/v1/integrations/{integration_id} | Delete Integration
[**apps_integrations_api_delete_integration_type**](IntegrationsApi.md#apps_integrations_api_delete_integration_type) | **DELETE** /api/v1/integrations/admin/integration-types/{integration_type_id} | Delete Integration Type
[**apps_integrations_api_export_integration**](IntegrationsApi.md#apps_integrations_api_export_integration) | **GET** /api/v1/integrations/{integration_id}/export | Export Integration
[**apps_integrations_api_get_available_integration_types**](IntegrationsApi.md#apps_integrations_api_get_available_integration_types) | **GET** /api/v1/integrations/types/available | Get Available Integration Types
[**apps_integrations_api_get_integration**](IntegrationsApi.md#apps_integrations_api_get_integration) | **GET** /api/v1/integrations/{integration_id} | Get Integration
[**apps_integrations_api_get_integration_error_stats**](IntegrationsApi.md#apps_integrations_api_get_integration_error_stats) | **GET** /api/v1/integrations/error-stats | Get Integration Error Stats
[**apps_integrations_api_get_integration_stats**](IntegrationsApi.md#apps_integrations_api_get_integration_stats) | **GET** /api/v1/integrations/{integration_id}/stats | Get Integration Stats
[**apps_integrations_api_get_integration_type**](IntegrationsApi.md#apps_integrations_api_get_integration_type) | **GET** /api/v1/integrations/admin/integration-types/{integration_type_id} | Get Integration Type
[**apps_integrations_api_import_integration**](IntegrationsApi.md#apps_integrations_api_import_integration) | **POST** /api/v1/integrations/import | Import Integration
[**apps_integrations_api_list_config_fields**](IntegrationsApi.md#apps_integrations_api_list_config_fields) | **GET** /api/v1/integrations/admin/integration-types/{integration_type_id}/fields | List Config Fields
[**apps_integrations_api_list_integration_types**](IntegrationsApi.md#apps_integrations_api_list_integration_types) | **GET** /api/v1/integrations/admin/integration-types | List Integration Types
[**apps_integrations_api_list_integrations**](IntegrationsApi.md#apps_integrations_api_list_integrations) | **GET** /api/v1/integrations/ | List Integrations
[**apps_integrations_api_oauth_authorize**](IntegrationsApi.md#apps_integrations_api_oauth_authorize) | **GET** /api/v1/integrations/{integration_type}/oauth/authorize | Oauth Authorize
[**apps_integrations_api_oauth_callback**](IntegrationsApi.md#apps_integrations_api_oauth_callback) | **POST** /api/v1/integrations/{integration_type}/oauth/callback | Oauth Callback
[**apps_integrations_api_test_bulk_integrations**](IntegrationsApi.md#apps_integrations_api_test_bulk_integrations) | **POST** /api/v1/integrations/test-bulk | Test Bulk Integrations
[**apps_integrations_api_test_integration**](IntegrationsApi.md#apps_integrations_api_test_integration) | **POST** /api/v1/integrations/{integration_id}/test | Test Integration
[**apps_integrations_api_update_config_field**](IntegrationsApi.md#apps_integrations_api_update_config_field) | **PUT** /api/v1/integrations/admin/integration-types/{integration_type_id}/fields/{field_id} | Update Config Field
[**apps_integrations_api_update_integration**](IntegrationsApi.md#apps_integrations_api_update_integration) | **PUT** /api/v1/integrations/{integration_id} | Update Integration
[**apps_integrations_api_update_integration_type**](IntegrationsApi.md#apps_integrations_api_update_integration_type) | **PUT** /api/v1/integrations/admin/integration-types/{integration_type_id} | Update Integration Type


# **apps_integrations_api_bulk_export_integrations**
> List[ExportIntegrationSchema] apps_integrations_api_bulk_export_integrations(include_secrets=include_secrets, request_body=request_body)

Bulk Export Integrations

Export multiple integrations at once.  If integration_ids is not provided, exports all user's integrations.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.export_integration_schema import ExportIntegrationSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    include_secrets = False # bool |  (optional) (default to False)
    request_body = ['request_body_example'] # List[Optional[str]] |  (optional)

    try:
        # Bulk Export Integrations
        api_response = await api_instance.apps_integrations_api_bulk_export_integrations(include_secrets=include_secrets, request_body=request_body)
        print("The response of IntegrationsApi->apps_integrations_api_bulk_export_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_bulk_export_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_secrets** | **bool**|  | [optional] [default to False]
 **request_body** | [**List[Optional[str]]**](str.md)|  | [optional] 

### Return type

[**List[ExportIntegrationSchema]**](ExportIntegrationSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_bulk_import_integrations**
> List[ImportResultSchema] apps_integrations_api_bulk_import_integrations(export_integration_schema, overwrite=overwrite, decrypt_key=decrypt_key)

Bulk Import Integrations

Import multiple integrations at once.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.export_integration_schema import ExportIntegrationSchema
from spatialflow_generated.models.import_result_schema import ImportResultSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    export_integration_schema = [spatialflow_generated.ExportIntegrationSchema()] # List[ExportIntegrationSchema] | 
    overwrite = False # bool |  (optional) (default to False)
    decrypt_key = 'decrypt_key_example' # str |  (optional)

    try:
        # Bulk Import Integrations
        api_response = await api_instance.apps_integrations_api_bulk_import_integrations(export_integration_schema, overwrite=overwrite, decrypt_key=decrypt_key)
        print("The response of IntegrationsApi->apps_integrations_api_bulk_import_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_bulk_import_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_integration_schema** | [**List[ExportIntegrationSchema]**](ExportIntegrationSchema.md)|  | 
 **overwrite** | **bool**|  | [optional] [default to False]
 **decrypt_key** | **str**|  | [optional] 

### Return type

[**List[ImportResultSchema]**](ImportResultSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_create_config_field**
> ConfigFieldDefinitionResponse apps_integrations_api_create_config_field(integration_type_id, config_field_definition_request)

Create Config Field

Create config field for integration type (admin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.config_field_definition_request import ConfigFieldDefinitionRequest
from spatialflow_generated.models.config_field_definition_response import ConfigFieldDefinitionResponse
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_type_id = 'integration_type_id_example' # str | 
    config_field_definition_request = spatialflow_generated.ConfigFieldDefinitionRequest() # ConfigFieldDefinitionRequest | 

    try:
        # Create Config Field
        api_response = await api_instance.apps_integrations_api_create_config_field(integration_type_id, config_field_definition_request)
        print("The response of IntegrationsApi->apps_integrations_api_create_config_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_create_config_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_type_id** | **str**|  | 
 **config_field_definition_request** | [**ConfigFieldDefinitionRequest**](ConfigFieldDefinitionRequest.md)|  | 

### Return type

[**ConfigFieldDefinitionResponse**](ConfigFieldDefinitionResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_create_integration**
> IntegrationDetailSchema apps_integrations_api_create_integration(create_integration_schema)

Create Integration

Create a new integration

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.create_integration_schema import CreateIntegrationSchema
from spatialflow_generated.models.integration_detail_schema import IntegrationDetailSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    create_integration_schema = spatialflow_generated.CreateIntegrationSchema() # CreateIntegrationSchema | 

    try:
        # Create Integration
        api_response = await api_instance.apps_integrations_api_create_integration(create_integration_schema)
        print("The response of IntegrationsApi->apps_integrations_api_create_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_create_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_integration_schema** | [**CreateIntegrationSchema**](CreateIntegrationSchema.md)|  | 

### Return type

[**IntegrationDetailSchema**](IntegrationDetailSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_create_integration_type**
> IntegrationTypeResponse apps_integrations_api_create_integration_type(integration_type_request)

Create Integration Type

Create new integration type (admin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.integration_type_request import IntegrationTypeRequest
from spatialflow_generated.models.integration_type_response import IntegrationTypeResponse
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_type_request = spatialflow_generated.IntegrationTypeRequest() # IntegrationTypeRequest | 

    try:
        # Create Integration Type
        api_response = await api_instance.apps_integrations_api_create_integration_type(integration_type_request)
        print("The response of IntegrationsApi->apps_integrations_api_create_integration_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_create_integration_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_type_request** | [**IntegrationTypeRequest**](IntegrationTypeRequest.md)|  | 

### Return type

[**IntegrationTypeResponse**](IntegrationTypeResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_delete_config_field**
> ActionResponse apps_integrations_api_delete_config_field(integration_type_id, field_id)

Delete Config Field

Delete config field (admin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.action_response import ActionResponse
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_type_id = 'integration_type_id_example' # str | 
    field_id = 'field_id_example' # str | 

    try:
        # Delete Config Field
        api_response = await api_instance.apps_integrations_api_delete_config_field(integration_type_id, field_id)
        print("The response of IntegrationsApi->apps_integrations_api_delete_config_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_delete_config_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_type_id** | **str**|  | 
 **field_id** | **str**|  | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_delete_integration**
> Dict[str, object] apps_integrations_api_delete_integration(integration_id)

Delete Integration

Delete an integration

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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 

    try:
        # Delete Integration
        api_response = await api_instance.apps_integrations_api_delete_integration(integration_id)
        print("The response of IntegrationsApi->apps_integrations_api_delete_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_delete_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_delete_integration_type**
> ActionResponse apps_integrations_api_delete_integration_type(integration_type_id)

Delete Integration Type

Delete integration type (admin only, non-builtin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.action_response import ActionResponse
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_type_id = 'integration_type_id_example' # str | 

    try:
        # Delete Integration Type
        api_response = await api_instance.apps_integrations_api_delete_integration_type(integration_type_id)
        print("The response of IntegrationsApi->apps_integrations_api_delete_integration_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_delete_integration_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_type_id** | **str**|  | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_export_integration**
> ExportIntegrationSchema apps_integrations_api_export_integration(integration_id, include_secrets=include_secrets)

Export Integration

Export integration configuration.  By default, sensitive data is encrypted. Set include_secrets=true to include decrypted sensitive data (use with caution).

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.export_integration_schema import ExportIntegrationSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    include_secrets = False # bool |  (optional) (default to False)

    try:
        # Export Integration
        api_response = await api_instance.apps_integrations_api_export_integration(integration_id, include_secrets=include_secrets)
        print("The response of IntegrationsApi->apps_integrations_api_export_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_export_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **include_secrets** | **bool**|  | [optional] [default to False]

### Return type

[**ExportIntegrationSchema**](ExportIntegrationSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_get_available_integration_types**
> List[Dict[str, object]] apps_integrations_api_get_available_integration_types()

Get Available Integration Types

Get list of available integration types

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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)

    try:
        # Get Available Integration Types
        api_response = await api_instance.apps_integrations_api_get_available_integration_types()
        print("The response of IntegrationsApi->apps_integrations_api_get_available_integration_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_get_available_integration_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Dict[str, object]]**

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_get_integration**
> IntegrationDetailSchema apps_integrations_api_get_integration(integration_id)

Get Integration

Get integration details

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.integration_detail_schema import IntegrationDetailSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 

    try:
        # Get Integration
        api_response = await api_instance.apps_integrations_api_get_integration(integration_id)
        print("The response of IntegrationsApi->apps_integrations_api_get_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_get_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 

### Return type

[**IntegrationDetailSchema**](IntegrationDetailSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_get_integration_error_stats**
> Dict[str, object] apps_integrations_api_get_integration_error_stats()

Get Integration Error Stats

Get integration error statistics for the dashboard health strip.  Returns count of failed integration usage logs in the last 24 hours and timestamp of the most recent error.  Returns:     200: Error statistics     401: Unauthorized - invalid or missing authentication  Example:     GET /api/v1/integrations/error-stats     Response: { \"error_count_24h\": 5, \"last_error_at\": \"2025-10-05T12:34:56Z\" }

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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)

    try:
        # Get Integration Error Stats
        api_response = await api_instance.apps_integrations_api_get_integration_error_stats()
        print("The response of IntegrationsApi->apps_integrations_api_get_integration_error_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_get_integration_error_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_get_integration_stats**
> IntegrationStatsSchema apps_integrations_api_get_integration_stats(integration_id)

Get Integration Stats

Get usage statistics for an integration

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.integration_stats_schema import IntegrationStatsSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 

    try:
        # Get Integration Stats
        api_response = await api_instance.apps_integrations_api_get_integration_stats(integration_id)
        print("The response of IntegrationsApi->apps_integrations_api_get_integration_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_get_integration_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 

### Return type

[**IntegrationStatsSchema**](IntegrationStatsSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_get_integration_type**
> IntegrationTypeResponse apps_integrations_api_get_integration_type(integration_type_id)

Get Integration Type

Get specific integration type (admin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.integration_type_response import IntegrationTypeResponse
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_type_id = 'integration_type_id_example' # str | 

    try:
        # Get Integration Type
        api_response = await api_instance.apps_integrations_api_get_integration_type(integration_type_id)
        print("The response of IntegrationsApi->apps_integrations_api_get_integration_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_get_integration_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_type_id** | **str**|  | 

### Return type

[**IntegrationTypeResponse**](IntegrationTypeResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_import_integration**
> ImportResultSchema apps_integrations_api_import_integration(import_integration_schema)

Import Integration

Import integration from exported data.  If an integration with the same name exists: - Set overwrite=true to replace it - Set overwrite=false to create with a new name (default)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.import_integration_schema import ImportIntegrationSchema
from spatialflow_generated.models.import_result_schema import ImportResultSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    import_integration_schema = spatialflow_generated.ImportIntegrationSchema() # ImportIntegrationSchema | 

    try:
        # Import Integration
        api_response = await api_instance.apps_integrations_api_import_integration(import_integration_schema)
        print("The response of IntegrationsApi->apps_integrations_api_import_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_import_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_integration_schema** | [**ImportIntegrationSchema**](ImportIntegrationSchema.md)|  | 

### Return type

[**ImportResultSchema**](ImportResultSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_list_config_fields**
> List[ConfigFieldDefinitionResponse] apps_integrations_api_list_config_fields(integration_type_id)

List Config Fields

List config fields for an integration type (admin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.config_field_definition_response import ConfigFieldDefinitionResponse
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_type_id = 'integration_type_id_example' # str | 

    try:
        # List Config Fields
        api_response = await api_instance.apps_integrations_api_list_config_fields(integration_type_id)
        print("The response of IntegrationsApi->apps_integrations_api_list_config_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_list_config_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_type_id** | **str**|  | 

### Return type

[**List[ConfigFieldDefinitionResponse]**](ConfigFieldDefinitionResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_list_integration_types**
> IntegrationTypeListResponse apps_integrations_api_list_integration_types(page=page, page_size=page_size, category=category, is_active=is_active, search=search)

List Integration Types

List all integration types (admin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.integration_type_list_response import IntegrationTypeListResponse
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    category = 'category_example' # str |  (optional)
    is_active = True # bool |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # List Integration Types
        api_response = await api_instance.apps_integrations_api_list_integration_types(page=page, page_size=page_size, category=category, is_active=is_active, search=search)
        print("The response of IntegrationsApi->apps_integrations_api_list_integration_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_list_integration_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **category** | **str**|  | [optional] 
 **is_active** | **bool**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**IntegrationTypeListResponse**](IntegrationTypeListResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_list_integrations**
> List[IntegrationResponseSchema] apps_integrations_api_list_integrations(type=type, is_active=is_active, is_verified=is_verified, search=search)

List Integrations

List user's integrations with optional filtering

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.integration_response_schema import IntegrationResponseSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    type = 'type_example' # str |  (optional)
    is_active = True # bool |  (optional)
    is_verified = True # bool |  (optional)
    search = 'search_example' # str |  (optional)

    try:
        # List Integrations
        api_response = await api_instance.apps_integrations_api_list_integrations(type=type, is_active=is_active, is_verified=is_verified, search=search)
        print("The response of IntegrationsApi->apps_integrations_api_list_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_list_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **is_active** | **bool**|  | [optional] 
 **is_verified** | **bool**|  | [optional] 
 **search** | **str**|  | [optional] 

### Return type

[**List[IntegrationResponseSchema]**](IntegrationResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_oauth_authorize**
> apps_integrations_api_oauth_authorize(integration_type)

Oauth Authorize

Initiate OAuth flow for an integration

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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_type = 'integration_type_example' # str | 

    try:
        # Oauth Authorize
        await api_instance.apps_integrations_api_oauth_authorize(integration_type)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_oauth_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_oauth_callback**
> apps_integrations_api_oauth_callback(integration_type, code, state)

Oauth Callback

Handle OAuth callback

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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_type = 'integration_type_example' # str | 
    code = 'code_example' # str | 
    state = 'state_example' # str | 

    try:
        # Oauth Callback
        await api_instance.apps_integrations_api_oauth_callback(integration_type, code, state)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_oauth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_type** | **str**|  | 
 **code** | **str**|  | 
 **state** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_test_bulk_integrations**
> List[TestIntegrationResponseSchema] apps_integrations_api_test_bulk_integrations()

Test Bulk Integrations

Test all active integrations for the user

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.test_integration_response_schema import TestIntegrationResponseSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)

    try:
        # Test Bulk Integrations
        api_response = await api_instance.apps_integrations_api_test_bulk_integrations()
        print("The response of IntegrationsApi->apps_integrations_api_test_bulk_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_test_bulk_integrations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TestIntegrationResponseSchema]**](TestIntegrationResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_test_integration**
> TestIntegrationResponseSchema apps_integrations_api_test_integration(integration_id)

Test Integration

Test an integration to verify it works

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.test_integration_response_schema import TestIntegrationResponseSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 

    try:
        # Test Integration
        api_response = await api_instance.apps_integrations_api_test_integration(integration_id)
        print("The response of IntegrationsApi->apps_integrations_api_test_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_test_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 

### Return type

[**TestIntegrationResponseSchema**](TestIntegrationResponseSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_update_config_field**
> ConfigFieldDefinitionResponse apps_integrations_api_update_config_field(integration_type_id, field_id, config_field_definition_request)

Update Config Field

Update config field (admin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.config_field_definition_request import ConfigFieldDefinitionRequest
from spatialflow_generated.models.config_field_definition_response import ConfigFieldDefinitionResponse
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_type_id = 'integration_type_id_example' # str | 
    field_id = 'field_id_example' # str | 
    config_field_definition_request = spatialflow_generated.ConfigFieldDefinitionRequest() # ConfigFieldDefinitionRequest | 

    try:
        # Update Config Field
        api_response = await api_instance.apps_integrations_api_update_config_field(integration_type_id, field_id, config_field_definition_request)
        print("The response of IntegrationsApi->apps_integrations_api_update_config_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_update_config_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_type_id** | **str**|  | 
 **field_id** | **str**|  | 
 **config_field_definition_request** | [**ConfigFieldDefinitionRequest**](ConfigFieldDefinitionRequest.md)|  | 

### Return type

[**ConfigFieldDefinitionResponse**](ConfigFieldDefinitionResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_update_integration**
> IntegrationDetailSchema apps_integrations_api_update_integration(integration_id, update_integration_schema)

Update Integration

Update an integration

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.integration_detail_schema import IntegrationDetailSchema
from spatialflow_generated.models.update_integration_schema import UpdateIntegrationSchema
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_id = 'integration_id_example' # str | 
    update_integration_schema = spatialflow_generated.UpdateIntegrationSchema() # UpdateIntegrationSchema | 

    try:
        # Update Integration
        api_response = await api_instance.apps_integrations_api_update_integration(integration_id, update_integration_schema)
        print("The response of IntegrationsApi->apps_integrations_api_update_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_update_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  | 
 **update_integration_schema** | [**UpdateIntegrationSchema**](UpdateIntegrationSchema.md)|  | 

### Return type

[**IntegrationDetailSchema**](IntegrationDetailSchema.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_integrations_api_update_integration_type**
> IntegrationTypeResponse apps_integrations_api_update_integration_type(integration_type_id, integration_type_request)

Update Integration Type

Update integration type (admin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.integration_type_request import IntegrationTypeRequest
from spatialflow_generated.models.integration_type_response import IntegrationTypeResponse
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
    api_instance = spatialflow_generated.IntegrationsApi(api_client)
    integration_type_id = 'integration_type_id_example' # str | 
    integration_type_request = spatialflow_generated.IntegrationTypeRequest() # IntegrationTypeRequest | 

    try:
        # Update Integration Type
        api_response = await api_instance.apps_integrations_api_update_integration_type(integration_type_id, integration_type_request)
        print("The response of IntegrationsApi->apps_integrations_api_update_integration_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationsApi->apps_integrations_api_update_integration_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_type_id** | **str**|  | 
 **integration_type_request** | [**IntegrationTypeRequest**](IntegrationTypeRequest.md)|  | 

### Return type

[**IntegrationTypeResponse**](IntegrationTypeResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

