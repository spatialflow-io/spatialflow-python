# spatialflow_generated.EmailApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_email_api_get_email_history**](EmailApi.md#apps_email_api_get_email_history) | **GET** /api/v1/email/history | Get Email History
[**apps_email_api_get_email_status**](EmailApi.md#apps_email_api_get_email_status) | **GET** /api/v1/email/status/{email_id} | Get Email Status
[**apps_email_api_get_queue_stats**](EmailApi.md#apps_email_api_get_queue_stats) | **GET** /api/v1/email/queue-stats | Get Queue Stats
[**apps_email_api_health_check**](EmailApi.md#apps_email_api_health_check) | **GET** /api/v1/email/health | Health Check
[**apps_email_api_preview_email_template**](EmailApi.md#apps_email_api_preview_email_template) | **GET** /api/v1/email/preview/{template_name} | Preview Email Template
[**apps_email_api_send_email**](EmailApi.md#apps_email_api_send_email) | **POST** /api/v1/email/send | Send Email
[**apps_email_api_send_test_email**](EmailApi.md#apps_email_api_send_test_email) | **POST** /api/v1/email/test | Send Test Email


# **apps_email_api_get_email_history**
> apps_email_api_get_email_history(limit=limit, offset=offset)

Get Email History

Get email history for the current user

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
    api_instance = spatialflow_generated.EmailApi(api_client)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)

    try:
        # Get Email History
        await api_instance.apps_email_api_get_email_history(limit=limit, offset=offset)
    except Exception as e:
        print("Exception when calling EmailApi->apps_email_api_get_email_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]

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

# **apps_email_api_get_email_status**
> EmailStatusResponse apps_email_api_get_email_status(email_id)

Get Email Status

Check email delivery status

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.email_status_response import EmailStatusResponse
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
    api_instance = spatialflow_generated.EmailApi(api_client)
    email_id = 'email_id_example' # str | 

    try:
        # Get Email Status
        api_response = await api_instance.apps_email_api_get_email_status(email_id)
        print("The response of EmailApi->apps_email_api_get_email_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->apps_email_api_get_email_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**|  | 

### Return type

[**EmailStatusResponse**](EmailStatusResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_email_api_get_queue_stats**
> EmailQueueStats apps_email_api_get_queue_stats()

Get Queue Stats

Get email queue statistics (admin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.email_queue_stats import EmailQueueStats
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
    api_instance = spatialflow_generated.EmailApi(api_client)

    try:
        # Get Queue Stats
        api_response = await api_instance.apps_email_api_get_queue_stats()
        print("The response of EmailApi->apps_email_api_get_queue_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->apps_email_api_get_queue_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EmailQueueStats**](EmailQueueStats.md)

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

# **apps_email_api_health_check**
> EmailHealthResponse apps_email_api_health_check()

Health Check

Email service health check

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.email_health_response import EmailHealthResponse
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
    api_instance = spatialflow_generated.EmailApi(api_client)

    try:
        # Health Check
        api_response = await api_instance.apps_email_api_health_check()
        print("The response of EmailApi->apps_email_api_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->apps_email_api_health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EmailHealthResponse**](EmailHealthResponse.md)

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

# **apps_email_api_preview_email_template**
> apps_email_api_preview_email_template(template_name, format=format)

Preview Email Template

Preview an email template with sample data (admin only)

Args:
    template_name: Name of the template to preview
    format: Output format - 'html' or 'txt' (default: 'html')

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
    api_instance = spatialflow_generated.EmailApi(api_client)
    template_name = 'template_name_example' # str | 
    format = 'html' # str |  (optional) (default to 'html')

    try:
        # Preview Email Template
        await api_instance.apps_email_api_preview_email_template(template_name, format=format)
    except Exception as e:
        print("Exception when calling EmailApi->apps_email_api_preview_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**|  | 
 **format** | **str**|  | [optional] [default to &#39;html&#39;]

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
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_email_api_send_email**
> Dict[str, object] apps_email_api_send_email(send_email_request)

Send Email

Queue email for delivery (admin only)

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.send_email_request import SendEmailRequest
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
    api_instance = spatialflow_generated.EmailApi(api_client)
    send_email_request = spatialflow_generated.SendEmailRequest() # SendEmailRequest | 

    try:
        # Send Email
        api_response = await api_instance.apps_email_api_send_email(send_email_request)
        print("The response of EmailApi->apps_email_api_send_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->apps_email_api_send_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_email_request** | [**SendEmailRequest**](SendEmailRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_email_api_send_test_email**
> Dict[str, object] apps_email_api_send_test_email()

Send Test Email

Send a test email to verify email configuration (admin only)

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
    api_instance = spatialflow_generated.EmailApi(api_client)

    try:
        # Send Test Email
        api_response = await api_instance.apps_email_api_send_test_email()
        print("The response of EmailApi->apps_email_api_send_test_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->apps_email_api_send_test_email: %s\n" % e)
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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

