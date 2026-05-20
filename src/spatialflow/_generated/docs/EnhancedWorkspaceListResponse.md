# EnhancedWorkspaceListResponse

Response for enhanced workspace list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[EnhancedWorkspaceListItem]**](EnhancedWorkspaceListItem.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**limit** | **int** |  | 
**pages** | **int** |  | 

## Example

```python
from spatialflow_generated.models.enhanced_workspace_list_response import EnhancedWorkspaceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancedWorkspaceListResponse from a JSON string
enhanced_workspace_list_response_instance = EnhancedWorkspaceListResponse.from_json(json)
# print the JSON string representation of the object
print(EnhancedWorkspaceListResponse.to_json())

# convert the object into a dict
enhanced_workspace_list_response_dict = enhanced_workspace_list_response_instance.to_dict()
# create an instance of EnhancedWorkspaceListResponse from a dict
enhanced_workspace_list_response_from_dict = EnhancedWorkspaceListResponse.from_dict(enhanced_workspace_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


