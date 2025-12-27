# spatialflow_generated.SubscriptionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_subscriptions_api_cancel_subscription**](SubscriptionsApi.md#apps_subscriptions_api_cancel_subscription) | **PUT** /api/v1/subscriptions/cancel | Cancel Subscription
[**apps_subscriptions_api_create_checkout_session**](SubscriptionsApi.md#apps_subscriptions_api_create_checkout_session) | **POST** /api/v1/subscriptions/create-checkout-session | Create Checkout Session
[**apps_subscriptions_api_create_portal_session**](SubscriptionsApi.md#apps_subscriptions_api_create_portal_session) | **POST** /api/v1/subscriptions/create-portal-session | Create Portal Session
[**apps_subscriptions_api_get_current_subscription**](SubscriptionsApi.md#apps_subscriptions_api_get_current_subscription) | **GET** /api/v1/subscriptions/current | Get Current Subscription
[**apps_subscriptions_api_get_subscription_plans**](SubscriptionsApi.md#apps_subscriptions_api_get_subscription_plans) | **GET** /api/v1/subscriptions/plans | Get Subscription Plans
[**apps_subscriptions_api_get_usage_metrics**](SubscriptionsApi.md#apps_subscriptions_api_get_usage_metrics) | **GET** /api/v1/subscriptions/usage | Get Usage Metrics
[**apps_subscriptions_api_handle_stripe_webhook**](SubscriptionsApi.md#apps_subscriptions_api_handle_stripe_webhook) | **POST** /api/v1/subscriptions/stripe-webhook | Handle Stripe Webhook
[**apps_subscriptions_api_health_check**](SubscriptionsApi.md#apps_subscriptions_api_health_check) | **GET** /api/v1/subscriptions/health | Health Check
[**apps_subscriptions_api_reactivate_subscription**](SubscriptionsApi.md#apps_subscriptions_api_reactivate_subscription) | **PUT** /api/v1/subscriptions/reactivate | Reactivate Subscription


# **apps_subscriptions_api_cancel_subscription**
> SubscriptionActionResponse apps_subscriptions_api_cancel_subscription()

Cancel Subscription

Cancel the current user's subscription at period end.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.subscription_action_response import SubscriptionActionResponse
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
    api_instance = spatialflow_generated.SubscriptionsApi(api_client)

    try:
        # Cancel Subscription
        api_response = await api_instance.apps_subscriptions_api_cancel_subscription()
        print("The response of SubscriptionsApi->apps_subscriptions_api_cancel_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->apps_subscriptions_api_cancel_subscription: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SubscriptionActionResponse**](SubscriptionActionResponse.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_api_create_checkout_session**
> CheckoutSessionResponse apps_subscriptions_api_create_checkout_session(checkout_session_request)

Create Checkout Session

Create a Stripe checkout session for subscription purchase.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.checkout_session_request import CheckoutSessionRequest
from spatialflow_generated.models.checkout_session_response import CheckoutSessionResponse
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
    api_instance = spatialflow_generated.SubscriptionsApi(api_client)
    checkout_session_request = spatialflow_generated.CheckoutSessionRequest() # CheckoutSessionRequest | 

    try:
        # Create Checkout Session
        api_response = await api_instance.apps_subscriptions_api_create_checkout_session(checkout_session_request)
        print("The response of SubscriptionsApi->apps_subscriptions_api_create_checkout_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->apps_subscriptions_api_create_checkout_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_request** | [**CheckoutSessionRequest**](CheckoutSessionRequest.md)|  | 

### Return type

[**CheckoutSessionResponse**](CheckoutSessionResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_api_create_portal_session**
> PortalSessionResponse apps_subscriptions_api_create_portal_session(portal_session_request)

Create Portal Session

Create a Stripe customer portal session for subscription management.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.portal_session_request import PortalSessionRequest
from spatialflow_generated.models.portal_session_response import PortalSessionResponse
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
    api_instance = spatialflow_generated.SubscriptionsApi(api_client)
    portal_session_request = spatialflow_generated.PortalSessionRequest() # PortalSessionRequest | 

    try:
        # Create Portal Session
        api_response = await api_instance.apps_subscriptions_api_create_portal_session(portal_session_request)
        print("The response of SubscriptionsApi->apps_subscriptions_api_create_portal_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->apps_subscriptions_api_create_portal_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_session_request** | [**PortalSessionRequest**](PortalSessionRequest.md)|  | 

### Return type

[**PortalSessionResponse**](PortalSessionResponse.md)

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
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_api_get_current_subscription**
> SubscriptionResponse apps_subscriptions_api_get_current_subscription()

Get Current Subscription

Get current user's subscription details.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.subscription_response import SubscriptionResponse
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
    api_instance = spatialflow_generated.SubscriptionsApi(api_client)

    try:
        # Get Current Subscription
        api_response = await api_instance.apps_subscriptions_api_get_current_subscription()
        print("The response of SubscriptionsApi->apps_subscriptions_api_get_current_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->apps_subscriptions_api_get_current_subscription: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_api_get_subscription_plans**
> List[PlanResponse] apps_subscriptions_api_get_subscription_plans()

Get Subscription Plans

Get all available subscription plans.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.plan_response import PlanResponse
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
    api_instance = spatialflow_generated.SubscriptionsApi(api_client)

    try:
        # Get Subscription Plans
        api_response = await api_instance.apps_subscriptions_api_get_subscription_plans()
        print("The response of SubscriptionsApi->apps_subscriptions_api_get_subscription_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->apps_subscriptions_api_get_subscription_plans: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PlanResponse]**](PlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_api_get_usage_metrics**
> UsageResponse apps_subscriptions_api_get_usage_metrics()

Get Usage Metrics

Get detailed usage metrics for the current billing period.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.usage_response import UsageResponse
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
    api_instance = spatialflow_generated.SubscriptionsApi(api_client)

    try:
        # Get Usage Metrics
        api_response = await api_instance.apps_subscriptions_api_get_usage_metrics()
        print("The response of SubscriptionsApi->apps_subscriptions_api_get_usage_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->apps_subscriptions_api_get_usage_metrics: %s\n" % e)
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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_api_handle_stripe_webhook**
> apps_subscriptions_api_handle_stripe_webhook()

Handle Stripe Webhook

Handle Stripe webhook events.

Note: This endpoint doesn't use standard Django Ninja response handling
because it needs to work with raw request body for signature verification.

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
    api_instance = spatialflow_generated.SubscriptionsApi(api_client)

    try:
        # Handle Stripe Webhook
        await api_instance.apps_subscriptions_api_handle_stripe_webhook()
    except Exception as e:
        print("Exception when calling SubscriptionsApi->apps_subscriptions_api_handle_stripe_webhook: %s\n" % e)
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

# **apps_subscriptions_api_health_check**
> HealthResponse apps_subscriptions_api_health_check()

Health Check

Health check endpoint for subscription service.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.health_response import HealthResponse
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
    api_instance = spatialflow_generated.SubscriptionsApi(api_client)

    try:
        # Health Check
        api_response = await api_instance.apps_subscriptions_api_health_check()
        print("The response of SubscriptionsApi->apps_subscriptions_api_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->apps_subscriptions_api_health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

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

# **apps_subscriptions_api_reactivate_subscription**
> SubscriptionActionResponse apps_subscriptions_api_reactivate_subscription()

Reactivate Subscription

Reactivate a cancelled subscription before period end.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.subscription_action_response import SubscriptionActionResponse
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
    api_instance = spatialflow_generated.SubscriptionsApi(api_client)

    try:
        # Reactivate Subscription
        api_response = await api_instance.apps_subscriptions_api_reactivate_subscription()
        print("The response of SubscriptionsApi->apps_subscriptions_api_reactivate_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->apps_subscriptions_api_reactivate_subscription: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SubscriptionActionResponse**](SubscriptionActionResponse.md)

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
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

