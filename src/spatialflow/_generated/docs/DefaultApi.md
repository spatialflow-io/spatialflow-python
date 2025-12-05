# spatialflow_generated.DefaultApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_authentication_oauth_api_disconnect_oauth_account**](DefaultApi.md#apps_authentication_oauth_api_disconnect_oauth_account) | **DELETE** /api/v1/auth/oauth/{provider}/disconnect | Disconnect Oauth Account
[**apps_authentication_oauth_api_get_linked_accounts**](DefaultApi.md#apps_authentication_oauth_api_get_linked_accounts) | **GET** /api/v1/auth/oauth/user/linked-accounts | Get Linked Accounts
[**apps_authentication_oauth_api_get_oauth_providers**](DefaultApi.md#apps_authentication_oauth_api_get_oauth_providers) | **GET** /api/v1/auth/oauth/providers | Get Oauth Providers
[**apps_authentication_oauth_api_link_oauth_account**](DefaultApi.md#apps_authentication_oauth_api_link_oauth_account) | **POST** /api/v1/auth/oauth/{provider}/link | Link Oauth Account
[**apps_authentication_oauth_api_oauth_authorize**](DefaultApi.md#apps_authentication_oauth_api_oauth_authorize) | **GET** /api/v1/auth/oauth/{provider}/authorize | Oauth Authorize
[**apps_authentication_oauth_api_oauth_callback**](DefaultApi.md#apps_authentication_oauth_api_oauth_callback) | **GET** /api/v1/auth/oauth/{provider}/callback | Oauth Callback
[**apps_email_unsubscribe_unsubscribe**](DefaultApi.md#apps_email_unsubscribe_unsubscribe) | **POST** /api/v1/email/unsubscribe | Unsubscribe
[**apps_email_unsubscribe_verify_unsubscribe_token**](DefaultApi.md#apps_email_unsubscribe_verify_unsubscribe_token) | **GET** /api/v1/email/unsubscribe/verify | Verify Unsubscribe Token


# **apps_authentication_oauth_api_disconnect_oauth_account**
> Dict[str, object] apps_authentication_oauth_api_disconnect_oauth_account(provider)

Disconnect Oauth Account

Disconnect an OAuth provider from user account.

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
    api_instance = spatialflow_generated.DefaultApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Disconnect Oauth Account
        api_response = await api_instance.apps_authentication_oauth_api_disconnect_oauth_account(provider)
        print("The response of DefaultApi->apps_authentication_oauth_api_disconnect_oauth_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_oauth_api_disconnect_oauth_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_oauth_api_get_linked_accounts**
> apps_authentication_oauth_api_get_linked_accounts()

Get Linked Accounts

Get list of OAuth providers linked to user account.

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
    api_instance = spatialflow_generated.DefaultApi(api_client)

    try:
        # Get Linked Accounts
        await api_instance.apps_authentication_oauth_api_get_linked_accounts()
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_oauth_api_get_linked_accounts: %s\n" % e)
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

# **apps_authentication_oauth_api_get_oauth_providers**
> OAuthProvidersResponse apps_authentication_oauth_api_get_oauth_providers()

Get Oauth Providers

Get list of available OAuth providers

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.o_auth_providers_response import OAuthProvidersResponse
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
    api_instance = spatialflow_generated.DefaultApi(api_client)

    try:
        # Get Oauth Providers
        api_response = await api_instance.apps_authentication_oauth_api_get_oauth_providers()
        print("The response of DefaultApi->apps_authentication_oauth_api_get_oauth_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_oauth_api_get_oauth_providers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OAuthProvidersResponse**](OAuthProvidersResponse.md)

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

# **apps_authentication_oauth_api_link_oauth_account**
> OAuthLinkResponse apps_authentication_oauth_api_link_oauth_account(provider)

Link Oauth Account

Link an OAuth provider to an existing authenticated user account.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.o_auth_link_response import OAuthLinkResponse
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
    api_instance = spatialflow_generated.DefaultApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Link Oauth Account
        api_response = await api_instance.apps_authentication_oauth_api_link_oauth_account(provider)
        print("The response of DefaultApi->apps_authentication_oauth_api_link_oauth_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_oauth_api_link_oauth_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 

### Return type

[**OAuthLinkResponse**](OAuthLinkResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_oauth_api_oauth_authorize**
> OAuthAuthorizeResponse apps_authentication_oauth_api_oauth_authorize(provider, next=next)

Oauth Authorize

Initialize OAuth flow for a provider. Returns authorization URL to redirect user to.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.o_auth_authorize_response import OAuthAuthorizeResponse
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
    api_instance = spatialflow_generated.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    next = 'next_example' # str |  (optional)

    try:
        # Oauth Authorize
        api_response = await api_instance.apps_authentication_oauth_api_oauth_authorize(provider, next=next)
        print("The response of DefaultApi->apps_authentication_oauth_api_oauth_authorize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_oauth_api_oauth_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **next** | **str**|  | [optional] 

### Return type

[**OAuthAuthorizeResponse**](OAuthAuthorizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_oauth_api_oauth_callback**
> apps_authentication_oauth_api_oauth_callback(provider, o_auth_callback_query)

Oauth Callback

Handle OAuth callback from provider. Exchanges code for tokens and creates/links user account.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.o_auth_callback_query import OAuthCallbackQuery
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
    api_instance = spatialflow_generated.DefaultApi(api_client)
    provider = 'provider_example' # str | 
    o_auth_callback_query = spatialflow_generated.OAuthCallbackQuery() # OAuthCallbackQuery | 

    try:
        # Oauth Callback
        await api_instance.apps_authentication_oauth_api_oauth_callback(provider, o_auth_callback_query)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_oauth_api_oauth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **o_auth_callback_query** | [**OAuthCallbackQuery**](OAuthCallbackQuery.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_email_unsubscribe_unsubscribe**
> UnsubscribeResponse apps_email_unsubscribe_unsubscribe(unsubscribe_request)

Unsubscribe

Handle email unsubscribe requests.  Verifies the signed timestamped token (max 90 days old) and adds the email to the blacklist. This endpoint is public (no authentication required) to allow one-click unsubscribe from emails.  Rate limited to 10 requests per minute per IP to prevent abuse.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.unsubscribe_request import UnsubscribeRequest
from spatialflow_generated.models.unsubscribe_response import UnsubscribeResponse
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
    api_instance = spatialflow_generated.DefaultApi(api_client)
    unsubscribe_request = spatialflow_generated.UnsubscribeRequest() # UnsubscribeRequest | 

    try:
        # Unsubscribe
        api_response = await api_instance.apps_email_unsubscribe_unsubscribe(unsubscribe_request)
        print("The response of DefaultApi->apps_email_unsubscribe_unsubscribe:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_email_unsubscribe_unsubscribe: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unsubscribe_request** | [**UnsubscribeRequest**](UnsubscribeRequest.md)|  | 

### Return type

[**UnsubscribeResponse**](UnsubscribeResponse.md)

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

# **apps_email_unsubscribe_verify_unsubscribe_token**
> Dict[str, object] apps_email_unsubscribe_verify_unsubscribe_token(token)

Verify Unsubscribe Token

Verify an unsubscribe token without actually unsubscribing.  This can be used by the frontend to show a confirmation page before the user confirms they want to unsubscribe.

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
    api_instance = spatialflow_generated.DefaultApi(api_client)
    token = 'token_example' # str | 

    try:
        # Verify Unsubscribe Token
        api_response = await api_instance.apps_email_unsubscribe_verify_unsubscribe_token(token)
        print("The response of DefaultApi->apps_email_unsubscribe_verify_unsubscribe_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_email_unsubscribe_verify_unsubscribe_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

