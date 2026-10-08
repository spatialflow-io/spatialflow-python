# InvitationIssuedOut

Response for the two endpoints that MINT a token: create and resend.  Carries `invite_link` -- byte for byte the same link the invitation email contains -- so the caller who just created the invitation can render it as a QR code for on-site check-in without a second token transport. The token is stored hashed and is unrecoverable afterwards, which is why the listing schema deliberately still omits it: `InvitationOut` never exposes a token, and only the authenticated owner/manager making this very request sees it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**role** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**expires_at** | **datetime** |  | 
**invited_by_email** | **str** |  | [optional] 
**invite_link** | **str** |  | 
**invite_ttl_hours** | **int** |  | 

## Example

```python
from spatialflow_generated.models.invitation_issued_out import InvitationIssuedOut

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationIssuedOut from a JSON string
invitation_issued_out_instance = InvitationIssuedOut.from_json(json)
# print the JSON string representation of the object
print(InvitationIssuedOut.to_json())

# convert the object into a dict
invitation_issued_out_dict = invitation_issued_out_instance.to_dict()
# create an instance of InvitationIssuedOut from a dict
invitation_issued_out_from_dict = InvitationIssuedOut.from_dict(invitation_issued_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


