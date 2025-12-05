# UpdateUserWorkspaceRequest

Request to update user's workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **str** |  | 
**role** | **str** |  | [optional] [default to 'member']

## Example

```python
from spatialflow_generated.models.update_user_workspace_request import UpdateUserWorkspaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserWorkspaceRequest from a JSON string
update_user_workspace_request_instance = UpdateUserWorkspaceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserWorkspaceRequest.to_json())

# convert the object into a dict
update_user_workspace_request_dict = update_user_workspace_request_instance.to_dict()
# create an instance of UpdateUserWorkspaceRequest from a dict
update_user_workspace_request_from_dict = UpdateUserWorkspaceRequest.from_dict(update_user_workspace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


