# spatialflow_generated.BillingApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_subscriptions_billing_api_add_payment_method**](BillingApi.md#apps_subscriptions_billing_api_add_payment_method) | **POST** /api/v1/billing/payment-methods | Add Payment Method
[**apps_subscriptions_billing_api_change_plan**](BillingApi.md#apps_subscriptions_billing_api_change_plan) | **POST** /api/v1/billing/change-plan | Change Plan
[**apps_subscriptions_billing_api_create_setup_intent**](BillingApi.md#apps_subscriptions_billing_api_create_setup_intent) | **POST** /api/v1/billing/create-setup-intent | Create Setup Intent
[**apps_subscriptions_billing_api_download_invoice**](BillingApi.md#apps_subscriptions_billing_api_download_invoice) | **GET** /api/v1/billing/invoices/{invoice_id}/download | Download Invoice
[**apps_subscriptions_billing_api_get_invoice**](BillingApi.md#apps_subscriptions_billing_api_get_invoice) | **GET** /api/v1/billing/invoices/{invoice_id} | Get Invoice
[**apps_subscriptions_billing_api_list_invoices**](BillingApi.md#apps_subscriptions_billing_api_list_invoices) | **GET** /api/v1/billing/invoices | List Invoices
[**apps_subscriptions_billing_api_list_payment_methods**](BillingApi.md#apps_subscriptions_billing_api_list_payment_methods) | **GET** /api/v1/billing/payment-methods | List Payment Methods
[**apps_subscriptions_billing_api_preview_plan_change**](BillingApi.md#apps_subscriptions_billing_api_preview_plan_change) | **POST** /api/v1/billing/preview-plan-change | Preview Plan Change
[**apps_subscriptions_billing_api_remove_payment_method**](BillingApi.md#apps_subscriptions_billing_api_remove_payment_method) | **DELETE** /api/v1/billing/payment-methods/{pm_id} | Remove Payment Method
[**apps_subscriptions_billing_api_set_default_payment_method**](BillingApi.md#apps_subscriptions_billing_api_set_default_payment_method) | **PUT** /api/v1/billing/payment-methods/{pm_id}/default | Set Default Payment Method


# **apps_subscriptions_billing_api_add_payment_method**
> Dict[str, object] apps_subscriptions_billing_api_add_payment_method(payment_method_request)

Add Payment Method

Add a new payment method

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.payment_method_request import PaymentMethodRequest
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
    api_instance = spatialflow_generated.BillingApi(api_client)
    payment_method_request = spatialflow_generated.PaymentMethodRequest() # PaymentMethodRequest | 

    try:
        # Add Payment Method
        api_response = await api_instance.apps_subscriptions_billing_api_add_payment_method(payment_method_request)
        print("The response of BillingApi->apps_subscriptions_billing_api_add_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_add_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_request** | [**PaymentMethodRequest**](PaymentMethodRequest.md)|  | 

### Return type

**Dict[str, object]**

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_billing_api_change_plan**
> Dict[str, object] apps_subscriptions_billing_api_change_plan(plan_change_request)

Change Plan

Change subscription plan

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.plan_change_request import PlanChangeRequest
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
    api_instance = spatialflow_generated.BillingApi(api_client)
    plan_change_request = spatialflow_generated.PlanChangeRequest() # PlanChangeRequest | 

    try:
        # Change Plan
        api_response = await api_instance.apps_subscriptions_billing_api_change_plan(plan_change_request)
        print("The response of BillingApi->apps_subscriptions_billing_api_change_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_change_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_change_request** | [**PlanChangeRequest**](PlanChangeRequest.md)|  | 

### Return type

**Dict[str, object]**

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
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_billing_api_download_invoice**
> Dict[str, object] apps_subscriptions_billing_api_download_invoice(invoice_id)

Download Invoice

Get invoice download URL

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
    api_instance = spatialflow_generated.BillingApi(api_client)
    invoice_id = 'invoice_id_example' # str | 

    try:
        # Download Invoice
        api_response = await api_instance.apps_subscriptions_billing_api_download_invoice(invoice_id)
        print("The response of BillingApi->apps_subscriptions_billing_api_download_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_download_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_billing_api_preview_plan_change**
> PlanChangePreviewResponse apps_subscriptions_billing_api_preview_plan_change(plan_change_request)

Preview Plan Change

Preview prorated charges for plan change

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.plan_change_preview_response import PlanChangePreviewResponse
from spatialflow_generated.models.plan_change_request import PlanChangeRequest
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
    api_instance = spatialflow_generated.BillingApi(api_client)
    plan_change_request = spatialflow_generated.PlanChangeRequest() # PlanChangeRequest | 

    try:
        # Preview Plan Change
        api_response = await api_instance.apps_subscriptions_billing_api_preview_plan_change(plan_change_request)
        print("The response of BillingApi->apps_subscriptions_billing_api_preview_plan_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_preview_plan_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_change_request** | [**PlanChangeRequest**](PlanChangeRequest.md)|  | 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_billing_api_remove_payment_method**
> Dict[str, object] apps_subscriptions_billing_api_remove_payment_method(pm_id)

Remove Payment Method

Remove a payment method.  Security: Verifies ownership before detaching to prevent users from detaching payment methods belonging to other customers. Returns 404 for ALL non-owned cases to avoid enumeration attacks.

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
    api_instance = spatialflow_generated.BillingApi(api_client)
    pm_id = 'pm_id_example' # str | 

    try:
        # Remove Payment Method
        api_response = await api_instance.apps_subscriptions_billing_api_remove_payment_method(pm_id)
        print("The response of BillingApi->apps_subscriptions_billing_api_remove_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_remove_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_id** | **str**|  | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_subscriptions_billing_api_set_default_payment_method**
> Dict[str, object] apps_subscriptions_billing_api_set_default_payment_method(pm_id)

Set Default Payment Method

Set payment method as default

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
    api_instance = spatialflow_generated.BillingApi(api_client)
    pm_id = 'pm_id_example' # str | 

    try:
        # Set Default Payment Method
        api_response = await api_instance.apps_subscriptions_billing_api_set_default_payment_method(pm_id)
        print("The response of BillingApi->apps_subscriptions_billing_api_set_default_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->apps_subscriptions_billing_api_set_default_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_id** | **str**|  | 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

