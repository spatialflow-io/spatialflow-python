# MemberActionOut

Response for member management actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**user_id** | **str** |  | 
**role** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.member_action_out import MemberActionOut

# TODO update the JSON string below
json = "{}"
# create an instance of MemberActionOut from a JSON string
member_action_out_instance = MemberActionOut.from_json(json)
# print the JSON string representation of the object
print(MemberActionOut.to_json())

# convert the object into a dict
member_action_out_dict = member_action_out_instance.to_dict()
# create an instance of MemberActionOut from a dict
member_action_out_from_dict = MemberActionOut.from_dict(member_action_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


