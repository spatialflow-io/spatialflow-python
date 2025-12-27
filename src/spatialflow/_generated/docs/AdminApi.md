# spatialflow_generated.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_admin_portal_api_activate_user**](AdminApi.md#apps_admin_portal_api_activate_user) | **PUT** /api/v1/admin/users/{user_id}/activate | Activate User
[**apps_admin_portal_api_admin_health_check**](AdminApi.md#apps_admin_portal_api_admin_health_check) | **GET** /api/v1/admin/health | Admin Health Check
[**apps_admin_portal_api_admin_ping**](AdminApi.md#apps_admin_portal_api_admin_ping) | **GET** /api/v1/admin/ping | Admin Ping
[**apps_admin_portal_api_admin_reset_password**](AdminApi.md#apps_admin_portal_api_admin_reset_password) | **POST** /api/v1/admin/users/{user_id}/reset-password | Admin Reset Password
[**apps_admin_portal_api_approve_user**](AdminApi.md#apps_admin_portal_api_approve_user) | **POST** /api/v1/admin/users/{user_id}/approve | Approve User
[**apps_admin_portal_api_deactivate_user**](AdminApi.md#apps_admin_portal_api_deactivate_user) | **PUT** /api/v1/admin/users/{user_id}/deactivate | Deactivate User
[**apps_admin_portal_api_delete_user**](AdminApi.md#apps_admin_portal_api_delete_user) | **DELETE** /api/v1/admin/users/{user_id} | Delete User
[**apps_admin_portal_api_delete_workspace**](AdminApi.md#apps_admin_portal_api_delete_workspace) | **DELETE** /api/v1/admin/workspaces/{workspace_id} | Delete Workspace
[**apps_admin_portal_api_get_user_usage**](AdminApi.md#apps_admin_portal_api_get_user_usage) | **GET** /api/v1/admin/users/{user_id}/usage | Get User Usage
[**apps_admin_portal_api_get_users_with_stats**](AdminApi.md#apps_admin_portal_api_get_users_with_stats) | **GET** /api/v1/admin/users/stats | Get Users With Stats
[**apps_admin_portal_api_get_workspace**](AdminApi.md#apps_admin_portal_api_get_workspace) | **GET** /api/v1/admin/workspaces/{workspace_id} | Get Workspace
[**apps_admin_portal_api_get_workspace_members**](AdminApi.md#apps_admin_portal_api_get_workspace_members) | **GET** /api/v1/admin/workspaces/{workspace_id}/members | Get Workspace Members
[**apps_admin_portal_api_invite_user**](AdminApi.md#apps_admin_portal_api_invite_user) | **POST** /api/v1/admin/users/invite | Invite User
[**apps_admin_portal_api_list_pending_users**](AdminApi.md#apps_admin_portal_api_list_pending_users) | **GET** /api/v1/admin/users/pending | List Pending Users
[**apps_admin_portal_api_list_users**](AdminApi.md#apps_admin_portal_api_list_users) | **GET** /api/v1/admin/users | List Users
[**apps_admin_portal_api_list_workspaces**](AdminApi.md#apps_admin_portal_api_list_workspaces) | **GET** /api/v1/admin/workspaces | List Workspaces
[**apps_admin_portal_api_reject_user**](AdminApi.md#apps_admin_portal_api_reject_user) | **POST** /api/v1/admin/users/{user_id}/reject | Reject User
[**apps_admin_portal_api_remove_member**](AdminApi.md#apps_admin_portal_api_remove_member) | **DELETE** /api/v1/admin/workspaces/{workspace_id}/members/{user_id} | Remove Member
[**apps_admin_portal_api_remove_user_workspace**](AdminApi.md#apps_admin_portal_api_remove_user_workspace) | **DELETE** /api/v1/admin/users/{user_id}/workspace | Remove User Workspace
[**apps_admin_portal_api_resend_password_reset**](AdminApi.md#apps_admin_portal_api_resend_password_reset) | **POST** /api/v1/admin/users/{user_id}/resend-reset | Resend Password Reset
[**apps_admin_portal_api_resend_verification_email**](AdminApi.md#apps_admin_portal_api_resend_verification_email) | **POST** /api/v1/admin/users/{user_id}/resend-verification | Resend Verification Email
[**apps_admin_portal_api_revoke_invitation**](AdminApi.md#apps_admin_portal_api_revoke_invitation) | **DELETE** /api/v1/admin/invitations/{invite_id} | Revoke Invitation
[**apps_admin_portal_api_update_member_role**](AdminApi.md#apps_admin_portal_api_update_member_role) | **PATCH** /api/v1/admin/workspaces/{workspace_id}/members/{user_id} | Update Member Role
[**apps_admin_portal_api_update_user_workspace**](AdminApi.md#apps_admin_portal_api_update_user_workspace) | **PATCH** /api/v1/admin/users/{user_id}/workspace | Update User Workspace
[**apps_admin_portal_api_update_workspace**](AdminApi.md#apps_admin_portal_api_update_workspace) | **PUT** /api/v1/admin/workspaces/{workspace_id} | Update Workspace


# **apps_admin_portal_api_activate_user**
> UserActionResponse apps_admin_portal_api_activate_user(user_id)

Activate User

Activate a user account (set email_verified=True).

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_action_response import UserActionResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Activate User
        api_response = await api_instance.apps_admin_portal_api_activate_user(user_id)
        print("The response of AdminApi->apps_admin_portal_api_activate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_activate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserActionResponse**](UserActionResponse.md)

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

# **apps_admin_portal_api_admin_health_check**
> HealthCheckResponse apps_admin_portal_api_admin_health_check()

Admin Health Check

Comprehensive health check for admin service.

### Example


```python
import spatialflow_generated
from spatialflow_generated.models.health_check_response import HealthCheckResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)

    try:
        # Admin Health Check
        api_response = await api_instance.apps_admin_portal_api_admin_health_check()
        print("The response of AdminApi->apps_admin_portal_api_admin_health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_admin_health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthCheckResponse**](HealthCheckResponse.md)

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

# **apps_admin_portal_api_admin_ping**
> PingResponse apps_admin_portal_api_admin_ping()

Admin Ping

Simple health check for admin API (requires admin auth).

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.ping_response import PingResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)

    try:
        # Admin Ping
        api_response = await api_instance.apps_admin_portal_api_admin_ping()
        print("The response of AdminApi->apps_admin_portal_api_admin_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_admin_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

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

# **apps_admin_portal_api_admin_reset_password**
> UserActionResponse apps_admin_portal_api_admin_reset_password(user_id)

Admin Reset Password

Admin-initiated password reset for a user.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_action_response import UserActionResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Admin Reset Password
        api_response = await api_instance.apps_admin_portal_api_admin_reset_password(user_id)
        print("The response of AdminApi->apps_admin_portal_api_admin_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_admin_reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserActionResponse**](UserActionResponse.md)

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

# **apps_admin_portal_api_approve_user**
> UserActionResponse apps_admin_portal_api_approve_user(user_id, user_approval_request)

Approve User

Approve a pending user account (for beta signups requiring approval).

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_action_response import UserActionResponse
from spatialflow_generated.models.user_approval_request import UserApprovalRequest
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 
    user_approval_request = spatialflow_generated.UserApprovalRequest() # UserApprovalRequest | 

    try:
        # Approve User
        api_response = await api_instance.apps_admin_portal_api_approve_user(user_id, user_approval_request)
        print("The response of AdminApi->apps_admin_portal_api_approve_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_approve_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_approval_request** | [**UserApprovalRequest**](UserApprovalRequest.md)|  | 

### Return type

[**UserActionResponse**](UserActionResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_admin_portal_api_deactivate_user**
> UserActionResponse apps_admin_portal_api_deactivate_user(user_id)

Deactivate User

Deactivate a user account (set email_verified=False).

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_action_response import UserActionResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Deactivate User
        api_response = await api_instance.apps_admin_portal_api_deactivate_user(user_id)
        print("The response of AdminApi->apps_admin_portal_api_deactivate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_deactivate_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserActionResponse**](UserActionResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_admin_portal_api_delete_user**
> Dict[str, object] apps_admin_portal_api_delete_user(user_id, confirm_workspace_deletion=confirm_workspace_deletion)

Delete User

Delete a user with proper cascade cleanup (Issue #67).

Workspace Deletion Policy:
- Delete workspace when member count reaches ZERO (any role)
- Shared workspaces with other members: remove membership only
- This prevents orphaned workspaces regardless of user's role

Args:
    user_id: UUID of user to delete
    confirm_workspace_deletion: Query param - must be True to delete last-member workspaces

Returns:
    200: Summary of deleted data
    400: User is last member without confirmation, self-deletion, etc.
    404: User not found
    500: Server error

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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 
    confirm_workspace_deletion = False # bool |  (optional) (default to False)

    try:
        # Delete User
        api_response = await api_instance.apps_admin_portal_api_delete_user(user_id, confirm_workspace_deletion=confirm_workspace_deletion)
        print("The response of AdminApi->apps_admin_portal_api_delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **confirm_workspace_deletion** | **bool**|  | [optional] [default to False]

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_admin_portal_api_delete_workspace**
> WorkspaceDeleteResponse apps_admin_portal_api_delete_workspace(workspace_id)

Delete Workspace

Delete workspace (hard delete with safety checks).
Workspace must have 0 members before deletion.
Cancels Stripe subscription and deletes all related data via CASCADE.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_delete_response import WorkspaceDeleteResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Delete Workspace
        api_response = await api_instance.apps_admin_portal_api_delete_workspace(workspace_id)
        print("The response of AdminApi->apps_admin_portal_api_delete_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**WorkspaceDeleteResponse**](WorkspaceDeleteResponse.md)

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

# **apps_admin_portal_api_get_user_usage**
> UserUsageResponse apps_admin_portal_api_get_user_usage(user_id)

Get User Usage

Get usage statistics for a specific user.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_usage_response import UserUsageResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User Usage
        api_response = await api_instance.apps_admin_portal_api_get_user_usage(user_id)
        print("The response of AdminApi->apps_admin_portal_api_get_user_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_get_user_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserUsageResponse**](UserUsageResponse.md)

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

# **apps_admin_portal_api_get_users_with_stats**
> AdminUserStatsResponse apps_admin_portal_api_get_users_with_stats(days=days, limit=limit, offset=offset, sort=sort, user_ids=user_ids)

Get Users With Stats

Get users with API call counts for admin dashboard.

Returns aggregated API call counts per user within the specified date range.
Health/admin/docs paths are already excluded by APIUsageTrackingMiddleware.

Args:
    days: Number of days to look back (default 30, max 90)
    limit: Maximum results per page (default 50, max 100)
    offset: Number of results to skip for pagination
    sort: Sort by "api_calls" (descending) or "email" (ascending)
    user_ids: Optional comma-separated UUIDs to scope to specific users

Returns:
    200: List of users with their API call counts
    403: User is not an admin
    500: Internal server error

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.admin_user_stats_response import AdminUserStatsResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    days = 30 # int |  (optional) (default to 30)
    limit = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    sort = 'api_calls' # str |  (optional) (default to 'api_calls')
    user_ids = 'user_ids_example' # str |  (optional)

    try:
        # Get Users With Stats
        api_response = await api_instance.apps_admin_portal_api_get_users_with_stats(days=days, limit=limit, offset=offset, sort=sort, user_ids=user_ids)
        print("The response of AdminApi->apps_admin_portal_api_get_users_with_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_get_users_with_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **days** | **int**|  | [optional] [default to 30]
 **limit** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **sort** | **str**|  | [optional] [default to &#39;api_calls&#39;]
 **user_ids** | **str**|  | [optional] 

### Return type

[**AdminUserStatsResponse**](AdminUserStatsResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_admin_portal_api_get_workspace**
> WorkspaceDetailResponse apps_admin_portal_api_get_workspace(workspace_id)

Get Workspace

Get detailed information about a specific workspace.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_detail_response import WorkspaceDetailResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    workspace_id = 'workspace_id_example' # str | 

    try:
        # Get Workspace
        api_response = await api_instance.apps_admin_portal_api_get_workspace(workspace_id)
        print("The response of AdminApi->apps_admin_portal_api_get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_get_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 

### Return type

[**WorkspaceDetailResponse**](WorkspaceDetailResponse.md)

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

# **apps_admin_portal_api_get_workspace_members**
> WorkspaceMembersResponse apps_admin_portal_api_get_workspace_members(workspace_id, page=page, limit=limit)

Get Workspace Members

Get paginated list of members in a workspace.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_members_response import WorkspaceMembersResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)

    try:
        # Get Workspace Members
        api_response = await api_instance.apps_admin_portal_api_get_workspace_members(workspace_id, page=page, limit=limit)
        print("The response of AdminApi->apps_admin_portal_api_get_workspace_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_get_workspace_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 20]

### Return type

[**WorkspaceMembersResponse**](WorkspaceMembersResponse.md)

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

# **apps_admin_portal_api_invite_user**
> UserInviteResponse apps_admin_portal_api_invite_user(user_invite_request)

Invite User

Invite new user to a workspace via email.

If workspace_id is None or empty, creates a new workspace for the user.
The user becomes owner of new workspaces, or gets the requested role for existing ones.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_invite_request import UserInviteRequest
from spatialflow_generated.models.user_invite_response import UserInviteResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_invite_request = spatialflow_generated.UserInviteRequest() # UserInviteRequest | 

    try:
        # Invite User
        api_response = await api_instance.apps_admin_portal_api_invite_user(user_invite_request)
        print("The response of AdminApi->apps_admin_portal_api_invite_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_invite_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_invite_request** | [**UserInviteRequest**](UserInviteRequest.md)|  | 

### Return type

[**UserInviteResponse**](UserInviteResponse.md)

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

# **apps_admin_portal_api_list_pending_users**
> UserListResponse apps_admin_portal_api_list_pending_users(limit=limit, cursor=cursor)

List Pending Users

List all users pending admin approval.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_list_response import UserListResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    limit = 20 # int |  (optional) (default to 20)
    cursor = 'cursor_example' # str |  (optional)

    try:
        # List Pending Users
        api_response = await api_instance.apps_admin_portal_api_list_pending_users(limit=limit, cursor=cursor)
        print("The response of AdminApi->apps_admin_portal_api_list_pending_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_list_pending_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 20]
 **cursor** | **str**|  | [optional] 

### Return type

[**UserListResponse**](UserListResponse.md)

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

# **apps_admin_portal_api_list_users**
> UserListResponse apps_admin_portal_api_list_users(page=page, limit=limit, search=search, role=role, status=status)

List Users

Get paginated list of users with filtering options.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_list_response import UserListResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str |  (optional)
    role = 'role_example' # str |  (optional)
    status = 'status_example' # str |  (optional)

    try:
        # List Users
        api_response = await api_instance.apps_admin_portal_api_list_users(page=page, limit=limit, search=search, role=role, status=status)
        print("The response of AdminApi->apps_admin_portal_api_list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 20]
 **search** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 

### Return type

[**UserListResponse**](UserListResponse.md)

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

# **apps_admin_portal_api_list_workspaces**
> WorkspaceListResponse apps_admin_portal_api_list_workspaces(page=page, limit=limit, search=search)

List Workspaces

Get paginated list of workspaces with filtering options.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_list_response import WorkspaceListResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    limit = 20 # int |  (optional) (default to 20)
    search = 'search_example' # str |  (optional)

    try:
        # List Workspaces
        api_response = await api_instance.apps_admin_portal_api_list_workspaces(page=page, limit=limit, search=search)
        print("The response of AdminApi->apps_admin_portal_api_list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_list_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **limit** | **int**|  | [optional] [default to 20]
 **search** | **str**|  | [optional] 

### Return type

[**WorkspaceListResponse**](WorkspaceListResponse.md)

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

# **apps_admin_portal_api_reject_user**
> UserActionResponse apps_admin_portal_api_reject_user(user_id, user_rejection_request)

Reject User

Reject a pending user account.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_action_response import UserActionResponse
from spatialflow_generated.models.user_rejection_request import UserRejectionRequest
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 
    user_rejection_request = spatialflow_generated.UserRejectionRequest() # UserRejectionRequest | 

    try:
        # Reject User
        api_response = await api_instance.apps_admin_portal_api_reject_user(user_id, user_rejection_request)
        print("The response of AdminApi->apps_admin_portal_api_reject_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_reject_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_rejection_request** | [**UserRejectionRequest**](UserRejectionRequest.md)|  | 

### Return type

[**UserActionResponse**](UserActionResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_admin_portal_api_remove_member**
> MemberActionResponse apps_admin_portal_api_remove_member(workspace_id, user_id)

Remove Member

Remove member from workspace.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.member_action_response import MemberActionResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    user_id = 'user_id_example' # str | 

    try:
        # Remove Member
        api_response = await api_instance.apps_admin_portal_api_remove_member(workspace_id, user_id)
        print("The response of AdminApi->apps_admin_portal_api_remove_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_remove_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**MemberActionResponse**](MemberActionResponse.md)

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

# **apps_admin_portal_api_remove_user_workspace**
> UserWorkspaceResponse apps_admin_portal_api_remove_user_workspace(user_id)

Remove User Workspace

Remove user from their workspace.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_workspace_response import UserWorkspaceResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Remove User Workspace
        api_response = await api_instance.apps_admin_portal_api_remove_user_workspace(user_id)
        print("The response of AdminApi->apps_admin_portal_api_remove_user_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_remove_user_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserWorkspaceResponse**](UserWorkspaceResponse.md)

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

# **apps_admin_portal_api_resend_password_reset**
> UserActionResponse apps_admin_portal_api_resend_password_reset(user_id)

Resend Password Reset

Resend password reset email to a user.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_action_response import UserActionResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Resend Password Reset
        api_response = await api_instance.apps_admin_portal_api_resend_password_reset(user_id)
        print("The response of AdminApi->apps_admin_portal_api_resend_password_reset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_resend_password_reset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserActionResponse**](UserActionResponse.md)

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

# **apps_admin_portal_api_resend_verification_email**
> UserActionResponse apps_admin_portal_api_resend_verification_email(user_id)

Resend Verification Email

Resend email verification to a user.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.user_action_response import UserActionResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Resend Verification Email
        api_response = await api_instance.apps_admin_portal_api_resend_verification_email(user_id)
        print("The response of AdminApi->apps_admin_portal_api_resend_verification_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_resend_verification_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserActionResponse**](UserActionResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_admin_portal_api_revoke_invitation**
> Dict[str, object] apps_admin_portal_api_revoke_invitation(invite_id)

Revoke Invitation

Revoke a pending invitation (admin action).

Use case: Stolen/compromised invite link needs to be killed.

Authorization: Global admins (is_superuser or role='admin') can revoke any invitation.
This is by design - admins have full system authority for security incidents.

Args:
    invite_id: UUID of the invitation to revoke

Returns:
    200: Success message
    400: Invitation already used or revoked
    404: Invitation not found

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
    api_instance = spatialflow_generated.AdminApi(api_client)
    invite_id = 'invite_id_example' # str | 

    try:
        # Revoke Invitation
        api_response = await api_instance.apps_admin_portal_api_revoke_invitation(invite_id)
        print("The response of AdminApi->apps_admin_portal_api_revoke_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_revoke_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_admin_portal_api_update_member_role**
> MemberActionResponse apps_admin_portal_api_update_member_role(workspace_id, user_id, update_member_role_request)

Update Member Role

Update workspace member role.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.member_action_response import MemberActionResponse
from spatialflow_generated.models.update_member_role_request import UpdateMemberRoleRequest
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    user_id = 'user_id_example' # str | 
    update_member_role_request = spatialflow_generated.UpdateMemberRoleRequest() # UpdateMemberRoleRequest | 

    try:
        # Update Member Role
        api_response = await api_instance.apps_admin_portal_api_update_member_role(workspace_id, user_id, update_member_role_request)
        print("The response of AdminApi->apps_admin_portal_api_update_member_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_update_member_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **user_id** | **str**|  | 
 **update_member_role_request** | [**UpdateMemberRoleRequest**](UpdateMemberRoleRequest.md)|  | 

### Return type

[**MemberActionResponse**](MemberActionResponse.md)

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

# **apps_admin_portal_api_update_user_workspace**
> UserWorkspaceResponse apps_admin_portal_api_update_user_workspace(user_id, update_user_workspace_request)

Update User Workspace

Update user's workspace (add to workspace or move between workspaces).

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.update_user_workspace_request import UpdateUserWorkspaceRequest
from spatialflow_generated.models.user_workspace_response import UserWorkspaceResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    user_id = 'user_id_example' # str | 
    update_user_workspace_request = spatialflow_generated.UpdateUserWorkspaceRequest() # UpdateUserWorkspaceRequest | 

    try:
        # Update User Workspace
        api_response = await api_instance.apps_admin_portal_api_update_user_workspace(user_id, update_user_workspace_request)
        print("The response of AdminApi->apps_admin_portal_api_update_user_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_update_user_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **update_user_workspace_request** | [**UpdateUserWorkspaceRequest**](UpdateUserWorkspaceRequest.md)|  | 

### Return type

[**UserWorkspaceResponse**](UserWorkspaceResponse.md)

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

# **apps_admin_portal_api_update_workspace**
> WorkspaceUpdateResponse apps_admin_portal_api_update_workspace(workspace_id, workspace_update_request)

Update Workspace

Update workspace details.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_update_request import WorkspaceUpdateRequest
from spatialflow_generated.models.workspace_update_response import WorkspaceUpdateResponse
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
    api_instance = spatialflow_generated.AdminApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    workspace_update_request = spatialflow_generated.WorkspaceUpdateRequest() # WorkspaceUpdateRequest | 

    try:
        # Update Workspace
        api_response = await api_instance.apps_admin_portal_api_update_workspace(workspace_id, workspace_update_request)
        print("The response of AdminApi->apps_admin_portal_api_update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->apps_admin_portal_api_update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **workspace_update_request** | [**WorkspaceUpdateRequest**](WorkspaceUpdateRequest.md)|  | 

### Return type

[**WorkspaceUpdateResponse**](WorkspaceUpdateResponse.md)

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

