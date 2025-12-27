# InvitationListResponse

Response for workspace invitations list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitations** | [**List[InvitationOut]**](InvitationOut.md) |  | 
**total** | **int** |  | 

## Example

```python
from spatialflow_generated.models.invitation_list_response import InvitationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationListResponse from a JSON string
invitation_list_response_instance = InvitationListResponse.from_json(json)
# print the JSON string representation of the object
print(InvitationListResponse.to_json())

# convert the object into a dict
invitation_list_response_dict = invitation_list_response_instance.to_dict()
# create an instance of InvitationListResponse from a dict
invitation_list_response_from_dict = InvitationListResponse.from_dict(invitation_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


