# AcceptInvitePasswordlessSchema

Schema for accepting an invitation without setting a password.  `invite_id` is a body field, not a path parameter, on purpose: rate_limit_dual reads identifier_field off the Ninja schema positional argument, so per-invite limiting only works when the id is in the body. The token is in the body for the same reason it is on /accept-invite: query strings end up in access logs, referrers and browser history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**invite_id** | **str** |  | 

## Example

```python
from spatialflow_generated.models.accept_invite_passwordless_schema import AcceptInvitePasswordlessSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptInvitePasswordlessSchema from a JSON string
accept_invite_passwordless_schema_instance = AcceptInvitePasswordlessSchema.from_json(json)
# print the JSON string representation of the object
print(AcceptInvitePasswordlessSchema.to_json())

# convert the object into a dict
accept_invite_passwordless_schema_dict = accept_invite_passwordless_schema_instance.to_dict()
# create an instance of AcceptInvitePasswordlessSchema from a dict
accept_invite_passwordless_schema_from_dict = AcceptInvitePasswordlessSchema.from_dict(accept_invite_passwordless_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


