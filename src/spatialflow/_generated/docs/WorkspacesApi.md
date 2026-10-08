# spatialflow_generated.WorkspacesApi

All URIs are relative to *https://api.spatialflow.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_workspaces_api_accept_mobile_tracking_consent**](WorkspacesApi.md#apps_workspaces_api_accept_mobile_tracking_consent) | **POST** /api/v1/workspaces/mobile/tracking-consent | Accept Mobile Tracking Consent
[**apps_workspaces_api_available_web_workspaces**](WorkspacesApi.md#apps_workspaces_api_available_web_workspaces) | **GET** /api/v1/workspaces/available | Available Web Workspaces
[**apps_workspaces_api_cancel_invitation**](WorkspacesApi.md#apps_workspaces_api_cancel_invitation) | **DELETE** /api/v1/workspaces/invitations/{invite_id} | Cancel Invitation
[**apps_workspaces_api_create_invitation**](WorkspacesApi.md#apps_workspaces_api_create_invitation) | **POST** /api/v1/workspaces/invitations | Create Invitation
[**apps_workspaces_api_delete_example_data**](WorkspacesApi.md#apps_workspaces_api_delete_example_data) | **DELETE** /api/v1/workspaces/example-data | Remove all example/starter content from the workspace
[**apps_workspaces_api_delete_saml_config**](WorkspacesApi.md#apps_workspaces_api_delete_saml_config) | **DELETE** /api/v1/workspaces/saml-config | Delete Saml Config
[**apps_workspaces_api_extend_invitation**](WorkspacesApi.md#apps_workspaces_api_extend_invitation) | **PATCH** /api/v1/workspaces/invitations/{invite_id} | Extend Invitation
[**apps_workspaces_api_get_saml_config**](WorkspacesApi.md#apps_workspaces_api_get_saml_config) | **GET** /api/v1/workspaces/saml-config | Get Saml Config
[**apps_workspaces_api_get_workspace**](WorkspacesApi.md#apps_workspaces_api_get_workspace) | **GET** /api/v1/workspaces/ | Get Workspace
[**apps_workspaces_api_get_workspace_usage**](WorkspacesApi.md#apps_workspaces_api_get_workspace_usage) | **GET** /api/v1/workspaces/usage | Get Workspace Usage
[**apps_workspaces_api_list_invitations**](WorkspacesApi.md#apps_workspaces_api_list_invitations) | **GET** /api/v1/workspaces/invitations | List Invitations
[**apps_workspaces_api_list_workspace_members**](WorkspacesApi.md#apps_workspaces_api_list_workspace_members) | **GET** /api/v1/workspaces/members | List Workspace Members
[**apps_workspaces_api_mobile_workspace_bootstrap**](WorkspacesApi.md#apps_workspaces_api_mobile_workspace_bootstrap) | **GET** /api/v1/workspaces/mobile/bootstrap | Mobile Workspace Bootstrap
[**apps_workspaces_api_patch_workspace**](WorkspacesApi.md#apps_workspaces_api_patch_workspace) | **PATCH** /api/v1/workspaces/ | Patch Workspace
[**apps_workspaces_api_remove_member**](WorkspacesApi.md#apps_workspaces_api_remove_member) | **DELETE** /api/v1/workspaces/members/{user_id} | Remove Member
[**apps_workspaces_api_resend_invitation**](WorkspacesApi.md#apps_workspaces_api_resend_invitation) | **POST** /api/v1/workspaces/invitations/{invite_id}/resend | Resend Invitation
[**apps_workspaces_api_resend_missing_invitations**](WorkspacesApi.md#apps_workspaces_api_resend_missing_invitations) | **POST** /api/v1/workspaces/invitations/resend-missing | Resend Missing Invitations
[**apps_workspaces_api_revoke_all_workspace_sessions**](WorkspacesApi.md#apps_workspaces_api_revoke_all_workspace_sessions) | **POST** /api/v1/workspaces/revoke-all-sessions | Revoke All Workspace Sessions
[**apps_workspaces_api_select_mobile_workspace**](WorkspacesApi.md#apps_workspaces_api_select_mobile_workspace) | **POST** /api/v1/workspaces/mobile/select | Select Mobile Workspace
[**apps_workspaces_api_select_web_workspace**](WorkspacesApi.md#apps_workspaces_api_select_web_workspace) | **POST** /api/v1/workspaces/select | Select Web Workspace
[**apps_workspaces_api_update_member_role**](WorkspacesApi.md#apps_workspaces_api_update_member_role) | **PATCH** /api/v1/workspaces/members/{user_id} | Update Member Role
[**apps_workspaces_api_update_workspace**](WorkspacesApi.md#apps_workspaces_api_update_workspace) | **PUT** /api/v1/workspaces/ | Update Workspace
[**apps_workspaces_api_upsert_saml_config**](WorkspacesApi.md#apps_workspaces_api_upsert_saml_config) | **PUT** /api/v1/workspaces/saml-config | Upsert Saml Config


# **apps_workspaces_api_accept_mobile_tracking_consent**
> MobileTrackingConsentOut apps_workspaces_api_accept_mobile_tracking_consent(mobile_tracking_consent_in)

Accept Mobile Tracking Consent

Record the selected member's explicit acknowledgement before tracking starts.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.mobile_tracking_consent_in import MobileTrackingConsentIn
from spatialflow_generated.models.mobile_tracking_consent_out import MobileTrackingConsentOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    mobile_tracking_consent_in = spatialflow_generated.MobileTrackingConsentIn() # MobileTrackingConsentIn | 

    try:
        # Accept Mobile Tracking Consent
        api_response = await api_instance.apps_workspaces_api_accept_mobile_tracking_consent(mobile_tracking_consent_in)
        print("The response of WorkspacesApi->apps_workspaces_api_accept_mobile_tracking_consent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_accept_mobile_tracking_consent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_tracking_consent_in** | [**MobileTrackingConsentIn**](MobileTrackingConsentIn.md)|  | 

### Return type

[**MobileTrackingConsentOut**](MobileTrackingConsentOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_available_web_workspaces**
> MobileWorkspaceBootstrapOut apps_workspaces_api_available_web_workspaces()

Available Web Workspaces

Return every workspace the signed-in web user may switch to.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.mobile_workspace_bootstrap_out import MobileWorkspaceBootstrapOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # Available Web Workspaces
        api_response = await api_instance.apps_workspaces_api_available_web_workspaces()
        print("The response of WorkspacesApi->apps_workspaces_api_available_web_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_available_web_workspaces: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MobileWorkspaceBootstrapOut**](MobileWorkspaceBootstrapOut.md)

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_cancel_invitation**
> Dict[str, object] apps_workspaces_api_cancel_invitation(invite_id)

Cancel Invitation

Cancel (revoke) a pending invitation.  Available to owners and managers. Returns 404 for invitations in other workspaces (tenant isolation). Returns 400 if already used or already cancelled.

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_create_invitation**
> InvitationIssuedOut apps_workspaces_api_create_invitation(create_invitation_in)

Create Invitation

Send an invitation to join the workspace.  Role-based invitation rules: - Owners: Can invite to any role - Managers: Can invite to manager, field_worker, or member (NOT owner) - Field workers/members: Cannot invite  Creates a new invitation and sends an email to the invitee. Auto-revokes previous pending invitations for the same email/workspace.  Blocks: - Self-invites - Inviting existing workspace members  Does NOT block inviting a user who already belongs to a different workspace -- every self-signup gets a personal workspace, so an account already having one is the common case, not a special one. Acceptance (apps/authentication/api.py accept_invitation) moves that account's primary workspace to the inviter's and creates the membership.  Rate limited to 100 invitations per hour per user (only counted after permission check passes) — sized for the bulk-invite modal's one-request-per-address flow.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.create_invitation_in import CreateInvitationIn
from spatialflow_generated.models.invitation_issued_out import InvitationIssuedOut
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

[**InvitationIssuedOut**](InvitationIssuedOut.md)

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_delete_example_data**
> Dict[str, object] apps_workspaces_api_delete_example_data()

Remove all example/starter content from the workspace

Remove all is_example=True rows (geofences, devices, workflows) from the caller's workspace.  Only owners and managers can remove example data. Idempotent — calling again when no example rows remain still returns 200.  Returns:     200: {\"removed\": {\"workflows\": N, \"devices\": N, \"geofences\": N}}     403: if the caller is not an owner or manager     404: if the caller has no workspace

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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # Remove all example/starter content from the workspace
        api_response = await api_instance.apps_workspaces_api_delete_example_data()
        print("The response of WorkspacesApi->apps_workspaces_api_delete_example_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_delete_example_data: %s\n" % e)
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
**409** | Conflict |  -  |
**503** | Service Unavailable |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_delete_saml_config**
> Dict[str, object] apps_workspaces_api_delete_saml_config()

Delete Saml Config

Delete the SAML SSO configuration for the workspace.  Only workspace owners can manage SSO configuration. Returns 404 if no configuration exists.

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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # Delete Saml Config
        api_response = await api_instance.apps_workspaces_api_delete_saml_config()
        print("The response of WorkspacesApi->apps_workspaces_api_delete_saml_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_delete_saml_config: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_extend_invitation**
> InvitationOut apps_workspaces_api_extend_invitation(invite_id, extend_invitation_in)

Extend Invitation

Extend the expiry of a pending invitation.  Available to owners and managers. Permits extending an already-expired invitation (recovery path) but blocks extending a used or revoked one. The original invitation token is preserved — no new email is sent; the recipient's existing email link will continue to work until the new expires_at. Validates expires_at strictly in the future and at most 90 days from now. Atomic with select_for_update to prevent race conditions with concurrent revoke.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.extend_invitation_in import ExtendInvitationIn
from spatialflow_generated.models.invitation_out import InvitationOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    invite_id = 'invite_id_example' # str | 
    extend_invitation_in = spatialflow_generated.ExtendInvitationIn() # ExtendInvitationIn | 

    try:
        # Extend Invitation
        api_response = await api_instance.apps_workspaces_api_extend_invitation(invite_id, extend_invitation_in)
        print("The response of WorkspacesApi->apps_workspaces_api_extend_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_extend_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 
 **extend_invitation_in** | [**ExtendInvitationIn**](ExtendInvitationIn.md)|  | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_get_saml_config**
> SAMLConfigOut apps_workspaces_api_get_saml_config()

Get Saml Config

Get the SAML SSO configuration for the workspace.  Only workspace owners can view SSO configuration. Returns 404 if no configuration exists.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.saml_config_out import SAMLConfigOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # Get Saml Config
        api_response = await api_instance.apps_workspaces_api_get_saml_config()
        print("The response of WorkspacesApi->apps_workspaces_api_get_saml_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_get_saml_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SAMLConfigOut**](SAMLConfigOut.md)

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_get_workspace_usage**
> UsageResponse apps_workspaces_api_get_workspace_usage()

Get Workspace Usage

Get current period usage metrics for billing.  Returns aggregated usage for the current day (midnight to now). Usage is calculated hourly and includes: - Location events (DeviceLocation records) - Action deliveries (successful webhook deliveries) - Event units (locations + 0.5 * actions)  **Event Units Calculation:** - 1 location event = 1 event unit - 1 action delivery = 0.5 event units  **Tier & limit** are derived from the workspace's active subscription plan (free / pro / team / business / enterprise). ``tier_limit`` is the plan's monthly event allowance (``null`` = unlimited).  **Example Response:** ```json {     \"location_events\": 10000,     \"action_deliveries\": 5000,     \"event_units\": 12500,     \"tier\": \"developer\",     \"tier_limit\": 500000,     \"period_start\": \"2025-10-01T00:00:00Z\",     \"period_end\": \"2025-10-01T23:59:59Z\" } ```

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.usage_response import UsageResponse
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_list_invitations**
> InvitationListResponse apps_workspaces_api_list_invitations(limit=limit, offset=offset, before=before)

List Invitations

List pending invitations for the workspace.  Available to owners and managers. Returns only pending (not used, not revoked, not expired) invitations.  One page is capped at 100 rows for performance; `total` is always the true pending count. Defaults are unchanged from the single-page behaviour: first 100, newest first.  A caller that needs every row (the print sheet does) pages with `before` rather than `offset`. `before` is a keyset cursor, `\"<created_at ISO>,<id>\"` -- echoed back as `next_cursor` -- and returns the rows strictly after it in the `(-created_at, id)` order. Offsets drift when rows are accepted, revoked or created mid-walk: a deletion behind the cursor shifts every later row one place forward and the next `offset` page silently skips one. A cursor names a position in the ordering, not a count, so it cannot skip.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.invitation_list_response import InvitationListResponse
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    before = 'before_example' # str |  (optional)

    try:
        # List Invitations
        api_response = await api_instance.apps_workspaces_api_list_invitations(limit=limit, offset=offset, before=before)
        print("The response of WorkspacesApi->apps_workspaces_api_list_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_list_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **before** | **str**|  | [optional] 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_list_workspace_members**
> MemberListResponse apps_workspaces_api_list_workspace_members()

List Workspace Members

Get members of the user's workspace.  Returns all members with their roles. Available to all workspace members. Scoped to requester's workspace only (no cross-workspace access).  Hard cap at 500 members; pagination is not yet available for larger lists.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.member_list_response import MemberListResponse
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_mobile_workspace_bootstrap**
> MobileWorkspaceBootstrapOut apps_workspaces_api_mobile_workspace_bootstrap()

Mobile Workspace Bootstrap

Return mobile workspace-picker state for signed-in mobile tracking users.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.mobile_workspace_bootstrap_out import MobileWorkspaceBootstrapOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)

    try:
        # Mobile Workspace Bootstrap
        api_response = await api_instance.apps_workspaces_api_mobile_workspace_bootstrap()
        print("The response of WorkspacesApi->apps_workspaces_api_mobile_workspace_bootstrap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_mobile_workspace_bootstrap: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MobileWorkspaceBootstrapOut**](MobileWorkspaceBootstrapOut.md)

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_patch_workspace**
> WorkspaceOut apps_workspaces_api_patch_workspace(workspace_patch_in)

Patch Workspace

Partially update the user's workspace (e.g. the map home area).  Same permissions as the PUT: owners and managers only.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_out import WorkspaceOut
from spatialflow_generated.models.workspace_patch_in import WorkspacePatchIn
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    workspace_patch_in = spatialflow_generated.WorkspacePatchIn() # WorkspacePatchIn | 

    try:
        # Patch Workspace
        api_response = await api_instance.apps_workspaces_api_patch_workspace(workspace_patch_in)
        print("The response of WorkspacesApi->apps_workspaces_api_patch_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_patch_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_patch_in** | [**WorkspacePatchIn**](WorkspacePatchIn.md)|  | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_remove_member**
> apps_workspaces_api_remove_member(user_id)

Remove Member

Remove a member from the workspace.  Role-based removal rules: - Owners: Can remove any member (including other owners, except last) - Managers: Can remove field_workers and members (NOT owners or managers) - Field workers/members: Cannot remove anyone  Immediately invalidates all tokens for the removed user. The user will receive 401 on subsequent requests and must re-authenticate.  Note: This assumes single-workspace-per-user model. On removal, user.workspace is cleared. If multi-workspace membership is added later, this logic and the last-owner checks will need to be updated.

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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Remove Member
        await api_instance.apps_workspaces_api_remove_member(user_id)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_remove_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

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
**204** | No Content |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_resend_invitation**
> InvitationIssuedOut apps_workspaces_api_resend_invitation(invite_id)

Resend Invitation

Resend invitation email.  Available to owners and managers. Creates a new invitation (new token, new expiry) and revokes the old one. Only works for pending (non-expired, non-used, non-revoked) invitations.  For expired invitations, create a new invitation instead. Rate limited to 10 resends per hour per user (only counted after permission check passes).  A crew sheet of pending invitations should use POST /invitations/resend-missing instead: it reissues many invitations in one call against its own rate-limit budget, rather than this endpoint's per- invitation limit.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.invitation_issued_out import InvitationIssuedOut
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

[**InvitationIssuedOut**](InvitationIssuedOut.md)

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
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_resend_missing_invitations**
> BatchResendOut apps_workspaces_api_resend_missing_invitations(batch_resend_in)

Resend Missing Invitations

Reissue many invitations in a single call.  Available to owners and managers. For each invitation named by `invitation_ids` -- or, if omitted, the next pending page in the workspace keyset walk -- this reissues it exactly as POST /invitations/{id}/resend does (same `_validate_resend` / `_execute_resend` helpers: same token regeneration, same email, same audit entry, same owner-invitation restriction). A row a manager may not touch, or one that stopped being pending, is skipped and reported rather than failing the call.  A print sheet checking in a hundred-person crew needs every pending invitation reissued in bounded pages: the single endpoint is rate limited to 10 resends per hour per user, which would take ten passes an hour apart for a sheet that size. This endpoint counts as ONE call against its own budget (also 10 per hour per user) regardless of how many invitations it reissues -- charged once every row has been classified with `_validate_resend` and at least one is actually executable, so a batch that turns out to be entirely unknown ids or owner invitations a manager may not touch costs nothing. Capped at MAX_BATCH_RESEND invitations per call. When `invitation_ids` is omitted, a capped response returns a keyset `next_cursor` and the pending `remaining_count`; supplying that cursor on the next call excludes replacements created by earlier pages, so old invitations cannot be starved by their newer replacements.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.batch_resend_in import BatchResendIn
from spatialflow_generated.models.batch_resend_out import BatchResendOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    batch_resend_in = spatialflow_generated.BatchResendIn() # BatchResendIn | 

    try:
        # Resend Missing Invitations
        api_response = await api_instance.apps_workspaces_api_resend_missing_invitations(batch_resend_in)
        print("The response of WorkspacesApi->apps_workspaces_api_resend_missing_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_resend_missing_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_resend_in** | [**BatchResendIn**](BatchResendIn.md)|  | 

### Return type

[**BatchResendOut**](BatchResendOut.md)

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
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_revoke_all_workspace_sessions**
> RevokeAllSessionsOut apps_workspaces_api_revoke_all_workspace_sessions()

Revoke All Workspace Sessions

Revoke all sessions for all members of the workspace.  Only workspace owners can perform this action. All members (including the caller) will need to re-authenticate. Rate limited to 1 request per minute per workspace.  Use cases: - Security incident response - Compliance requirements - Credential rotation after potential breach

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.revoke_all_sessions_out import RevokeAllSessionsOut
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_select_mobile_workspace**
> MobileWorkspaceSelectionOut apps_workspaces_api_select_mobile_workspace(mobile_workspace_select_in)

Select Mobile Workspace

Set or confirm the selected mobile workspace and return fresh tokens.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.mobile_workspace_select_in import MobileWorkspaceSelectIn
from spatialflow_generated.models.mobile_workspace_selection_out import MobileWorkspaceSelectionOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    mobile_workspace_select_in = spatialflow_generated.MobileWorkspaceSelectIn() # MobileWorkspaceSelectIn | 

    try:
        # Select Mobile Workspace
        api_response = await api_instance.apps_workspaces_api_select_mobile_workspace(mobile_workspace_select_in)
        print("The response of WorkspacesApi->apps_workspaces_api_select_mobile_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_select_mobile_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_workspace_select_in** | [**MobileWorkspaceSelectIn**](MobileWorkspaceSelectIn.md)|  | 

### Return type

[**MobileWorkspaceSelectionOut**](MobileWorkspaceSelectionOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_select_web_workspace**
> MobileWorkspaceSelectionOut apps_workspaces_api_select_web_workspace(mobile_workspace_select_in)

Select Web Workspace

Switch the web session to one of the user's memberships.  Fresh workspace-bound tokens are returned for the in-memory web client and also replace both HttpOnly auth cookies. The membership lookup is the authorization boundary; a caller cannot select an arbitrary workspace.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.mobile_workspace_select_in import MobileWorkspaceSelectIn
from spatialflow_generated.models.mobile_workspace_selection_out import MobileWorkspaceSelectionOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    mobile_workspace_select_in = spatialflow_generated.MobileWorkspaceSelectIn() # MobileWorkspaceSelectIn | 

    try:
        # Select Web Workspace
        api_response = await api_instance.apps_workspaces_api_select_web_workspace(mobile_workspace_select_in)
        print("The response of WorkspacesApi->apps_workspaces_api_select_web_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_select_web_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_workspace_select_in** | [**MobileWorkspaceSelectIn**](MobileWorkspaceSelectIn.md)|  | 

### Return type

[**MobileWorkspaceSelectionOut**](MobileWorkspaceSelectionOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_update_member_role**
> MemberActionOut apps_workspaces_api_update_member_role(user_id, update_member_role_in)

Update Member Role

Update a member's role.  Role management rules: - Owners: Can change any role (including promoting to owner) - Managers: Can change to manager, field_worker, or member (NOT owner) - Field workers/members: Cannot change roles  Cannot demote the last owner.  On any permission downgrade, immediately invalidates all tokens for the affected user. They must re-authenticate to get new tokens with the updated role.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.member_action_out import MemberActionOut
from spatialflow_generated.models.update_member_role_in import UpdateMemberRoleIn
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
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_update_workspace**
> WorkspaceOut apps_workspaces_api_update_workspace(workspace_in)

Update Workspace

Update the user's workspace. Only owners and managers can update.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.workspace_in import WorkspaceIn
from spatialflow_generated.models.workspace_out import WorkspaceOut
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_workspaces_api_upsert_saml_config**
> SAMLConfigOut apps_workspaces_api_upsert_saml_config(saml_config_in)

Upsert Saml Config

Create or update the SAML SSO configuration for the workspace.  Only workspace owners can manage SSO configuration. Validates PEM certificate format and domain uniqueness.

### Example

* Bearer Authentication (JWTBearer):

```python
import spatialflow_generated
from spatialflow_generated.models.saml_config_in import SAMLConfigIn
from spatialflow_generated.models.saml_config_out import SAMLConfigOut
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
    api_instance = spatialflow_generated.WorkspacesApi(api_client)
    saml_config_in = spatialflow_generated.SAMLConfigIn() # SAMLConfigIn | 

    try:
        # Upsert Saml Config
        api_response = await api_instance.apps_workspaces_api_upsert_saml_config(saml_config_in)
        print("The response of WorkspacesApi->apps_workspaces_api_upsert_saml_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspacesApi->apps_workspaces_api_upsert_saml_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_config_in** | [**SAMLConfigIn**](SAMLConfigIn.md)|  | 

### Return type

[**SAMLConfigOut**](SAMLConfigOut.md)

### Authorization

[JWTBearer](../README.md#JWTBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

