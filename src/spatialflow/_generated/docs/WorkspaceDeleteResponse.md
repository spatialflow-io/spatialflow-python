# WorkspaceDeleteResponse

Response for workspace deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**workspace_id** | **str** |  | 
**workspace_name** | **str** |  | 
**deleted_counts** | **Dict[str, int]** |  | 

## Example

```python
from spatialflow_generated.models.workspace_delete_response import WorkspaceDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceDeleteResponse from a JSON string
workspace_delete_response_instance = WorkspaceDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceDeleteResponse.to_json())

# convert the object into a dict
workspace_delete_response_dict = workspace_delete_response_instance.to_dict()
# create an instance of WorkspaceDeleteResponse from a dict
workspace_delete_response_from_dict = WorkspaceDeleteResponse.from_dict(workspace_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


