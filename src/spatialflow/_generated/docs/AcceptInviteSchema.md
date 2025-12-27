# AcceptInviteSchema

Schema for accepting workspace invitations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**invite_id** | **str** |  | 
**password** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.accept_invite_schema import AcceptInviteSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptInviteSchema from a JSON string
accept_invite_schema_instance = AcceptInviteSchema.from_json(json)
# print the JSON string representation of the object
print(AcceptInviteSchema.to_json())

# convert the object into a dict
accept_invite_schema_dict = accept_invite_schema_instance.to_dict()
# create an instance of AcceptInviteSchema from a dict
accept_invite_schema_from_dict = AcceptInviteSchema.from_dict(accept_invite_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


