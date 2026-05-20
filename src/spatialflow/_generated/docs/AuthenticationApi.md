# spatialflow_generated.AuthenticationApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_authentication_api_accept_invitation**](AuthenticationApi.md#apps_authentication_api_accept_invitation) | **POST** /api/v1/auth/accept-invite | Accept Invitation
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
[**apps_authentication_api_resend_verification**](AuthenticationApi.md#apps_authentication_api_resend_verification) | **POST** /api/v1/auth/resend-verification-authenticated | Resend Verification
[**apps_authentication_api_resend_verification_alias**](AuthenticationApi.md#apps_authentication_api_resend_verification_alias) | **POST** /api/v1/auth/resend-verification | Resend Verification Alias
[**apps_authentication_api_resend_verification_email**](AuthenticationApi.md#apps_authentication_api_resend_verification_email) | **POST** /api/v1/auth/resend-verification-email | Resend Verification Email
[**apps_authentication_api_reset_password**](AuthenticationApi.md#apps_authentication_api_reset_password) | **POST** /api/v1/auth/reset-password | Reset Password
[**apps_authentication_api_sso_start**](AuthenticationApi.md#apps_authentication_api_sso_start) | **GET** /api/v1/auth/sso/start | Sso Start
[**apps_authentication_api_verify_email**](AuthenticationApi.md#apps_authentication_api_verify_email) | **GET** /api/v1/auth/verify-email | Verify Email
[**apps_authentication_api_verify_email_path**](AuthenticationApi.md#apps_authentication_api_verify_email_path) | **GET** /api/v1/auth/verify-email/{token} | Verify Email Path
[**apps_authentication_api_verify_email_post**](AuthenticationApi.md#apps_authentication_api_verify_email_post) | **POST** /api/v1/auth/verify-email | Verify Email Post
[**apps_authentication_apple_mobile_api_apple_nonce**](AuthenticationApi.md#apps_authentication_apple_mobile_api_apple_nonce) | **POST** /api/v1/auth/apple/nonce | Apple Nonce
[**apps_authentication_apple_mobile_api_apple_token_exchange**](AuthenticationApi.md#apps_authentication_apple_mobile_api_apple_token_exchange) | **POST** /api/v1/auth/apple/token-exchange | Apple Token Exchange
[**apps_authentication_google_mobile_api_google_token_exchange**](AuthenticationApi.md#apps_authentication_google_mobile_api_google_token_exchange) | **POST** /api/v1/auth/google/token-exchange | Google Token Exchange
[**apps_authentication_oauth_api_disconnect_oauth_account**](AuthenticationApi.md#apps_authentication_oauth_api_disconnect_oauth_account) | **DELETE** /api/v1/auth/oauth/{provider}/disconnect | Disconnect Oauth Account
[**apps_authentication_oauth_api_get_linked_accounts**](AuthenticationApi.md#apps_authentication_oauth_api_get_linked_accounts) | **GET** /api/v1/auth/oauth/user/linked-accounts | Get Linked Accounts
[**apps_authentication_oauth_api_get_oauth_providers**](AuthenticationApi.md#apps_authentication_oauth_api_get_oauth_providers) | **GET** /api/v1/auth/oauth/providers | Get Oauth Providers
[**apps_authentication_oauth_api_link_oauth_account**](AuthenticationApi.md#apps_authentication_oauth_api_link_oauth_account) | **POST** /api/v1/auth/oauth/{provider}/link | Link Oauth Account
[**apps_authentication_oauth_api_oauth_authorize**](AuthenticationApi.md#apps_authentication_oauth_api_oauth_authorize) | **GET** /api/v1/auth/oauth/{provider}/authorize | Oauth Authorize
[**apps_authentication_oauth_api_oauth_callback**](AuthenticationApi.md#apps_authentication_oauth_api_oauth_callback) | **GET** /api/v1/auth/oauth/{provider}/callback | Oauth Callback
[**apps_authentication_saml_api_detect_method**](AuthenticationApi.md#apps_authentication_saml_api_detect_method) | **POST** /api/v1/auth/saml/detect-method | Detect Method
[**apps_authentication_saml_api_initiate**](AuthenticationApi.md#apps_authentication_saml_api_initiate) | **GET** /api/v1/auth/saml/{slug}/initiate | Initiate
[**apps_authentication_saml_api_metadata**](AuthenticationApi.md#apps_authentication_saml_api_metadata) | **GET** /api/v1/auth/saml/{slug}/metadata | Metadata
[**apps_authentication_saml_api_saml_acs**](AuthenticationApi.md#apps_authentication_saml_api_saml_acs) | **POST** /api/v1/auth/saml/{slug}/acs | Saml Acs


# **apps_authentication_api_accept_invitation**
> Dict[str, object] apps_authentication_api_accept_invitation(accept_invite_schema)

Accept Invitation

Accept a workspace invitation and optionally set password.  Security features (Issue #67): - Uses Invitation model with hashed token storage - Atomic transaction prevents race conditions on double-accept - Token validated via SHA256 hash comparison - Single-use enforcement (used_at timestamp) - Sibling invites auto-revoked on acceptance - Clears stale verification tokens on acceptance  Phase 77 WR-03 — strict email-match guard against authenticated session. If the request carries a valid JWT and the authenticated user's email does NOT match the invitation's email, reject with 409 + error_code INVITE_EMAIL_MISMATCH. Mirrors the guard in google_mobile_api.py and invite_sso_service.resolve_for_callback so the threat-model claim \"Email-mismatch: must NOT add user to workspace\" is enforced on the password path as well as the Google path. The mobile client now force-logs-out before reaching this endpoint (CR-01), so this is a defense-in-depth check for any other caller (web, raw API consumers).  Args:     data.token: Invitation token (plaintext, will be hashed for lookup)     data.invite_id: Invitation ID (UUID)     data.password: New password (optional for existing users with password)  Returns:     200: Success with access/refresh tokens     400: Invalid state (already used, revoked, expired, invalid password)     404: Invalid token/invite_id combination     409: Authenticated session email does not match invitation email

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.accept_invite_schema import AcceptInviteSchema
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
    accept_invite_schema = spatialflow_generated.AcceptInviteSchema() # AcceptInviteSchema | 

    try:
        # Accept Invitation
        api_response = await api_instance.apps_authentication_api_accept_invitation(accept_invite_schema)
        print("The response of AuthenticationApi->apps_authentication_api_accept_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_accept_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_invite_schema** | [**AcceptInviteSchema**](AcceptInviteSchema.md)|  | 

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

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
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_forgot_password**
> Dict[str, object] apps_authentication_api_forgot_password(forgot_password_schema)

Forgot Password

Request password reset email.  Rate limited: 10/hour per IP, 3/hour per email (Issue #67 security hardening).

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
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_health_check**
> Dict[str, object] apps_authentication_api_health_check()

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
        api_response = await api_instance.apps_authentication_api_health_check()
        print("The response of AuthenticationApi->apps_authentication_api_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_health_check: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_login**
> LoginResponse apps_authentication_api_login(login_schema)

Login

User login endpoint. Returns JWT access and refresh tokens, and sets HttpOnly cookies.  Rate limited: 60/min per IP, 15/min per email. Per-email limit raised from 5/m (Issue #67) to 15/m (Issue #242) to reduce false lockouts from mobile retries on flaky networks, typos, and app restarts. IP limit remains the primary abuse deterrent.

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
**429** | Too Many Requests |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_refresh_token**
> LoginResponse apps_authentication_api_refresh_token(refresh_token_schema=refresh_token_schema)

Refresh Token

Refresh access token using refresh token. Supports both body payload and HttpOnly cookie for refresh token.  Rate limited: 30/min per token + 100/min per IP.

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
**429** | Too Many Requests |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_register**
> apps_authentication_api_register(register_schema)

Register

DEPRECATED: User registration endpoint.  This endpoint is deprecated and will be removed in a future version. Please use /api/v1/public/signup instead, which includes: - Admin notifications - Enhanced tracking and analytics

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.register_schema import RegisterSchema
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
        await api_instance.apps_authentication_api_register(register_schema)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_register: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_schema** | [**RegisterSchema**](RegisterSchema.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_resend_verification**
> Dict[str, object] apps_authentication_api_resend_verification()

Resend Verification

Resend verification email for authenticated user.

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_resend_verification_alias**
> Dict[str, object] apps_authentication_api_resend_verification_alias(resend_verification_schema)

Resend Verification Alias

Resend verification email (unauthenticated alias for backwards compatibility).  Security (Issue #67): - Generates new token (invalidates previous) - Token stored as SHA256 hash - Token expires per settings.EMAIL_VERIFICATION_TTL_HOURS (default 24h)  Rate limited to 3 requests per hour per email to prevent abuse.

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
        # Resend Verification Alias
        api_response = await api_instance.apps_authentication_api_resend_verification_alias(resend_verification_schema)
        print("The response of AuthenticationApi->apps_authentication_api_resend_verification_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_resend_verification_alias: %s\n" % e)
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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_resend_verification_email**
> Dict[str, object] apps_authentication_api_resend_verification_email(resend_verification_schema)

Resend Verification Email

Resend verification email (unauthenticated endpoint with rate limiting). Allows users who haven't verified their email to request a new verification email.  Security (Issue #67): - Generates new token (invalidates previous) - Token stored as SHA256 hash - Token expires per settings.EMAIL_VERIFICATION_TTL_HOURS (default 24h)  Rate limited to 3 requests per hour per email to prevent abuse.

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_sso_start**
> apps_authentication_api_sso_start(var_return, workspace_slug)

Sso Start

Initiate SAML SSO from mobile app.  Validates the `return` deeplink URL against an allowlist (spatialflow://, spatialflowdev://) to prevent open-redirect abuse (D-06), then delegates to the existing SP-initiated SAML flow for the given workspace slug. On success, the SAML ACS handler will redirect back to `return` with ?token=<jwt>&refresh=<refresh> appended (D-04).  Returns:     302: Redirect to IdP login page.     400: Invalid return URL or SAML configuration error.

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
    var_return = 'var_return_example' # str | 
    workspace_slug = 'workspace_slug_example' # str | 

    try:
        # Sso Start
        await api_instance.apps_authentication_api_sso_start(var_return, workspace_slug)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_sso_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_return** | **str**|  | 
 **workspace_slug** | **str**|  | 

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
**302** | Found |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_verify_email**
> Dict[str, object] apps_authentication_api_verify_email(token)

Verify Email

Verify email address (GET method, backwards compatible).  Note: This endpoint accepts plaintext tokens for backwards compatibility with existing verification links. New tokens are stored hashed, so it tries both plaintext lookup (for old tokens) and hash lookup (for new tokens).

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_api_verify_email_post**
> Dict[str, object] apps_authentication_api_verify_email_post(verify_email_schema)

Verify Email Post

Verify email address (POST method with enhanced security).  Security features (Issue #67): - Token stored as SHA256 hash (not plaintext) - Token has configurable expiration (default 24h via settings.EMAIL_VERIFICATION_TTL_HOURS) - Single-use: token cleared after successful verification - Dual rate limiting: 20/hour per IP, 5/hour per token  Args:     data.token: Verification token (plaintext, will be hashed for lookup)  Returns:     200: Success with verification status     400: Invalid, expired, or already used token     429: Rate limit exceeded

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.verify_email_schema import VerifyEmailSchema
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
    verify_email_schema = spatialflow_generated.VerifyEmailSchema() # VerifyEmailSchema | 

    try:
        # Verify Email Post
        api_response = await api_instance.apps_authentication_api_verify_email_post(verify_email_schema)
        print("The response of AuthenticationApi->apps_authentication_api_verify_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_api_verify_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_email_schema** | [**VerifyEmailSchema**](VerifyEmailSchema.md)|  | 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)

    try:
        # Apple Nonce
        api_response = await api_instance.apps_authentication_apple_mobile_api_apple_nonce()
        print("The response of AuthenticationApi->apps_authentication_apple_mobile_api_apple_nonce:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_apple_mobile_api_apple_nonce: %s\n" % e)
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    apple_token_exchange_request = spatialflow_generated.AppleTokenExchangeRequest() # AppleTokenExchangeRequest | 

    try:
        # Apple Token Exchange
        api_response = await api_instance.apps_authentication_apple_mobile_api_apple_token_exchange(apple_token_exchange_request)
        print("The response of AuthenticationApi->apps_authentication_apple_mobile_api_apple_token_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_apple_mobile_api_apple_token_exchange: %s\n" % e)
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

Exchange a Google ID token (from mobile SDK) for a SpatialFlow JWT.  Phase 74: when both `invite_id` and `invite_token` are provided, the request is routed through invite_sso_service for strict email-match reconciliation against the targeted Invitation (INVT-IDENT-01). On mismatch, no User/SocialAccount/Membership/Invitation mutation occurs. When invite params are absent, the call falls through to today's implicit email-match auto-join via provision_workspace_for_new_user (D-22).

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    google_token_exchange_request = spatialflow_generated.GoogleTokenExchangeRequest() # GoogleTokenExchangeRequest | 

    try:
        # Google Token Exchange
        api_response = await api_instance.apps_authentication_google_mobile_api_google_token_exchange(google_token_exchange_request)
        print("The response of AuthenticationApi->apps_authentication_google_mobile_api_google_token_exchange:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_google_mobile_api_google_token_exchange: %s\n" % e)
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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**403** | Forbidden |  -  |
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Disconnect Oauth Account
        api_response = await api_instance.apps_authentication_oauth_api_disconnect_oauth_account(provider)
        print("The response of AuthenticationApi->apps_authentication_oauth_api_disconnect_oauth_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_oauth_api_disconnect_oauth_account: %s\n" % e)
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)

    try:
        # Get Linked Accounts
        await api_instance.apps_authentication_oauth_api_get_linked_accounts()
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_oauth_api_get_linked_accounts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)

    try:
        # Get Oauth Providers
        api_response = await api_instance.apps_authentication_oauth_api_get_oauth_providers()
        print("The response of AuthenticationApi->apps_authentication_oauth_api_get_oauth_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_oauth_api_get_oauth_providers: %s\n" % e)
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    provider = 'provider_example' # str | 

    try:
        # Link Oauth Account
        api_response = await api_instance.apps_authentication_oauth_api_link_oauth_account(provider)
        print("The response of AuthenticationApi->apps_authentication_oauth_api_link_oauth_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_oauth_api_link_oauth_account: %s\n" % e)
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
> OAuthAuthorizeResponse apps_authentication_oauth_api_oauth_authorize(provider, next=next, invite_id=invite_id, invite_token=invite_token)

Oauth Authorize

Initialize OAuth flow for a provider.  When `invite_id` and `invite_token` are both provided (Phase 74 / D-02), the invitation is validated server-side and bound to the AuthOAuthState for recovery on the callback. Either-missing falls through to the standard sign-in flow (D-22 backward compat).

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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    provider = 'provider_example' # str | 
    next = 'next_example' # str |  (optional)
    invite_id = 'invite_id_example' # str |  (optional)
    invite_token = 'invite_token_example' # str |  (optional)

    try:
        # Oauth Authorize
        api_response = await api_instance.apps_authentication_oauth_api_oauth_authorize(provider, next=next, invite_id=invite_id, invite_token=invite_token)
        print("The response of AuthenticationApi->apps_authentication_oauth_api_oauth_authorize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_oauth_api_oauth_authorize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**|  | 
 **next** | **str**|  | [optional] 
 **invite_id** | **str**|  | [optional] 
 **invite_token** | **str**|  | [optional] 

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
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_authentication_oauth_api_oauth_callback**
> apps_authentication_oauth_api_oauth_callback(provider, code, state, error=error, error_description=error_description)

Oauth Callback

Handle OAuth callback from provider. Exchanges code for tokens and creates/links user account.  OAuth state is always invalidated on callback (success, error, or exception) to prevent replay attacks. State tokens are one-time use for CSRF protection.  Phase 74: When the OAuth state has a bound Invitation (invite-driven SSO flow), recovers the FK and routes through invite_sso_service.resolve_for_callback. On email match: creates WorkspaceMembership, marks invite used, delivers JWT. On mismatch: redirects to accept-invite page with error_code (D-12).

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
    provider = 'provider_example' # str | 
    code = 'code_example' # str | 
    state = 'state_example' # str | 
    error = 'error_example' # str |  (optional)
    error_description = 'error_description_example' # str |  (optional)

    try:
        # Oauth Callback
        await api_instance.apps_authentication_oauth_api_oauth_callback(provider, code, state, error=error, error_description=error_description)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_oauth_api_oauth_callback: %s\n" % e)
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    detect_method_request = spatialflow_generated.DetectMethodRequest() # DetectMethodRequest | 

    try:
        # Detect Method
        api_response = await api_instance.apps_authentication_saml_api_detect_method(detect_method_request)
        print("The response of AuthenticationApi->apps_authentication_saml_api_detect_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_saml_api_detect_method: %s\n" % e)
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    slug = 'slug_example' # str | 

    try:
        # Initiate
        await api_instance.apps_authentication_saml_api_initiate(slug)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_saml_api_initiate: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    slug = 'slug_example' # str | 

    try:
        # Metadata
        await api_instance.apps_authentication_saml_api_metadata(slug)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_saml_api_metadata: %s\n" % e)
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
    api_instance = spatialflow_generated.AuthenticationApi(api_client)
    slug = 'slug_example' # str | 

    try:
        # Saml Acs
        await api_instance.apps_authentication_saml_api_saml_acs(slug)
    except Exception as e:
        print("Exception when calling AuthenticationApi->apps_authentication_saml_api_saml_acs: %s\n" % e)
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

