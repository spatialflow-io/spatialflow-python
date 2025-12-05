# WorkspaceUpdateResponse

Response for workspace update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**workspace_id** | **str** |  | 
**name** | **str** |  | 
**changes** | **Dict[str, object]** |  | 

## Example

```python
from spatialflow_generated.models.workspace_update_response import WorkspaceUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceUpdateResponse from a JSON string
workspace_update_response_instance = WorkspaceUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceUpdateResponse.to_json())

# convert the object into a dict
workspace_update_response_dict = workspace_update_response_instance.to_dict()
# create an instance of WorkspaceUpdateResponse from a dict
workspace_update_response_from_dict = WorkspaceUpdateResponse.from_dict(workspace_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


