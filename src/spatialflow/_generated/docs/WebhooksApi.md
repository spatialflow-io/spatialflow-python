# spatialflow_generated.WebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_webhooks_api_create_webhook**](WebhooksApi.md#apps_webhooks_api_create_webhook) | **POST** /api/v1/webhooks/ | Create Webhook
[**apps_webhooks_api_delete_webhook**](WebhooksApi.md#apps_webhooks_api_delete_webhook) | **DELETE** /api/v1/webhooks/{webhook_id} | Delete Webhook
[**apps_webhooks_api_get_dlq_stats**](WebhooksApi.md#apps_webhooks_api_get_dlq_stats) | **GET** /api/v1/webhooks/dlq/stats | Get Dlq Stats
[**apps_webhooks_api_get_webhook**](WebhooksApi.md#apps_webhooks_api_get_webhook) | **GET** /api/v1/webhooks/{webhook_id} | Get Webhook
[**apps_webhooks_api_get_webhook_deliveries**](WebhooksApi.md#apps_webhooks_api_get_webhook_deliveries) | **GET** /api/v1/webhooks/{webhook_id}/deliveries | Get Webhook Deliveries
[**apps_webhooks_api_get_webhook_delivery_detail**](WebhooksApi.md#apps_webhooks_api_get_webhook_delivery_detail) | **GET** /api/v1/webhooks/{webhook_id}/deliveries/{delivery_id} | Get Webhook Delivery Detail
[**apps_webhooks_api_get_webhook_metrics**](WebhooksApi.md#apps_webhooks_api_get_webhook_metrics) | **GET** /api/v1/webhooks/metrics | Get Webhook Metrics
[**apps_webhooks_api_get_webhook_success_timeline**](WebhooksApi.md#apps_webhooks_api_get_webhook_success_timeline) | **GET** /api/v1/webhooks/success-timeline | Get Webhook Success Timeline
[**apps_webhooks_api_list_dlq_entries**](WebhooksApi.md#apps_webhooks_api_list_dlq_entries) | **GET** /api/v1/webhooks/dlq | List Dlq Entries
[**apps_webhooks_api_list_webhooks**](WebhooksApi.md#apps_webhooks_api_list_webhooks) | **GET** /api/v1/webhooks/ | List Webhooks
[**apps_webhooks_api_receive_webhook**](WebhooksApi.md#apps_webhooks_api_receive_webhook) | **POST** /api/v1/webhooks/receive/{webhook_id} | Receive Webhook
[**apps_webhooks_api_retry_from_dlq**](WebhooksApi.md#apps_webhooks_api_retry_from_dlq) | **POST** /api/v1/webhooks/dlq/{dlq_id}/retry | Retry From Dlq
[**apps_webhooks_api_retry_webhook_delivery**](WebhooksApi.md#apps_webhooks_api_retry_webhook_delivery) | **POST** /api/v1/webhooks/{webhook_id}/deliveries/{delivery_id}/retry | Retry Webhook Delivery
[**apps_webhooks_api_test_webhook**](WebhooksApi.md#apps_webhooks_api_test_webhook) | **POST** /api/v1/webhooks/{webhook_id}/test | Test Webhook
[**apps_webhooks_api_update_webhook**](WebhooksApi.md#apps_webhooks_api_update_webhook) | **PUT** /api/v1/webhooks/{webhook_id} | Update Webhook
[**apps_webhooks_api_webhook_health_check**](WebhooksApi.md#apps_webhooks_api_webhook_health_check) | **GET** /api/v1/webhooks/health | Webhook Health Check


# **apps_webhooks_api_create_webhook**
> WebhookResponse apps_webhooks_api_create_webhook(create_webhook_request)

Create Webhook

Create a new webhook endpoint.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.create_webhook_request import CreateWebhookRequest
from spatialflow_generated.models.webhook_response import WebhookResponse
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
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    create_webhook_request = spatialflow_generated.CreateWebhookRequest() # CreateWebhookRequest | 

    try:
        # Create Webhook
        api_response = await api_instance.apps_webhooks_api_create_webhook(create_webhook_request)
        print("The response of WebhooksApi->apps_webhooks_api_create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

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
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_delete_webhook**
> SuccessResponse apps_webhooks_api_delete_webhook(webhook_id)

Delete Webhook

Delete a webhook.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.success_response import SuccessResponse
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
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    webhook_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Webhook
        api_response = await api_instance.apps_webhooks_api_delete_webhook(webhook_id)
        print("The response of WebhooksApi->apps_webhooks_api_delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **UUID**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_get_dlq_stats**
> Dict[str, object] apps_webhooks_api_get_dlq_stats()

Get Dlq Stats

Get Dead Letter Queue statistics for the workspace.

Returns aggregated metrics about failed webhook deliveries including
total entries, requeued count, and breakdown by webhook.

Returns:
    200: DLQ statistics
    401: Unauthorized - invalid or missing authentication

Example:
    GET /api/v1/webhooks/dlq/stats

### Example

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

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.WebhooksApi(api_client)

    try:
        # Get Dlq Stats
        api_response = await api_instance.apps_webhooks_api_get_dlq_stats()
        print("The response of WebhooksApi->apps_webhooks_api_get_dlq_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_get_dlq_stats: %s\n" % e)
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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_get_webhook**
> WebhookResponse apps_webhooks_api_get_webhook(webhook_id)

Get Webhook

Get a specific webhook by ID.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.webhook_response import WebhookResponse
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
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    webhook_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Webhook
        api_response = await api_instance.apps_webhooks_api_get_webhook(webhook_id)
        print("The response of WebhooksApi->apps_webhooks_api_get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **UUID**|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_get_webhook_deliveries**
> WebhookDeliveryListResponse apps_webhooks_api_get_webhook_deliveries(webhook_id, limit=limit, offset=offset, status=status, event_type=event_type)

Get Webhook Deliveries

Get delivery history for a webhook.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.webhook_delivery_list_response import WebhookDeliveryListResponse
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
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    webhook_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    status = 'status_example' # str |  (optional)
    event_type = 'event_type_example' # str |  (optional)

    try:
        # Get Webhook Deliveries
        api_response = await api_instance.apps_webhooks_api_get_webhook_deliveries(webhook_id, limit=limit, offset=offset, status=status, event_type=event_type)
        print("The response of WebhooksApi->apps_webhooks_api_get_webhook_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_get_webhook_deliveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **UUID**|  | 
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **status** | **str**|  | [optional] 
 **event_type** | **str**|  | [optional] 

### Return type

[**WebhookDeliveryListResponse**](WebhookDeliveryListResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_get_webhook_delivery_detail**
> WebhookDeliveryDetailResponse apps_webhooks_api_get_webhook_delivery_detail(webhook_id, delivery_id)

Get Webhook Delivery Detail

Get detailed delivery information.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.webhook_delivery_detail_response import WebhookDeliveryDetailResponse
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
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    webhook_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    delivery_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Webhook Delivery Detail
        api_response = await api_instance.apps_webhooks_api_get_webhook_delivery_detail(webhook_id, delivery_id)
        print("The response of WebhooksApi->apps_webhooks_api_get_webhook_delivery_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_get_webhook_delivery_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **UUID**|  | 
 **delivery_id** | **UUID**|  | 

### Return type

[**WebhookDeliveryDetailResponse**](WebhookDeliveryDetailResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_get_webhook_metrics**
> WebhookMetricsResponse apps_webhooks_api_get_webhook_metrics()

Get Webhook Metrics

Get current webhook delivery metrics (admin only).

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.webhook_metrics_response import WebhookMetricsResponse
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
    api_instance = spatialflow_generated.WebhooksApi(api_client)

    try:
        # Get Webhook Metrics
        api_response = await api_instance.apps_webhooks_api_get_webhook_metrics()
        print("The response of WebhooksApi->apps_webhooks_api_get_webhook_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_get_webhook_metrics: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhookMetricsResponse**](WebhookMetricsResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_get_webhook_success_timeline**
> Dict[str, object] apps_webhooks_api_get_webhook_success_timeline(time_range=time_range, start_date=start_date, end_date=end_date)

Get Webhook Success Timeline

Get webhook delivery success rate timeline for sparkline visualization.

Aggregates webhook delivery success rates over the specified time range,
returning hourly or daily buckets depending on the range duration.

Args:
    time_range: One of 'today', 'week', 'month', 'custom' (default: 'today')
    start_date: ISO date string for custom range start (YYYY-MM-DD)
    end_date: ISO date string for custom range end (YYYY-MM-DD)

Returns:
    200: Success rate timeline with current overall rate
    401: Unauthorized - invalid or missing authentication

Example:
    GET /api/v1/webhooks/success-timeline?time_range=week
    Response: {
        "timeline": [
            {"timestamp": "2025-10-01T00:00:00Z", "success_rate": 95.2, "total": 100, "successful": 95},
            ...
        ],
        "current_rate": 96.5,
        "total_deliveries": 1000,
        "successful_deliveries": 965
    }

### Example

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

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    time_range = 'today' # str |  (optional) (default to 'today')
    start_date = 'start_date_example' # str |  (optional)
    end_date = 'end_date_example' # str |  (optional)

    try:
        # Get Webhook Success Timeline
        api_response = await api_instance.apps_webhooks_api_get_webhook_success_timeline(time_range=time_range, start_date=start_date, end_date=end_date)
        print("The response of WebhooksApi->apps_webhooks_api_get_webhook_success_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_get_webhook_success_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_range** | **str**|  | [optional] [default to &#39;today&#39;]
 **start_date** | **str**|  | [optional] 
 **end_date** | **str**|  | [optional] 

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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_list_dlq_entries**
> Dict[str, object] apps_webhooks_api_list_dlq_entries(limit=limit, offset=offset, requeued=requeued)

List Dlq Entries

List webhook deliveries in Dead Letter Queue.

Returns failed webhook deliveries that have exhausted all retry attempts.
Entries can be filtered by requeue status and are paginated for performance.

Args:
    limit: Maximum number of entries to return (default: 50, max: 100)
    offset: Number of entries to skip for pagination (default: 0)
    requeued: Filter by requeue status (None = all, True = requeued only, False = not requeued)

Returns:
    200: List of DLQ entries with pagination metadata
    401: Unauthorized - invalid or missing authentication

Example:
    GET /api/v1/webhooks/dlq?limit=20&requeued=false

### Example

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

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    requeued = True # bool |  (optional)

    try:
        # List Dlq Entries
        api_response = await api_instance.apps_webhooks_api_list_dlq_entries(limit=limit, offset=offset, requeued=requeued)
        print("The response of WebhooksApi->apps_webhooks_api_list_dlq_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_list_dlq_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **requeued** | **bool**|  | [optional] 

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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_list_webhooks**
> WebhookListResponse apps_webhooks_api_list_webhooks(limit=limit, offset=offset, is_active=is_active)

List Webhooks

List user's webhooks with pagination.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.webhook_list_response import WebhookListResponse
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
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    is_active = True # bool |  (optional)

    try:
        # List Webhooks
        api_response = await api_instance.apps_webhooks_api_list_webhooks(limit=limit, offset=offset, is_active=is_active)
        print("The response of WebhooksApi->apps_webhooks_api_list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_list_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **is_active** | **bool**|  | [optional] 

### Return type

[**WebhookListResponse**](WebhookListResponse.md)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer), [JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_receive_webhook**
> SuccessResponse apps_webhooks_api_receive_webhook(webhook_id)

Receive Webhook

Receive incoming webhook from external service with signature verification.

This endpoint is PUBLIC and used when SpatialFlow receives webhooks from external services
(e.g., payment providers, third-party integrations). The signature is verified
using the configured secret for the webhook.

Security: This endpoint does not require authentication since external services
cannot authenticate with our org context. Security is provided by signature validation.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.success_response import SuccessResponse
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

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    webhook_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Receive Webhook
        api_response = await api_instance.apps_webhooks_api_receive_webhook(webhook_id)
        print("The response of WebhooksApi->apps_webhooks_api_receive_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_receive_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **UUID**|  | 

### Return type

[**SuccessResponse**](SuccessResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_retry_from_dlq**
> Dict[str, object] apps_webhooks_api_retry_from_dlq(dlq_id)

Retry From Dlq

Manually retry a failed webhook delivery from Dead Letter Queue.

Marks the DLQ entry as requeued and creates a new delivery attempt.
The webhook will go through the full retry logic again (7 attempts).

Args:
    dlq_id: UUID of the DLQ entry to retry

Returns:
    200: Successfully queued for retry with new task ID
    400: Entry already requeued
    401: Unauthorized - invalid or missing authentication
    404: DLQ entry not found or doesn't belong to workspace

Example:
    POST /api/v1/webhooks/dlq/550e8400-e29b-41d4-a716-446655440000/retry

### Example

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

# Configure Bearer authorization: JWTBearer
configuration = spatialflow_generated.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    dlq_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Retry From Dlq
        api_response = await api_instance.apps_webhooks_api_retry_from_dlq(dlq_id)
        print("The response of WebhooksApi->apps_webhooks_api_retry_from_dlq:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_retry_from_dlq: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dlq_id** | **UUID**|  | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_retry_webhook_delivery**
> Dict[str, object] apps_webhooks_api_retry_webhook_delivery(webhook_id, delivery_id)

Retry Webhook Delivery

Retry a failed webhook delivery.

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
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    webhook_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    delivery_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Retry Webhook Delivery
        api_response = await api_instance.apps_webhooks_api_retry_webhook_delivery(webhook_id, delivery_id)
        print("The response of WebhooksApi->apps_webhooks_api_retry_webhook_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_retry_webhook_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **UUID**|  | 
 **delivery_id** | **UUID**|  | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_test_webhook**
> WebhookTestResponse apps_webhooks_api_test_webhook(webhook_id, test_webhook_request)

Test Webhook

Test a webhook with a sample payload.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.test_webhook_request import TestWebhookRequest
from spatialflow_generated.models.webhook_test_response import WebhookTestResponse
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
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    webhook_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    test_webhook_request = spatialflow_generated.TestWebhookRequest() # TestWebhookRequest | 

    try:
        # Test Webhook
        api_response = await api_instance.apps_webhooks_api_test_webhook(webhook_id, test_webhook_request)
        print("The response of WebhooksApi->apps_webhooks_api_test_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_test_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **UUID**|  | 
 **test_webhook_request** | [**TestWebhookRequest**](TestWebhookRequest.md)|  | 

### Return type

[**WebhookTestResponse**](WebhookTestResponse.md)

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_update_webhook**
> WebhookResponse apps_webhooks_api_update_webhook(webhook_id, update_webhook_request)

Update Webhook

Update an existing webhook.

### Example

* Api Key Authentication (APIKeyBearer):
* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.update_webhook_request import UpdateWebhookRequest
from spatialflow_generated.models.webhook_response import WebhookResponse
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
    api_instance = spatialflow_generated.WebhooksApi(api_client)
    webhook_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_webhook_request = spatialflow_generated.UpdateWebhookRequest() # UpdateWebhookRequest | 

    try:
        # Update Webhook
        api_response = await api_instance.apps_webhooks_api_update_webhook(webhook_id, update_webhook_request)
        print("The response of WebhooksApi->apps_webhooks_api_update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **UUID**|  | 
 **update_webhook_request** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_webhooks_api_webhook_health_check**
> Dict[str, object] apps_webhooks_api_webhook_health_check()

Webhook Health Check

Health check for webhook service.

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
    api_instance = spatialflow_generated.WebhooksApi(api_client)

    try:
        # Webhook Health Check
        api_response = await api_instance.apps_webhooks_api_webhook_health_check()
        print("The response of WebhooksApi->apps_webhooks_api_webhook_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->apps_webhooks_api_webhook_health_check: %s\n" % e)
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
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

