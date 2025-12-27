# RevokeAllSessionsOut

Response for revoke all sessions action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**members_affected** | **int** |  | 
**sessions_revoked** | **int** |  | 
**workspace_id** | **str** |  | 

## Example

```python
from spatialflow_generated.models.revoke_all_sessions_out import RevokeAllSessionsOut

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeAllSessionsOut from a JSON string
revoke_all_sessions_out_instance = RevokeAllSessionsOut.from_json(json)
# print the JSON string representation of the object
print(RevokeAllSessionsOut.to_json())

# convert the object into a dict
revoke_all_sessions_out_dict = revoke_all_sessions_out_instance.to_dict()
# create an instance of RevokeAllSessionsOut from a dict
revoke_all_sessions_out_from_dict = RevokeAllSessionsOut.from_dict(revoke_all_sessions_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


