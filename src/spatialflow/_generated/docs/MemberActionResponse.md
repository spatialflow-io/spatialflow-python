# MemberActionResponse

Response for member management actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**user_id** | **str** |  | 
**workspace_id** | **str** |  | 
**new_role** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.member_action_response import MemberActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberActionResponse from a JSON string
member_action_response_instance = MemberActionResponse.from_json(json)
# print the JSON string representation of the object
print(MemberActionResponse.to_json())

# convert the object into a dict
member_action_response_dict = member_action_response_instance.to_dict()
# create an instance of MemberActionResponse from a dict
member_action_response_from_dict = MemberActionResponse.from_dict(member_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


