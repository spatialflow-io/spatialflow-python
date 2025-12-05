# WorkspaceListResponse

Response for list of workspaces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[WorkspaceListItem]**](WorkspaceListItem.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**limit** | **int** |  | 
**pages** | **int** |  | 

## Example

```python
from spatialflow_generated.models.workspace_list_response import WorkspaceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceListResponse from a JSON string
workspace_list_response_instance = WorkspaceListResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceListResponse.to_json())

# convert the object into a dict
workspace_list_response_dict = workspace_list_response_instance.to_dict()
# create an instance of WorkspaceListResponse from a dict
workspace_list_response_from_dict = WorkspaceListResponse.from_dict(workspace_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


