# spatialflow_generated.WorkspacesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_workspaces_api_cancel_invitation**](WorkspacesApi.md#apps_workspaces_api_cancel_invitation) | **DELETE** /api/v1/workspaces/invitations/{invite_id} | Cancel Invitation
[**apps_workspaces_api_create_invitation**](WorkspacesApi.md#apps_workspaces_api_create_invitation) | **POST** /api/v1/workspaces/invitations | Create Invitation
[**apps_workspaces_api_get_workspace**](WorkspacesApi.md#apps_workspaces_api_get_workspace) | **GET** /api/v1/workspaces/ | Get Workspace
[**apps_workspaces_api_get_workspace_usage**](WorkspacesApi.md#apps_workspaces_api_get_workspace_usage) | **GET** /api/v1/workspaces/usage | Get Workspace Usage
[**apps_workspaces_api_list_invitations**](WorkspacesApi.md#apps_workspaces_api_list_invitations) | **GET** /api/v1/workspaces/invitations | List Invitations
[**apps_workspaces_api_list_workspace_members**](WorkspacesApi.md#apps_workspaces_api_list_workspace_members) | **GET** /api/v1/workspaces/members | List Workspace Members
[**apps_workspaces_api_remove_member**](WorkspacesApi.md#apps_workspaces_api_remove_member) | **DELETE** /api/v1/workspaces/members/{user_id} | Remove Member
[**apps_workspaces_api_resend_invitation**](WorkspacesApi.md#apps_workspaces_api_resend_invitation) | **POST** /api/v1/workspaces/invitations/{invite_id}/resend | Resend Invitation
[**apps_workspaces_api_revoke_all_workspace_sessions**](WorkspacesApi.md#apps_workspaces_api_revoke_all_workspace_sessions) | **POST** /api/v1/workspaces/revoke-all-sessions | Revoke All Workspace Sessions
[**apps_workspaces_api_update_member_role**](WorkspacesApi.md#apps_workspaces_api_update_member_role) | **PATCH** /api/v1/workspaces/members/{user_id} | Update Member Role
[**apps_workspaces_api_update_workspace**](WorkspacesApi.md#apps_workspaces_api_update_workspace) | **PUT** /api/v1/workspaces/ | Update Workspace


# **apps_workspaces_api_cancel_invitation**
> Dict[str, object] apps_workspaces_api_cancel_invitation(invite_id)

Cancel Invitation

Cancel (revoke) a pending invitation (owner-only).

Returns 404 for invitations in other workspaces (tenant isolation).
Returns 400 if already used or already cancelled.

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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    invite_id = 'invite_id_example' # str | 

    try:
        # Cancel Invitation
        api_response = await api_instance.apps_workspaces_api_cancel_invitation(invite_id)
        print("The response of WorkspacesApi->apps_workspaces_api_cancel_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_cancel_invitation: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_create_invitation**
> InvitationOut apps_workspaces_api_create_invitation(create_invitation_in)

Create Invitation

Send an invitation to join the workspace (owner-only).

Creates a new invitation and sends an email to the invitee.
Auto-revokes previous pending invitations for the same email/workspace.

Blocks:
- Self-invites
- Inviting existing workspace members
- Inviting users already in another workspace (stricter than admin flow)

Rate limited to 10 invitations per hour per user (only counted after owner check passes).

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.create_invitation_in import CreateInvitationIn
from spatialflow_generated.models.invitation_out import InvitationOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    create_invitation_in = spatialflow_generated.CreateInvitationIn() # CreateInvitationIn | 

    try:
        # Create Invitation
        api_response = await api_instance.apps_workspaces_api_create_invitation(create_invitation_in)
        print("The response of WorkspacesApi->apps_workspaces_api_create_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_create_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_invitation_in** | [**CreateInvitationIn**](CreateInvitationIn.md)|  | 

### Return type

[**InvitationOut**](InvitationOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_get_workspace**
> WorkspaceOut apps_workspaces_api_get_workspace()

Get Workspace

Get the user's workspace.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_out import WorkspaceOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # Get Workspace
        api_response = await api_instance.apps_workspaces_api_get_workspace()
        print("The response of WorkspacesApi->apps_workspaces_api_get_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_get_workspace: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkspaceOut**](WorkspaceOut.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_get_workspace_usage**
> UsageResponse apps_workspaces_api_get_workspace_usage()

Get Workspace Usage

Get current period usage metrics for billing.

Returns aggregated usage for the current day (midnight to now).
Usage is calculated hourly and includes:
- Location events (DeviceLocation records)
- Action deliveries (successful webhook deliveries)
- Event units (locations + 0.5 * actions)

**Event Units Calculation (PRD §7):**
- 1 location event = 1 event unit
- 1 action delivery = 0.5 event units

**Tier Limits (PRD §7):**
- Developer: 500,000 event units/month
- Pro: 5,000,000 event units/month
- Enterprise: Unlimited

**Example Response:**
```json
{
    "location_events": 10000,
    "action_deliveries": 5000,
    "event_units": 12500,
    "tier": "developer",
    "tier_limit": 500000,
    "period_start": "2025-10-01T00:00:00Z",
    "period_end": "2025-10-01T23:59:59Z"
}
```

PRD Reference: §7 Pricing & Packaging
Roadmap: Phase 2, Task 2.3

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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # Get Workspace Usage
        api_response = await api_instance.apps_workspaces_api_get_workspace_usage()
        print("The response of WorkspacesApi->apps_workspaces_api_get_workspace_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_get_workspace_usage: %s\n" % e)
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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_list_invitations**
> InvitationListResponse apps_workspaces_api_list_invitations()

List Invitations

List pending invitations for the workspace (owner-only).

Returns only pending (not used, not revoked, not expired) invitations.
Capped at 100 results for performance; total reflects actual pending count.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.invitation_list_response import InvitationListResponse
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # List Invitations
        api_response = await api_instance.apps_workspaces_api_list_invitations()
        print("The response of WorkspacesApi->apps_workspaces_api_list_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_list_invitations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InvitationListResponse**](InvitationListResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_list_workspace_members**
> MemberListResponse apps_workspaces_api_list_workspace_members()

List Workspace Members

Get members of the user's workspace.

Returns all members with their roles. Available to all workspace members.
Scoped to requester's workspace only (no cross-workspace access).

Hard cap at 500 members. TODO (#67): Add pagination (page/limit params) for larger lists.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.member_list_response import MemberListResponse
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # List Workspace Members
        api_response = await api_instance.apps_workspaces_api_list_workspace_members()
        print("The response of WorkspacesApi->apps_workspaces_api_list_workspace_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_list_workspace_members: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MemberListResponse**](MemberListResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_remove_member**
> MemberActionOut apps_workspaces_api_remove_member(user_id)

Remove Member

Remove a member from the workspace.

Only workspace owners can remove members. Owners cannot remove themselves
if they are the last owner.

Immediately invalidates all tokens for the removed user (Issue #67).
The user will receive 401 on subsequent requests and must re-authenticate.

Note: This assumes single-workspace-per-user model. On removal, user.workspace
is cleared. If multi-workspace membership is added later, this logic and the
last-owner checks will need to be updated.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.member_action_out import MemberActionOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Remove Member
        api_response = await api_instance.apps_workspaces_api_remove_member(user_id)
        print("The response of WorkspacesApi->apps_workspaces_api_remove_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_remove_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**MemberActionOut**](MemberActionOut.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_resend_invitation**
> InvitationOut apps_workspaces_api_resend_invitation(invite_id)

Resend Invitation

Resend invitation email (owner-only).

Creates a new invitation (new token, new expiry) and revokes the old one.
Only works for pending (non-expired, non-used, non-revoked) invitations.

For expired invitations, create a new invitation instead.
Rate limited to 10 resends per hour per user (only counted after owner check passes).

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.invitation_out import InvitationOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    invite_id = 'invite_id_example' # str | 

    try:
        # Resend Invitation
        api_response = await api_instance.apps_workspaces_api_resend_invitation(invite_id)
        print("The response of WorkspacesApi->apps_workspaces_api_resend_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_resend_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 

### Return type

[**InvitationOut**](InvitationOut.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_revoke_all_workspace_sessions**
> RevokeAllSessionsOut apps_workspaces_api_revoke_all_workspace_sessions()

Revoke All Workspace Sessions

Revoke all sessions for all members of the workspace.

Only workspace owners can perform this action.
All members (including the caller) will need to re-authenticate.
Rate limited to 1 request per minute per workspace.

Use cases:
- Security incident response
- Compliance requirements
- Credential rotation after potential breach

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.revoke_all_sessions_out import RevokeAllSessionsOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # Revoke All Workspace Sessions
        api_response = await api_instance.apps_workspaces_api_revoke_all_workspace_sessions()
        print("The response of WorkspacesApi->apps_workspaces_api_revoke_all_workspace_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_revoke_all_workspace_sessions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RevokeAllSessionsOut**](RevokeAllSessionsOut.md)

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
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_update_member_role**
> MemberActionOut apps_workspaces_api_update_member_role(user_id, update_member_role_in)

Update Member Role

Update a member's role.

Only workspace owners can change roles. Cannot demote the last owner.

On role downgrade (owner -> member), immediately invalidates all tokens
for the affected user (Issue #67). They must re-authenticate to get new
tokens with the updated role.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.member_action_out import MemberActionOut
from spatialflow_generated.models.update_member_role_in import UpdateMemberRoleIn
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    user_id = 'user_id_example' # str | 
    update_member_role_in = spatialflow_generated.UpdateMemberRoleIn() # UpdateMemberRoleIn | 

    try:
        # Update Member Role
        api_response = await api_instance.apps_workspaces_api_update_member_role(user_id, update_member_role_in)
        print("The response of WorkspacesApi->apps_workspaces_api_update_member_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_update_member_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **update_member_role_in** | [**UpdateMemberRoleIn**](UpdateMemberRoleIn.md)|  | 

### Return type

[**MemberActionOut**](MemberActionOut.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_update_workspace**
> WorkspaceOut apps_workspaces_api_update_workspace(workspace_in)

Update Workspace

Update the user's workspace.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_in import WorkspaceIn
from spatialflow_generated.models.workspace_out import WorkspaceOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    workspace_in = spatialflow_generated.WorkspaceIn() # WorkspaceIn | 

    try:
        # Update Workspace
        api_response = await api_instance.apps_workspaces_api_update_workspace(workspace_in)
        print("The response of WorkspacesApi->apps_workspaces_api_update_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_update_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_in** | [**WorkspaceIn**](WorkspaceIn.md)|  | 

### Return type

[**WorkspaceOut**](WorkspaceOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

