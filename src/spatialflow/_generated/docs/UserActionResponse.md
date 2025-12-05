# UserActionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**user_id** | **str** |  | 
**email** | **str** |  | 
**email_verified** | **bool** |  | [optional] 
**admin_approved** | **bool** |  | [optional] 
**admin_approved_at** | **str** |  | [optional] 
**temporary_password** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.user_action_response import UserActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserActionResponse from a JSON string
user_action_response_instance = UserActionResponse.from_json(json)
# print the JSON string representation of the object
print(UserActionResponse.to_json())

# convert the object into a dict
user_action_response_dict = user_action_response_instance.to_dict()
# create an instance of UserActionResponse from a dict
user_action_response_from_dict = UserActionResponse.from_dict(user_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


