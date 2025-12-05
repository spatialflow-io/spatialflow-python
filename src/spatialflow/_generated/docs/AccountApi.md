# spatialflow_generated.AccountApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_accounts_api_account_health_check**](AccountApi.md#apps_accounts_api_account_health_check) | **GET** /api/v1/account/health | Account Health Check
[**apps_accounts_api_create_api_key**](AccountApi.md#apps_accounts_api_create_api_key) | **POST** /api/v1/account/api-keys | Create Api Key
[**apps_accounts_api_create_erasure_job**](AccountApi.md#apps_accounts_api_create_erasure_job) | **POST** /api/v1/account/privacy/erasure | Create Erasure Job
[**apps_accounts_api_delete_api_key**](AccountApi.md#apps_accounts_api_delete_api_key) | **DELETE** /api/v1/account/api-keys/{api_key_id} | Delete Api Key
[**apps_accounts_api_dismiss_onboarding**](AccountApi.md#apps_accounts_api_dismiss_onboarding) | **POST** /api/v1/account/onboarding/dismiss | Dismiss Onboarding
[**apps_accounts_api_get_api_key**](AccountApi.md#apps_accounts_api_get_api_key) | **GET** /api/v1/account/api-keys/{api_key_id} | Get Api Key
[**apps_accounts_api_get_api_keys**](AccountApi.md#apps_accounts_api_get_api_keys) | **GET** /api/v1/account/api-keys | Get Api Keys
[**apps_accounts_api_get_dashboard_metrics**](AccountApi.md#apps_accounts_api_get_dashboard_metrics) | **GET** /api/v1/account/dashboard/metrics | Get Dashboard Metrics
[**apps_accounts_api_get_erasure_job**](AccountApi.md#apps_accounts_api_get_erasure_job) | **GET** /api/v1/account/privacy/erasure/{job_id} | Get Erasure Job
[**apps_accounts_api_get_notifications**](AccountApi.md#apps_accounts_api_get_notifications) | **GET** /api/v1/account/notifications | Get Notifications
[**apps_accounts_api_get_onboarding_progress**](AccountApi.md#apps_accounts_api_get_onboarding_progress) | **GET** /api/v1/account/onboarding/progress | Get Onboarding Progress
[**apps_accounts_api_get_user_profile**](AccountApi.md#apps_accounts_api_get_user_profile) | **GET** /api/v1/account/me | Get User Profile
[**apps_accounts_api_list_expiring_api_keys**](AccountApi.md#apps_accounts_api_list_expiring_api_keys) | **GET** /api/v1/account/api-keys/expiring | List Expiring Api Keys
[**apps_accounts_api_mark_all_notifications_read**](AccountApi.md#apps_accounts_api_mark_all_notifications_read) | **POST** /api/v1/account/notifications/read-all | Mark All Notifications Read
[**apps_accounts_api_mark_notification_read**](AccountApi.md#apps_accounts_api_mark_notification_read) | **POST** /api/v1/account/notifications/{notification_id}/read | Mark Notification Read
[**apps_accounts_api_regenerate_api_key**](AccountApi.md#apps_accounts_api_regenerate_api_key) | **POST** /api/v1/account/api-keys/{api_key_id}/regenerate | Regenerate Api Key
[**apps_accounts_api_rotate_api_key**](AccountApi.md#apps_accounts_api_rotate_api_key) | **POST** /api/v1/account/api-keys/{api_key_id}/rotate | Rotate Api Key
[**apps_accounts_api_set_api_key_expiration**](AccountApi.md#apps_accounts_api_set_api_key_expiration) | **PATCH** /api/v1/account/api-keys/{api_key_id}/expiration | Set Api Key Expiration
[**apps_accounts_api_update_api_key**](AccountApi.md#apps_accounts_api_update_api_key) | **PUT** /api/v1/account/api-keys/{api_key_id} | Update Api Key
[**apps_accounts_api_update_onboarding_progress**](AccountApi.md#apps_accounts_api_update_onboarding_progress) | **POST** /api/v1/account/onboarding/progress | Update Onboarding Progress
[**apps_accounts_api_update_user_profile**](AccountApi.md#apps_accounts_api_update_user_profile) | **PUT** /api/v1/account/me | Update User Profile


# **apps_accounts_api_account_health_check**
> apps_accounts_api_account_health_check()

Account Health Check

Health check endpoint for account service.

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
    api_instance = spatialflow_generated.AccountApi(api_client)

    try:
        # Account Health Check
        await api_instance.apps_accounts_api_account_health_check()
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_account_health_check: %s\n" % e)
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

# **apps_accounts_api_create_api_key**
> ApiKeyCreateResponse apps_accounts_api_create_api_key(api_key_create_request)

Create Api Key

Generate a new API key for the authenticated user.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.api_key_create_request import ApiKeyCreateRequest
from spatialflow_generated.models.api_key_create_response import ApiKeyCreateResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    api_key_create_request = spatialflow_generated.ApiKeyCreateRequest() # ApiKeyCreateRequest | 

    try:
        # Create Api Key
        api_response = await api_instance.apps_accounts_api_create_api_key(api_key_create_request)
        print("The response of AccountApi->apps_accounts_api_create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_create_request** | [**ApiKeyCreateRequest**](ApiKeyCreateRequest.md)|  | 

### Return type

[**ApiKeyCreateResponse**](ApiKeyCreateResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_accounts_api_create_erasure_job**
> PrivacyErasureResponse apps_accounts_api_create_erasure_job(privacy_erasure_request)

Create Erasure Job

Create a privacy data erasure job (GDPR compliance).  This endpoint allows workspace owners and admins to delete location and event data for GDPR Article 17 (Right to be Forgotten) compliance.  **Authentication:** JWT token required **Authorization:** Owner or Admin role only  **Scope Options:** - `workspace`: Delete all data for the workspace - `device`: Delete data for specific devices (requires device_ids) - `date_range`: Delete data within a time range (requires from_date and to_date) - `tag`: Delete data with specific tags (requires tags)  **Dry Run Mode:** Set `dry_run: true` to estimate deletions without actually deleting data. Always run dry-run first to verify the scope.  **Example:** ```json {     \"scope\": \"device\",     \"device_ids\": [\"truck-005\", \"truck-009\"],     \"from_date\": \"2024-01-01T00:00:00Z\",     \"to_date\": \"2024-12-31T23:59:59Z\",     \"dry_run\": true } ```  **PRD Reference:** §4.5 Privacy Erasure API **Roadmap:** Phase 2, Task 2.1

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.privacy_erasure_request import PrivacyErasureRequest
from spatialflow_generated.models.privacy_erasure_response import PrivacyErasureResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    privacy_erasure_request = spatialflow_generated.PrivacyErasureRequest() # PrivacyErasureRequest | 

    try:
        # Create Erasure Job
        api_response = await api_instance.apps_accounts_api_create_erasure_job(privacy_erasure_request)
        print("The response of AccountApi->apps_accounts_api_create_erasure_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_create_erasure_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privacy_erasure_request** | [**PrivacyErasureRequest**](PrivacyErasureRequest.md)|  | 

### Return type

[**PrivacyErasureResponse**](PrivacyErasureResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_accounts_api_delete_api_key**
> Dict[str, object] apps_accounts_api_delete_api_key(api_key_id)

Delete Api Key

Delete a specific API key.

### Example

* Api Key Authentication (APIKeyBearer):
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    api_key_id = 'api_key_id_example' # str | 

    try:
        # Delete Api Key
        api_response = await api_instance.apps_accounts_api_delete_api_key(api_key_id)
        print("The response of AccountApi->apps_accounts_api_delete_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_accounts_api_dismiss_onboarding**
> OnboardingProgressResponse apps_accounts_api_dismiss_onboarding()

Dismiss Onboarding

Dismiss the onboarding checklist.  Permanently hides the onboarding checklist card for the user. This action cannot be undone via API.  **Authentication:** JWT token required

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.onboarding_progress_response import OnboardingProgressResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)

    try:
        # Dismiss Onboarding
        api_response = await api_instance.apps_accounts_api_dismiss_onboarding()
        print("The response of AccountApi->apps_accounts_api_dismiss_onboarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_dismiss_onboarding: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OnboardingProgressResponse**](OnboardingProgressResponse.md)

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

# **apps_accounts_api_get_api_key**
> ApiKeyResponse apps_accounts_api_get_api_key(api_key_id)

Get Api Key

Get a specific API key by its ID.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.api_key_response import ApiKeyResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    api_key_id = 'api_key_id_example' # str | 

    try:
        # Get Api Key
        api_response = await api_instance.apps_accounts_api_get_api_key(api_key_id)
        print("The response of AccountApi->apps_accounts_api_get_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_get_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 

### Return type

[**ApiKeyResponse**](ApiKeyResponse.md)

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

# **apps_accounts_api_get_api_keys**
> List[ApiKeyResponse] apps_accounts_api_get_api_keys()

Get Api Keys

Get all API keys for the authenticated user.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.api_key_response import ApiKeyResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)

    try:
        # Get Api Keys
        api_response = await api_instance.apps_accounts_api_get_api_keys()
        print("The response of AccountApi->apps_accounts_api_get_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_get_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiKeyResponse]**](ApiKeyResponse.md)

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

# **apps_accounts_api_get_dashboard_metrics**
> DashboardMetricsResponse apps_accounts_api_get_dashboard_metrics(time_range=time_range, start_date=start_date, end_date=end_date)

Get Dashboard Metrics

Get dashboard KPI metrics for the authenticated user.  Returns key performance indicators for the dashboard: - **Active Workflows**: Workflows that are active and were created or executed in the period - **Events Total**: Total geofence entry/exit events triggered in the period - **Action Delivery Success**: Success rate for webhook deliveries and workflow step executions (north-star metric)  **Time Ranges:** - `today`: From midnight to now - `7d`: Last 7 days - `30d`: Last 30 days - `custom`: Custom date range (requires start_date and end_date)  **Formulas:** - Action Delivery Success Rate = (successful_deliveries / total_attempts) * 100 - Returns `null` when total_attempts = 0 (UI should show \"—\")  **Authentication:** JWT token required  **Example:** ``` GET /api/v1/accounts/dashboard/metrics?time_range=7d GET /api/v1/accounts/dashboard/metrics?time_range=custom&start_date=2025-01-01T00:00:00Z&end_date=2025-01-31T23:59:59Z ```  **Dashboard UX:** Ticket #2 - Global Time-Range Control + KPI Formulas

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.dashboard_metrics_response import DashboardMetricsResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    time_range = 'today' # str | Time range: today, 7d, 30d, or custom (optional) (default to 'today')
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Custom start date (ISO 8601, required if time_range=custom) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Custom end date (ISO 8601, required if time_range=custom) (optional)

    try:
        # Get Dashboard Metrics
        api_response = await api_instance.apps_accounts_api_get_dashboard_metrics(time_range=time_range, start_date=start_date, end_date=end_date)
        print("The response of AccountApi->apps_accounts_api_get_dashboard_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_get_dashboard_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_range** | **str**| Time range: today, 7d, 30d, or custom | [optional] [default to &#39;today&#39;]
 **start_date** | **datetime**| Custom start date (ISO 8601, required if time_range&#x3D;custom) | [optional] 
 **end_date** | **datetime**| Custom end date (ISO 8601, required if time_range&#x3D;custom) | [optional] 

### Return type

[**DashboardMetricsResponse**](DashboardMetricsResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_accounts_api_get_erasure_job**
> PrivacyErasureResponse apps_accounts_api_get_erasure_job(job_id)

Get Erasure Job

Get status of a privacy erasure job.  Returns the current status, progress, and results of an erasure job. Poll this endpoint to track job execution.  **Authentication:** JWT token required **Authorization:** Must be in the same workspace as the job  **Job Statuses:** - `pending`: Job queued, not yet started - `running`: Job is executing - `completed`: Job finished successfully - `failed`: Job encountered an error  **PRD Reference:** §4.5 Privacy Erasure API

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.privacy_erasure_response import PrivacyErasureResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Get Erasure Job
        api_response = await api_instance.apps_accounts_api_get_erasure_job(job_id)
        print("The response of AccountApi->apps_accounts_api_get_erasure_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_get_erasure_job: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**PrivacyErasureResponse**](PrivacyErasureResponse.md)

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

# **apps_accounts_api_get_notifications**
> apps_accounts_api_get_notifications(unread_only=unread_only)

Get Notifications

Get user notifications.

### Example

* Api Key Authentication (APIKeyBearer):
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    unread_only = False # bool |  (optional) (default to False)

    try:
        # Get Notifications
        await api_instance.apps_accounts_api_get_notifications(unread_only=unread_only)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_get_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unread_only** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_accounts_api_get_onboarding_progress**
> OnboardingProgressResponse apps_accounts_api_get_onboarding_progress()

Get Onboarding Progress

Get current user's onboarding checklist progress.  Returns the user's progress through the onboarding checklist steps, including which steps are complete and overall completion percentage.  **Authentication:** JWT token required

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.onboarding_progress_response import OnboardingProgressResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)

    try:
        # Get Onboarding Progress
        api_response = await api_instance.apps_accounts_api_get_onboarding_progress()
        print("The response of AccountApi->apps_accounts_api_get_onboarding_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_get_onboarding_progress: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OnboardingProgressResponse**](OnboardingProgressResponse.md)

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

# **apps_accounts_api_get_user_profile**
> UserProfileResponse apps_accounts_api_get_user_profile()

Get User Profile

Get current user profile information.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_profile_response import UserProfileResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)

    try:
        # Get User Profile
        api_response = await api_instance.apps_accounts_api_get_user_profile()
        print("The response of AccountApi->apps_accounts_api_get_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_get_user_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserProfileResponse**](UserProfileResponse.md)

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

# **apps_accounts_api_list_expiring_api_keys**
> List[Dict[str, object]] apps_accounts_api_list_expiring_api_keys(days=days)

List Expiring Api Keys

List API keys expiring within the specified number of days.  Default: 30 days

### Example

* Api Key Authentication (APIKeyBearer):
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    days = 30 # int |  (optional) (default to 30)

    try:
        # List Expiring Api Keys
        api_response = await api_instance.apps_accounts_api_list_expiring_api_keys(days=days)
        print("The response of AccountApi->apps_accounts_api_list_expiring_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_list_expiring_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] [default to 30]

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

# **apps_accounts_api_mark_all_notifications_read**
> Dict[str, object] apps_accounts_api_mark_all_notifications_read()

Mark All Notifications Read

Mark all notifications as read.

### Example

* Api Key Authentication (APIKeyBearer):
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
    api_instance = spatialflow_generated.AccountApi(api_client)

    try:
        # Mark All Notifications Read
        api_response = await api_instance.apps_accounts_api_mark_all_notifications_read()
        print("The response of AccountApi->apps_accounts_api_mark_all_notifications_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_mark_all_notifications_read: %s\n" % e)
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

# **apps_accounts_api_mark_notification_read**
> Dict[str, object] apps_accounts_api_mark_notification_read(notification_id)

Mark Notification Read

Mark a notification as read.

### Example

* Api Key Authentication (APIKeyBearer):
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    notification_id = 'notification_id_example' # str | 

    try:
        # Mark Notification Read
        api_response = await api_instance.apps_accounts_api_mark_notification_read(notification_id)
        print("The response of AccountApi->apps_accounts_api_mark_notification_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_mark_notification_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **str**|  | 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_accounts_api_regenerate_api_key**
> ApiKeyCreateResponse apps_accounts_api_regenerate_api_key(api_key_id)

Regenerate Api Key

Regenerate an existing API key.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.api_key_create_response import ApiKeyCreateResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    api_key_id = 'api_key_id_example' # str | 

    try:
        # Regenerate Api Key
        api_response = await api_instance.apps_accounts_api_regenerate_api_key(api_key_id)
        print("The response of AccountApi->apps_accounts_api_regenerate_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_regenerate_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 

### Return type

[**ApiKeyCreateResponse**](ApiKeyCreateResponse.md)

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

# **apps_accounts_api_rotate_api_key**
> ApiKeyCreateResponse apps_accounts_api_rotate_api_key(api_key_id, grace_period_days=grace_period_days)

Rotate Api Key

Rotate an API key.  Creates a new API key with the same permissions and marks the old one for expiration. The old key remains active for the grace period (default 7 days).

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.api_key_create_response import ApiKeyCreateResponse
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    api_key_id = 'api_key_id_example' # str | 
    grace_period_days = 7 # int |  (optional) (default to 7)

    try:
        # Rotate Api Key
        api_response = await api_instance.apps_accounts_api_rotate_api_key(api_key_id, grace_period_days=grace_period_days)
        print("The response of AccountApi->apps_accounts_api_rotate_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_rotate_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 
 **grace_period_days** | **int**|  | [optional] [default to 7]

### Return type

[**ApiKeyCreateResponse**](ApiKeyCreateResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_accounts_api_set_api_key_expiration**
> Dict[str, Optional[str]] apps_accounts_api_set_api_key_expiration(api_key_id, expires_at=expires_at)

Set Api Key Expiration

Set or update expiration date for an API key.  Pass expires_at as ISO 8601 datetime string or null to remove expiration.

### Example

* Api Key Authentication (APIKeyBearer):
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    api_key_id = 'api_key_id_example' # str | 
    expires_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Set Api Key Expiration
        api_response = await api_instance.apps_accounts_api_set_api_key_expiration(api_key_id, expires_at=expires_at)
        print("The response of AccountApi->apps_accounts_api_set_api_key_expiration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_set_api_key_expiration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 
 **expires_at** | **datetime**|  | [optional] 

### Return type

**Dict[str, Optional[str]]**

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

# **apps_accounts_api_update_api_key**
> Dict[str, object] apps_accounts_api_update_api_key(api_key_id, api_key_update_request)

Update Api Key

Update an API key's settings.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.api_key_update_request import ApiKeyUpdateRequest
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    api_key_id = 'api_key_id_example' # str | 
    api_key_update_request = spatialflow_generated.ApiKeyUpdateRequest() # ApiKeyUpdateRequest | 

    try:
        # Update Api Key
        api_response = await api_instance.apps_accounts_api_update_api_key(api_key_id, api_key_update_request)
        print("The response of AccountApi->apps_accounts_api_update_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_update_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **str**|  | 
 **api_key_update_request** | [**ApiKeyUpdateRequest**](ApiKeyUpdateRequest.md)|  | 

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
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_accounts_api_update_onboarding_progress**
> OnboardingProgressResponse apps_accounts_api_update_onboarding_progress(update_onboarding_progress_request)

Update Onboarding Progress

Update onboarding progress by marking a step as complete.  Marks the specified onboarding step as complete. If all steps are complete, automatically sets the completed_at timestamp.  **Authentication:** JWT token required  **Example:** ```json {     \"step\": \"created_workflow\" } ```

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.onboarding_progress_response import OnboardingProgressResponse
from spatialflow_generated.models.update_onboarding_progress_request import UpdateOnboardingProgressRequest
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    update_onboarding_progress_request = spatialflow_generated.UpdateOnboardingProgressRequest() # UpdateOnboardingProgressRequest | 

    try:
        # Update Onboarding Progress
        api_response = await api_instance.apps_accounts_api_update_onboarding_progress(update_onboarding_progress_request)
        print("The response of AccountApi->apps_accounts_api_update_onboarding_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_update_onboarding_progress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_onboarding_progress_request** | [**UpdateOnboardingProgressRequest**](UpdateOnboardingProgressRequest.md)|  | 

### Return type

[**OnboardingProgressResponse**](OnboardingProgressResponse.md)

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

# **apps_accounts_api_update_user_profile**
> Dict[str, object] apps_accounts_api_update_user_profile(update_profile_request)

Update User Profile

Update current user profile information.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.update_profile_request import UpdateProfileRequest
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
    api_instance = spatialflow_generated.AccountApi(api_client)
    update_profile_request = spatialflow_generated.UpdateProfileRequest() # UpdateProfileRequest | 

    try:
        # Update User Profile
        api_response = await api_instance.apps_accounts_api_update_user_profile(update_profile_request)
        print("The response of AccountApi->apps_accounts_api_update_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->apps_accounts_api_update_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_profile_request** | [**UpdateProfileRequest**](UpdateProfileRequest.md)|  | 

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
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

