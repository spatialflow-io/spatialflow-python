# CreateInvitationIn

Request to create a workspace invitation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | [optional] [default to 'member']

## Example

```python
from spatialflow_generated.models.create_invitation_in import CreateInvitationIn

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvitationIn from a JSON string
create_invitation_in_instance = CreateInvitationIn.from_json(json)
# print the JSON string representation of the object
print(CreateInvitationIn.to_json())

# convert the object into a dict
create_invitation_in_dict = create_invitation_in_instance.to_dict()
# create an instance of CreateInvitationIn from a dict
create_invitation_in_from_dict = CreateInvitationIn.from_dict(create_invitation_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


