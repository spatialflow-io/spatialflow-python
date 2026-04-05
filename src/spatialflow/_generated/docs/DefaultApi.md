# spatialflow_generated.DefaultApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_authentication_apple_mobile_api_apple_nonce**](DefaultApi.md#apps_authentication_apple_mobile_api_apple_nonce) | **POST** /api/v1/auth/apple/nonce | Apple Nonce
[**apps_authentication_apple_mobile_api_apple_token_exchange**](DefaultApi.md#apps_authentication_apple_mobile_api_apple_token_exchange) | **POST** /api/v1/auth/apple/token-exchange | Apple Token Exchange
[**apps_authentication_google_mobile_api_google_token_exchange**](DefaultApi.md#apps_authentication_google_mobile_api_google_token_exchange) | **POST** /api/v1/auth/google/token-exchange | Google Token Exchange
[**apps_authentication_oauth_api_disconnect_oauth_account**](DefaultApi.md#apps_authentication_oauth_api_disconnect_oauth_account) | **DELETE** /api/v1/auth/oauth/{provider}/disconnect | Disconnect Oauth Account
[**apps_authentication_oauth_api_get_linked_accounts**](DefaultApi.md#apps_authentication_oauth_api_get_linked_accounts) | **GET** /api/v1/auth/oauth/user/linked-accounts | Get Linked Accounts
[**apps_authentication_oauth_api_get_oauth_providers**](DefaultApi.md#apps_authentication_oauth_api_get_oauth_providers) | **GET** /api/v1/auth/oauth/providers | Get Oauth Providers
[**apps_authentication_oauth_api_link_oauth_account**](DefaultApi.md#apps_authentication_oauth_api_link_oauth_account) | **POST** /api/v1/auth/oauth/{provider}/link | Link Oauth Account
[**apps_authentication_oauth_api_oauth_authorize**](DefaultApi.md#apps_authentication_oauth_api_oauth_authorize) | **GET** /api/v1/auth/oauth/{provider}/authorize | Oauth Authorize
[**apps_authentication_oauth_api_oauth_callback**](DefaultApi.md#apps_authentication_oauth_api_oauth_callback) | **GET** /api/v1/auth/oauth/{provider}/callback | Oauth Callback
[**apps_authentication_saml_api_detect_method**](DefaultApi.md#apps_authentication_saml_api_detect_method) | **POST** /api/v1/auth/saml/detect-method | Detect Method
[**apps_authentication_saml_api_initiate**](DefaultApi.md#apps_authentication_saml_api_initiate) | **GET** /api/v1/auth/saml/{slug}/initiate | Initiate
[**apps_authentication_saml_api_metadata**](DefaultApi.md#apps_authentication_saml_api_metadata) | **GET** /api/v1/auth/saml/{slug}/metadata | Metadata
[**apps_authentication_saml_api_saml_acs**](DefaultApi.md#apps_authentication_saml_api_saml_acs) | **POST** /api/v1/auth/saml/{slug}/acs | Saml Acs
[**apps_email_unsubscribe_unsubscribe**](DefaultApi.md#apps_email_unsubscribe_unsubscribe) | **POST** /api/v1/email/unsubscribe | Unsubscribe
[**apps_email_unsubscribe_verify_unsubscribe_token**](DefaultApi.md#apps_email_unsubscribe_verify_unsubscribe_token) | **GET** /api/v1/email/unsubscribe/verify | Verify Unsubscribe Token


# **apps_authentication_apple_mobile_api_apple_nonce**
> AppleNonceResponse apps_authentication_apple_mobile_api_apple_nonce()

Apple Nonce

Generate a server-side nonce for Apple Sign-In replay protection.  Clients should call this before initiating Apple Sign-In, then pass the returned nonce to the Apple SDK. The nonce claim in the resulting identity token will be validated server-side during token exchange.  Rate limited: 10/min per IP.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.apple_nonce_response import AppleNonceResponse
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
        # Apple Nonce
        api_response = await api_instance.apps_authentication_apple_mobile_api_apple_nonce()
        print("The response of DefaultApi->apps_authentication_apple_mobile_api_apple_nonce:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_apple_mobile_api_apple_nonce: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppleNonceResponse**](AppleNonceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_apple_mobile_api_apple_token_exchange**
> AppleTokenExchangeResponse apps_authentication_apple_mobile_api_apple_token_exchange(apple_token_exchange_request)

Apple Token Exchange

Exchange an Apple identity token (from mobile SDK) for a SpatialFlow JWT.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.apple_token_exchange_request import AppleTokenExchangeRequest
from spatialflow_generated.models.apple_token_exchange_response import AppleTokenExchangeResponse
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
    apple_token_exchange_request = spatialflow_generated.AppleTokenExchangeRequest() # AppleTokenExchangeRequest | 

    try:
        # Apple Token Exchange
        api_response = await api_instance.apps_authentication_apple_mobile_api_apple_token_exchange(apple_token_exchange_request)
        print("The response of DefaultApi->apps_authentication_apple_mobile_api_apple_token_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_apple_mobile_api_apple_token_exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apple_token_exchange_request** | [**AppleTokenExchangeRequest**](AppleTokenExchangeRequest.md)|  | 

### Return type

[**AppleTokenExchangeResponse**](AppleTokenExchangeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**503** | Service Unavailable |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_google_mobile_api_google_token_exchange**
> GoogleTokenExchangeResponse apps_authentication_google_mobile_api_google_token_exchange(google_token_exchange_request)

Google Token Exchange

Exchange a Google ID token (from mobile SDK) for a SpatialFlow JWT.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.google_token_exchange_request import GoogleTokenExchangeRequest
from spatialflow_generated.models.google_token_exchange_response import GoogleTokenExchangeResponse
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
    google_token_exchange_request = spatialflow_generated.GoogleTokenExchangeRequest() # GoogleTokenExchangeRequest | 

    try:
        # Google Token Exchange
        api_response = await api_instance.apps_authentication_google_mobile_api_google_token_exchange(google_token_exchange_request)
        print("The response of DefaultApi->apps_authentication_google_mobile_api_google_token_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_google_mobile_api_google_token_exchange: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_token_exchange_request** | [**GoogleTokenExchangeRequest**](GoogleTokenExchangeRequest.md)|  | 

### Return type

[**GoogleTokenExchangeResponse**](GoogleTokenExchangeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**503** | Service Unavailable |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_oauth_api_get_linked_accounts**
> Dict[str, object] apps_authentication_oauth_api_get_linked_accounts()

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
        api_response = await api_instance.apps_authentication_oauth_api_get_linked_accounts()
        print("The response of DefaultApi->apps_authentication_oauth_api_get_linked_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_oauth_api_get_linked_accounts: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_oauth_api_get_oauth_providers**
> OAuthProvidersResponse apps_authentication_oauth_api_get_oauth_providers()

Get Oauth Providers

Get list of available OAuth providers.  Providers are shown only if: 1. SSO toggle is enabled in Admin UI (Issue #119) 2. Valid credentials are configured (non-placeholder)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_oauth_api_oauth_callback**
> Dict[str, object] apps_authentication_oauth_api_oauth_callback(provider, code, state, error=error, error_description=error_description)

Oauth Callback

Handle OAuth callback from provider. Exchanges code for tokens and creates/links user account.  OAuth state is always invalidated on callback (success, error, or exception) to prevent replay attacks. State tokens are one-time use for CSRF protection.

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
    provider = 'provider_example' # str | 
    code = 'code_example' # str | 
    state = 'state_example' # str | 
    error = 'error_example' # str |  (optional)
    error_description = 'error_description_example' # str |  (optional)

    try:
        # Oauth Callback
        api_response = await api_instance.apps_authentication_oauth_api_oauth_callback(provider, code, state, error=error, error_description=error_description)
        print("The response of DefaultApi->apps_authentication_oauth_api_oauth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_oauth_api_oauth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **code** | **str**|  | 
 **state** | **str**|  | 
 **error** | **str**|  | [optional] 
 **error_description** | **str**|  | [optional] 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_saml_api_detect_method**
> DetectMethodResponse apps_authentication_saml_api_detect_method(detect_method_request)

Detect Method

Detect authentication method for an email address.  Returns 'saml' with workspace slug if the email domain has a SAML configuration, otherwise returns 'password'.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.detect_method_request import DetectMethodRequest
from spatialflow_generated.models.detect_method_response import DetectMethodResponse
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
    detect_method_request = spatialflow_generated.DetectMethodRequest() # DetectMethodRequest | 

    try:
        # Detect Method
        api_response = await api_instance.apps_authentication_saml_api_detect_method(detect_method_request)
        print("The response of DefaultApi->apps_authentication_saml_api_detect_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_saml_api_detect_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detect_method_request** | [**DetectMethodRequest**](DetectMethodRequest.md)|  | 

### Return type

[**DetectMethodResponse**](DetectMethodResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_saml_api_initiate**
> apps_authentication_saml_api_initiate(slug)

Initiate

Initiate SP-initiated SAML login.  Looks up the SAMLConfiguration for the given workspace slug, creates an AuthnRequest via SAMLService, and redirects the browser to the IdP.

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
    slug = 'slug_example' # str | 

    try:
        # Initiate
        await api_instance.apps_authentication_saml_api_initiate(slug)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_saml_api_initiate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_saml_api_metadata**
> apps_authentication_saml_api_metadata(slug)

Metadata

Serve SP metadata XML for IdP configuration.  Returns the SP metadata as application/xml for the given workspace.

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
    slug = 'slug_example' # str | 

    try:
        # Metadata
        await api_instance.apps_authentication_saml_api_metadata(slug)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_saml_api_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_saml_api_saml_acs**
> apps_authentication_saml_api_saml_acs(slug)

Saml Acs

Assertion Consumer Service endpoint.  Receives the SAML response (form POST from IdP), validates the assertion, provisions or links the user, issues JWT tokens via HttpOnly cookies, and redirects to the frontend callback URL.

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
    slug = 'slug_example' # str | 

    try:
        # Saml Acs
        await api_instance.apps_authentication_saml_api_saml_acs(slug)
    except Exception as e:
        print("Exception when calling DefaultApi->apps_authentication_saml_api_saml_acs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

