# UserInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**workspace_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**role** | **str** |  | [optional] [default to 'member']

## Example

```python
from spatialflow_generated.models.user_invite_request import UserInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserInviteRequest from a JSON string
user_invite_request_instance = UserInviteRequest.from_json(json)
# print the JSON string representation of the object
print(UserInviteRequest.to_json())

# convert the object into a dict
user_invite_request_dict = user_invite_request_instance.to_dict()
# create an instance of UserInviteRequest from a dict
user_invite_request_from_dict = UserInviteRequest.from_dict(user_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


