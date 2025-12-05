# spatialflow_generated.E2ETestApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_test_api_cleanup_test_data**](E2ETestApi.md#apps_test_api_cleanup_test_data) | **POST** /api/v1/test/cleanup-e2e-data | Cleanup Test Data
[**apps_test_api_cleanup_test_data_0**](E2ETestApi.md#apps_test_api_cleanup_test_data_0) | **DELETE** /api/v1/test/cleanup | Cleanup Test Data
[**apps_test_api_create_test_user**](E2ETestApi.md#apps_test_api_create_test_user) | **POST** /api/v1/test/create-user | Create Test User
[**apps_test_api_seed_e2e_data**](E2ETestApi.md#apps_test_api_seed_e2e_data) | **POST** /api/v1/test/seed-e2e-data | Seed E2E Data


# **apps_test_api_cleanup_test_data**
> Dict[str, object] apps_test_api_cleanup_test_data()

Cleanup Test Data

Clean up E2E test data created during test runs.

### Example


```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.E2ETestApi(api_client)

    try:
        # Cleanup Test Data
        api_response = await api_instance.apps_test_api_cleanup_test_data()
        print("The response of E2ETestApi->apps_test_api_cleanup_test_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E2ETestApi->apps_test_api_cleanup_test_data: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_test_api_cleanup_test_data_0**
> Dict[str, object] apps_test_api_cleanup_test_data_0()

Cleanup Test Data

Clean up E2E test data created during test runs.

### Example


```python
import spatialflow_generated
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.E2ETestApi(api_client)

    try:
        # Cleanup Test Data
        api_response = await api_instance.apps_test_api_cleanup_test_data_0()
        print("The response of E2ETestApi->apps_test_api_cleanup_test_data_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E2ETestApi->apps_test_api_cleanup_test_data_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_test_api_create_test_user**
> Dict[str, object] apps_test_api_create_test_user(create_user_schema)

Create Test User

Create a test user for E2E testing.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.create_user_schema import CreateUserSchema
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.E2ETestApi(api_client)
    create_user_schema = spatialflow_generated.CreateUserSchema() # CreateUserSchema | 

    try:
        # Create Test User
        api_response = await api_instance.apps_test_api_create_test_user(create_user_schema)
        print("The response of E2ETestApi->apps_test_api_create_test_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E2ETestApi->apps_test_api_create_test_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_schema** | [**CreateUserSchema**](CreateUserSchema.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_test_api_seed_e2e_data**
> SeedDataResponseSchema apps_test_api_seed_e2e_data()

Seed E2E Data

Seed the database with E2E test data.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.seed_data_response_schema import SeedDataResponseSchema
from spatialflow_generated.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.spatialflow.io
# See configuration.py for a list of all supported configuration parameters.
configuration = spatialflow_generated.Configuration(
    host = "https://api.spatialflow.io"
)


# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.E2ETestApi(api_client)

    try:
        # Seed E2E Data
        api_response = await api_instance.apps_test_api_seed_e2e_data()
        print("The response of E2ETestApi->apps_test_api_seed_e2e_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling E2ETestApi->apps_test_api_seed_e2e_data: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SeedDataResponseSchema**](SeedDataResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

