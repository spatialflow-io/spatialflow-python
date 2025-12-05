# UserInviteResponse

Response schema for user invite endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**user_id** | **str** |  | 
**email** | **str** |  | 
**workspace_id** | **str** |  | 
**workspace_name** | **str** |  | 
**workspace_created** | **bool** |  | 
**role** | **str** |  | 

## Example

```python
from spatialflow_generated.models.user_invite_response import UserInviteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserInviteResponse from a JSON string
user_invite_response_instance = UserInviteResponse.from_json(json)
# print the JSON string representation of the object
print(UserInviteResponse.to_json())

# convert the object into a dict
user_invite_response_dict = user_invite_response_instance.to_dict()
# create an instance of UserInviteResponse from a dict
user_invite_response_from_dict = UserInviteResponse.from_dict(user_invite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


