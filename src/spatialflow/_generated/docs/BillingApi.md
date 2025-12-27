# spatialflow_generated.BillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_subscriptions_billing_api_add_payment_method**](BillingApi.md#apps_subscriptions_billing_api_add_payment_method) | **POST** /api/v1/billing/payment-methods | Add Payment Method
[**apps_subscriptions_billing_api_cancel_subscription**](BillingApi.md#apps_subscriptions_billing_api_cancel_subscription) | **POST** /api/v1/billing/cancel-subscription | Cancel Subscription
[**apps_subscriptions_billing_api_change_plan**](BillingApi.md#apps_subscriptions_billing_api_change_plan) | **POST** /api/v1/billing/change-plan | Change Plan
[**apps_subscriptions_billing_api_create_setup_intent**](BillingApi.md#apps_subscriptions_billing_api_create_setup_intent) | **POST** /api/v1/billing/create-setup-intent | Create Setup Intent
[**apps_subscriptions_billing_api_download_invoice**](BillingApi.md#apps_subscriptions_billing_api_download_invoice) | **GET** /api/v1/billing/invoices/{invoice_id}/download | Download Invoice
[**apps_subscriptions_billing_api_get_invoice**](BillingApi.md#apps_subscriptions_billing_api_get_invoice) | **GET** /api/v1/billing/invoices/{invoice_id} | Get Invoice
[**apps_subscriptions_billing_api_list_invoices**](BillingApi.md#apps_subscriptions_billing_api_list_invoices) | **GET** /api/v1/billing/invoices | List Invoices
[**apps_subscriptions_billing_api_list_payment_methods**](BillingApi.md#apps_subscriptions_billing_api_list_payment_methods) | **GET** /api/v1/billing/payment-methods | List Payment Methods
[**apps_subscriptions_billing_api_preview_plan_change**](BillingApi.md#apps_subscriptions_billing_api_preview_plan_change) | **POST** /api/v1/billing/preview-plan-change | Preview Plan Change
[**apps_subscriptions_billing_api_reactivate_subscription**](BillingApi.md#apps_subscriptions_billing_api_reactivate_subscription) | **POST** /api/v1/billing/reactivate-subscription | Reactivate Subscription
[**apps_subscriptions_billing_api_remove_payment_method**](BillingApi.md#apps_subscriptions_billing_api_remove_payment_method) | **DELETE** /api/v1/billing/payment-methods/{pm_id} | Remove Payment Method
[**apps_subscriptions_billing_api_set_default_payment_method**](BillingApi.md#apps_subscriptions_billing_api_set_default_payment_method) | **PUT** /api/v1/billing/payment-methods/{pm_id}/default | Set Default Payment Method


# **apps_subscriptions_billing_api_add_payment_method**
> apps_subscriptions_billing_api_add_payment_method(body)

Add Payment Method

Add a new payment method

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
    api_instance = spatialflow_generated.BillingApi(api_client)
    body = 'body_example' # str | 

    try:
        # Add Payment Method
        await api_instance.apps_subscriptions_billing_api_add_payment_method(body)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_add_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_billing_api_cancel_subscription**
> apps_subscriptions_billing_api_cancel_subscription(body=body)

Cancel Subscription

Cancel subscription at period end

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
    api_instance = spatialflow_generated.BillingApi(api_client)
    body = 'body_example' # str |  (optional)

    try:
        # Cancel Subscription
        await api_instance.apps_subscriptions_billing_api_cancel_subscription(body=body)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_cancel_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_billing_api_change_plan**
> apps_subscriptions_billing_api_change_plan(body)

Change Plan

Change subscription plan

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
    api_instance = spatialflow_generated.BillingApi(api_client)
    body = 'body_example' # str | 

    try:
        # Change Plan
        await api_instance.apps_subscriptions_billing_api_change_plan(body)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_change_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_billing_api_create_setup_intent**
> SetupIntentResponse apps_subscriptions_billing_api_create_setup_intent()

Create Setup Intent

Create Stripe setup intent for adding payment method

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.setup_intent_response import SetupIntentResponse
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
    api_instance = spatialflow_generated.BillingApi(api_client)

    try:
        # Create Setup Intent
        api_response = await api_instance.apps_subscriptions_billing_api_create_setup_intent()
        print("The response of BillingApi->apps_subscriptions_billing_api_create_setup_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_create_setup_intent: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SetupIntentResponse**](SetupIntentResponse.md)

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

# **apps_subscriptions_billing_api_download_invoice**
> apps_subscriptions_billing_api_download_invoice(invoice_id)

Download Invoice

Get invoice download URL

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
    api_instance = spatialflow_generated.BillingApi(api_client)
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Download Invoice
        await api_instance.apps_subscriptions_billing_api_download_invoice(invoice_id)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_download_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

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

# **apps_subscriptions_billing_api_get_invoice**
> InvoiceResponse apps_subscriptions_billing_api_get_invoice(invoice_id)

Get Invoice

Get specific invoice details

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.invoice_response import InvoiceResponse
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
    api_instance = spatialflow_generated.BillingApi(api_client)
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Get Invoice
        api_response = await api_instance.apps_subscriptions_billing_api_get_invoice(invoice_id)
        print("The response of BillingApi->apps_subscriptions_billing_api_get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

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

# **apps_subscriptions_billing_api_list_invoices**
> InvoiceListResponse apps_subscriptions_billing_api_list_invoices(limit=limit, starting_after=starting_after)

List Invoices

List user's invoices

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.invoice_list_response import InvoiceListResponse
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
    api_instance = spatialflow_generated.BillingApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    starting_after = 'starting_after_example' # str |  (optional)

    try:
        # List Invoices
        api_response = await api_instance.apps_subscriptions_billing_api_list_invoices(limit=limit, starting_after=starting_after)
        print("The response of BillingApi->apps_subscriptions_billing_api_list_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_list_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **starting_after** | **str**|  | [optional] 

### Return type

[**InvoiceListResponse**](InvoiceListResponse.md)

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

# **apps_subscriptions_billing_api_list_payment_methods**
> List[PaymentMethodResponse] apps_subscriptions_billing_api_list_payment_methods()

List Payment Methods

List user's payment methods

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.payment_method_response import PaymentMethodResponse
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
    api_instance = spatialflow_generated.BillingApi(api_client)

    try:
        # List Payment Methods
        api_response = await api_instance.apps_subscriptions_billing_api_list_payment_methods()
        print("The response of BillingApi->apps_subscriptions_billing_api_list_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_list_payment_methods: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PaymentMethodResponse]**](PaymentMethodResponse.md)

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

# **apps_subscriptions_billing_api_preview_plan_change**
> PlanChangePreviewResponse apps_subscriptions_billing_api_preview_plan_change(body)

Preview Plan Change

Preview prorated charges for plan change

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.plan_change_preview_response import PlanChangePreviewResponse
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
    api_instance = spatialflow_generated.BillingApi(api_client)
    body = 'body_example' # str | 

    try:
        # Preview Plan Change
        api_response = await api_instance.apps_subscriptions_billing_api_preview_plan_change(body)
        print("The response of BillingApi->apps_subscriptions_billing_api_preview_plan_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_preview_plan_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**PlanChangePreviewResponse**](PlanChangePreviewResponse.md)

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

# **apps_subscriptions_billing_api_reactivate_subscription**
> apps_subscriptions_billing_api_reactivate_subscription()

Reactivate Subscription

Reactivate a cancelled subscription

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
    api_instance = spatialflow_generated.BillingApi(api_client)

    try:
        # Reactivate Subscription
        await api_instance.apps_subscriptions_billing_api_reactivate_subscription()
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_reactivate_subscription: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **apps_subscriptions_billing_api_remove_payment_method**
> apps_subscriptions_billing_api_remove_payment_method(pm_id)

Remove Payment Method

Remove a payment method

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
    api_instance = spatialflow_generated.BillingApi(api_client)
    pm_id = 'pm_id_example' # str | 

    try:
        # Remove Payment Method
        await api_instance.apps_subscriptions_billing_api_remove_payment_method(pm_id)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_remove_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_id** | **str**|  | 

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

# **apps_subscriptions_billing_api_set_default_payment_method**
> apps_subscriptions_billing_api_set_default_payment_method(pm_id)

Set Default Payment Method

Set payment method as default

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
    api_instance = spatialflow_generated.BillingApi(api_client)
    pm_id = 'pm_id_example' # str | 

    try:
        # Set Default Payment Method
        await api_instance.apps_subscriptions_billing_api_set_default_payment_method(pm_id)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_set_default_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_id** | **str**|  | 

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

