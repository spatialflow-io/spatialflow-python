# UserWorkspaceResponse

Response for user workspace management actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**user_id** | **str** |  | 
**workspace_id** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**previous_workspace_name** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.user_workspace_response import UserWorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserWorkspaceResponse from a JSON string
user_workspace_response_instance = UserWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(UserWorkspaceResponse.to_json())

# convert the object into a dict
user_workspace_response_dict = user_workspace_response_instance.to_dict()
# create an instance of UserWorkspaceResponse from a dict
user_workspace_response_from_dict = UserWorkspaceResponse.from_dict(user_workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


