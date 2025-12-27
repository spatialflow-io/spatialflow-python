# UpdateMemberRoleIn

Request to update member role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from spatialflow_generated.models.update_member_role_in import UpdateMemberRoleIn

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMemberRoleIn from a JSON string
update_member_role_in_instance = UpdateMemberRoleIn.from_json(json)
# print the JSON string representation of the object
print(UpdateMemberRoleIn.to_json())

# convert the object into a dict
update_member_role_in_dict = update_member_role_in_instance.to_dict()
# create an instance of UpdateMemberRoleIn from a dict
update_member_role_in_from_dict = UpdateMemberRoleIn.from_dict(update_member_role_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


