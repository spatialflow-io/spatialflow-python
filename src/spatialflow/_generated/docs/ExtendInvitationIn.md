# ExtendInvitationIn

Input schema for PATCH /invitations/{id}.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.extend_invitation_in import ExtendInvitationIn

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendInvitationIn from a JSON string
extend_invitation_in_instance = ExtendInvitationIn.from_json(json)
# print the JSON string representation of the object
print(ExtendInvitationIn.to_json())

# convert the object into a dict
extend_invitation_in_dict = extend_invitation_in_instance.to_dict()
# create an instance of ExtendInvitationIn from a dict
extend_invitation_in_from_dict = ExtendInvitationIn.from_dict(extend_invitation_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


