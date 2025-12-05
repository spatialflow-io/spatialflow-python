# spatialflow_generated.AuthenticationApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_authentication_api_change_password**](AuthenticationApi.md#apps_authentication_api_change_password) | **POST** /api/v1/auth/change-password | Change Password
[**apps_authentication_api_confirm_password_reset**](AuthenticationApi.md#apps_authentication_api_confirm_password_reset) | **POST** /api/v1/auth/password-reset/confirm | Confirm Password Reset
[**apps_authentication_api_forgot_password**](AuthenticationApi.md#apps_authentication_api_forgot_password) | **POST** /api/v1/auth/forgot-password | Forgot Password
[**apps_authentication_api_get_current_user**](AuthenticationApi.md#apps_authentication_api_get_current_user) | **GET** /api/v1/auth/me | Get Current User
[**apps_authentication_api_get_feature_flags**](AuthenticationApi.md#apps_authentication_api_get_feature_flags) | **GET** /api/v1/auth/feature-flags | Get Feature Flags
[**apps_authentication_api_health_check**](AuthenticationApi.md#apps_authentication_api_health_check) | **GET** /api/v1/auth/health | Health Check
[**apps_authentication_api_login**](AuthenticationApi.md#apps_authentication_api_login) | **POST** /api/v1/auth/login | Login
[**apps_authentication_api_logout**](AuthenticationApi.md#apps_authentication_api_logout) | **POST** /api/v1/auth/logout | Logout
[**apps_authentication_api_password_reset_alias**](AuthenticationApi.md#apps_authentication_api_password_reset_alias) | **POST** /api/v1/auth/password-reset | Password Reset Alias
[**apps_authentication_api_refresh_token**](AuthenticationApi.md#apps_authentication_api_refresh_token) | **POST** /api/v1/auth/refresh | Refresh Token
[**apps_authentication_api_register**](AuthenticationApi.md#apps_authentication_api_register) | **POST** /api/v1/auth/register | Register
[**apps_authentication_api_resend_verification**](AuthenticationApi.md#apps_authentication_api_resend_verification) | **POST** /api/v1/auth/resend-verification | Resend Verification
[**apps_authentication_api_resend_verification_email**](AuthenticationApi.md#apps_authentication_api_resend_verification_email) | **POST** /api/v1/auth/resend-verification-email | Resend Verification Email
[**apps_authentication_api_reset_password**](AuthenticationApi.md#apps_authentication_api_reset_password) | **POST** /api/v1/auth/reset-password | Reset Password
[**apps_authentication_api_test_api_key_auth**](AuthenticationApi.md#apps_authentication_api_test_api_key_auth) | **GET** /api/v1/auth/test-api-key | Test Api Key Auth
[**apps_authentication_api_test_jwt_auth**](AuthenticationApi.md#apps_authentication_api_test_jwt_auth) | **GET** /api/v1/auth/test-auth | Test Jwt Auth
[**apps_authentication_api_verify_email**](AuthenticationApi.md#apps_authentication_api_verify_email) | **GET** /api/v1/auth/verify-email | Verify Email
[**apps_authentication_api_verify_email_path**](AuthenticationApi.md#apps_authentication_api_verify_email_path) | **GET** /api/v1/auth/verify-email/{token} | Verify Email Path


# **apps_authentication_api_change_password**
> Dict[str, object] apps_authentication_api_change_password(change_password_schema)

Change Password

Change password for authenticated user.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.change_password_schema import ChangePasswordSchema
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    change_password_schema = spatialflow_generated.ChangePasswordSchema() # ChangePasswordSchema | 

    try:
        # Change Password
        api_response = await api_instance.apps_authentication_api_change_password(change_password_schema)
        print("The response of AuthenticationApi->apps_authentication_api_change_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_change_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_schema** | [**ChangePasswordSchema**](ChangePasswordSchema.md)|  | 

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

# **apps_authentication_api_confirm_password_reset**
> Dict[str, object] apps_authentication_api_confirm_password_reset(confirm_password_reset_schema)

Confirm Password Reset

Confirm password reset with token (simpler API for backwards compatibility).  This endpoint uses the token stored directly in the user model (password_reset_token) rather than Django's default_token_generator with UID encoding.  Security: Tokens are stored as SHA256 hashes, so we hash the incoming token before comparison. This prevents database compromise from exposing usable tokens.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.confirm_password_reset_schema import ConfirmPasswordResetSchema
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    confirm_password_reset_schema = spatialflow_generated.ConfirmPasswordResetSchema() # ConfirmPasswordResetSchema | 

    try:
        # Confirm Password Reset
        api_response = await api_instance.apps_authentication_api_confirm_password_reset(confirm_password_reset_schema)
        print("The response of AuthenticationApi->apps_authentication_api_confirm_password_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_confirm_password_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirm_password_reset_schema** | [**ConfirmPasswordResetSchema**](ConfirmPasswordResetSchema.md)|  | 

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

# **apps_authentication_api_forgot_password**
> Dict[str, object] apps_authentication_api_forgot_password(forgot_password_schema)

Forgot Password

Request password reset email.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.forgot_password_schema import ForgotPasswordSchema
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    forgot_password_schema = spatialflow_generated.ForgotPasswordSchema() # ForgotPasswordSchema | 

    try:
        # Forgot Password
        api_response = await api_instance.apps_authentication_api_forgot_password(forgot_password_schema)
        print("The response of AuthenticationApi->apps_authentication_api_forgot_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_forgot_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forgot_password_schema** | [**ForgotPasswordSchema**](ForgotPasswordSchema.md)|  | 

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

# **apps_authentication_api_get_current_user**
> UserResponse apps_authentication_api_get_current_user()

Get Current User

Get current authenticated user. Requires JWT authentication.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_response import UserResponse
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)

    try:
        # Get Current User
        api_response = await api_instance.apps_authentication_api_get_current_user()
        print("The response of AuthenticationApi->apps_authentication_api_get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_get_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

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

# **apps_authentication_api_get_feature_flags**
> Dict[str, object] apps_authentication_api_get_feature_flags()

Get Feature Flags

Get feature flags for authenticated user.

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)

    try:
        # Get Feature Flags
        api_response = await api_instance.apps_authentication_api_get_feature_flags()
        print("The response of AuthenticationApi->apps_authentication_api_get_feature_flags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_get_feature_flags: %s\n" % e)
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

# **apps_authentication_api_health_check**
> apps_authentication_api_health_check()

Health Check

Health check for authentication service.

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)

    try:
        # Health Check
        await api_instance.apps_authentication_api_health_check()
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_health_check: %s\n" % e)
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

# **apps_authentication_api_login**
> LoginResponse apps_authentication_api_login(login_schema)

Login

User login endpoint. Returns JWT access and refresh tokens, and sets HttpOnly cookies.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.login_response import LoginResponse
from spatialflow_generated.models.login_schema import LoginSchema
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    login_schema = spatialflow_generated.LoginSchema() # LoginSchema | 

    try:
        # Login
        api_response = await api_instance.apps_authentication_api_login(login_schema)
        print("The response of AuthenticationApi->apps_authentication_api_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_schema** | [**LoginSchema**](LoginSchema.md)|  | 

### Return type

[**LoginResponse**](LoginResponse.md)

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

# **apps_authentication_api_logout**
> apps_authentication_api_logout()

Logout

Logout user by revoking all refresh tokens and clearing HttpOnly cookies.

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)

    try:
        # Logout
        await api_instance.apps_authentication_api_logout()
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_logout: %s\n" % e)
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

# **apps_authentication_api_password_reset_alias**
> Dict[str, object] apps_authentication_api_password_reset_alias(forgot_password_schema)

Password Reset Alias

Alias for /forgot-password endpoint (backwards compatibility).

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.forgot_password_schema import ForgotPasswordSchema
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    forgot_password_schema = spatialflow_generated.ForgotPasswordSchema() # ForgotPasswordSchema | 

    try:
        # Password Reset Alias
        api_response = await api_instance.apps_authentication_api_password_reset_alias(forgot_password_schema)
        print("The response of AuthenticationApi->apps_authentication_api_password_reset_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_password_reset_alias: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forgot_password_schema** | [**ForgotPasswordSchema**](ForgotPasswordSchema.md)|  | 

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

# **apps_authentication_api_refresh_token**
> LoginResponse apps_authentication_api_refresh_token(refresh_token_schema=refresh_token_schema)

Refresh Token

Refresh access token using refresh token. Supports both body payload and HttpOnly cookie for refresh token.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.login_response import LoginResponse
from spatialflow_generated.models.refresh_token_schema import RefreshTokenSchema
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    refresh_token_schema = spatialflow_generated.RefreshTokenSchema() # RefreshTokenSchema |  (optional)

    try:
        # Refresh Token
        api_response = await api_instance.apps_authentication_api_refresh_token(refresh_token_schema=refresh_token_schema)
        print("The response of AuthenticationApi->apps_authentication_api_refresh_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_refresh_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_token_schema** | [**RefreshTokenSchema**](RefreshTokenSchema.md)|  | [optional] 

### Return type

[**LoginResponse**](LoginResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_register**
> UserResponse apps_authentication_api_register(register_schema)

Register

DEPRECATED: User registration endpoint.  This endpoint is deprecated and will be removed in a future version. Please use /api/v1/public/signup instead, which includes: - Beta mode support with admin approval workflow - Proper admin notifications - Enhanced tracking and analytics  This endpoint remains for backward compatibility but lacks beta features.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.register_schema import RegisterSchema
from spatialflow_generated.models.user_response import UserResponse
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    register_schema = spatialflow_generated.RegisterSchema() # RegisterSchema | 

    try:
        # Register
        api_response = await api_instance.apps_authentication_api_register(register_schema)
        print("The response of AuthenticationApi->apps_authentication_api_register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_schema** | [**RegisterSchema**](RegisterSchema.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_resend_verification**
> Dict[str, object] apps_authentication_api_resend_verification()

Resend Verification

Resend verification email.

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)

    try:
        # Resend Verification
        api_response = await api_instance.apps_authentication_api_resend_verification()
        print("The response of AuthenticationApi->apps_authentication_api_resend_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_resend_verification: %s\n" % e)
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

# **apps_authentication_api_resend_verification_email**
> Dict[str, object] apps_authentication_api_resend_verification_email(resend_verification_schema)

Resend Verification Email

Resend verification email (unauthenticated endpoint with rate limiting). Allows users who haven't verified their email to request a new verification email. Rate limited to 3 requests per hour per email to prevent abuse.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.resend_verification_schema import ResendVerificationSchema
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    resend_verification_schema = spatialflow_generated.ResendVerificationSchema() # ResendVerificationSchema | 

    try:
        # Resend Verification Email
        api_response = await api_instance.apps_authentication_api_resend_verification_email(resend_verification_schema)
        print("The response of AuthenticationApi->apps_authentication_api_resend_verification_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_resend_verification_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resend_verification_schema** | [**ResendVerificationSchema**](ResendVerificationSchema.md)|  | 

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_reset_password**
> apps_authentication_api_reset_password(reset_password_schema)

Reset Password

DEPRECATED: This endpoint used Django's default_token_generator with UID encoding.  This flow is no longer supported. All password reset links now use the simpler /password-reset/confirm endpoint with hashed token storage.  If you have an old reset link, please request a new one via /forgot-password.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.reset_password_schema import ResetPasswordSchema
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    reset_password_schema = spatialflow_generated.ResetPasswordSchema() # ResetPasswordSchema | 

    try:
        # Reset Password
        await api_instance.apps_authentication_api_reset_password(reset_password_schema)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password_schema** | [**ResetPasswordSchema**](ResetPasswordSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**410** | Gone |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_test_api_key_auth**
> apps_authentication_api_test_api_key_auth()

Test Api Key Auth

Test endpoint for API key authentication.

### Example

* Api Key Authentication (APIKeyBearer):

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

# Enter a context with an instance of the API client
async with spatialflow_generated.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spatialflow_generated.AuthenticationApi(api_client)

    try:
        # Test Api Key Auth
        await api_instance.apps_authentication_api_test_api_key_auth()
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_test_api_key_auth: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[APIKeyBearer](../README.md#APIKeyBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_test_jwt_auth**
> apps_authentication_api_test_jwt_auth()

Test Jwt Auth

Test endpoint for JWT authentication.

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)

    try:
        # Test Jwt Auth
        await api_instance.apps_authentication_api_test_jwt_auth()
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_test_jwt_auth: %s\n" % e)
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

# **apps_authentication_api_verify_email**
> Dict[str, object] apps_authentication_api_verify_email(token)

Verify Email

Verify email address (query parameter format).

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    token = 'token_example' # str | 

    try:
        # Verify Email
        api_response = await api_instance.apps_authentication_api_verify_email(token)
        print("The response of AuthenticationApi->apps_authentication_api_verify_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_verify_email: %s\n" % e)
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

# **apps_authentication_api_verify_email_path**
> Dict[str, object] apps_authentication_api_verify_email_path(token)

Verify Email Path

Verify email address (path parameter format for backwards compatibility).

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    token = 'token_example' # str | 

    try:
        # Verify Email Path
        api_response = await api_instance.apps_authentication_api_verify_email_path(token)
        print("The response of AuthenticationApi->apps_authentication_api_verify_email_path:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_verify_email_path: %s\n" % e)
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

