# DormantWorkspaceItem

Workspace with dormancy information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**member_count** | **int** |  | 
**subscription_tier** | **str** |  | [optional] [default to 'free']
**last_activity** | **str** |  | [optional] 
**inactive_days** | **int** |  | 
**created_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.dormant_workspace_item import DormantWorkspaceItem

# TODO update the JSON string below
json = "{}"
# create an instance of DormantWorkspaceItem from a JSON string
dormant_workspace_item_instance = DormantWorkspaceItem.from_json(json)
# print the JSON string representation of the object
print(DormantWorkspaceItem.to_json())

# convert the object into a dict
dormant_workspace_item_dict = dormant_workspace_item_instance.to_dict()
# create an instance of DormantWorkspaceItem from a dict
dormant_workspace_item_from_dict = DormantWorkspaceItem.from_dict(dormant_workspace_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


