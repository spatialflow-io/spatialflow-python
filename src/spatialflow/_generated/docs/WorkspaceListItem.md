# WorkspaceListItem

Workspace item for list view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**billing_email** | **str** |  | 
**website** | **str** |  | 
**logo_url** | **str** |  | 
**timezone** | **str** |  | 
**member_count** | **int** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.workspace_list_item import WorkspaceListItem

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceListItem from a JSON string
workspace_list_item_instance = WorkspaceListItem.from_json(json)
# print the JSON string representation of the object
print(WorkspaceListItem.to_json())

# convert the object into a dict
workspace_list_item_dict = workspace_list_item_instance.to_dict()
# create an instance of WorkspaceListItem from a dict
workspace_list_item_from_dict = WorkspaceListItem.from_dict(workspace_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


