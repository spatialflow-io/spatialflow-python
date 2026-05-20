# EnhancedWorkspaceListItem

Workspace item with subscription and usage data.

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
**subscription_tier** | **str** |  | [optional] [default to 'free']
**subscription_status** | **str** |  | [optional] [default to 'none']
**usage_this_month** | **float** |  | [optional] [default to 0.0]
**last_activity** | **str** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.enhanced_workspace_list_item import EnhancedWorkspaceListItem

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancedWorkspaceListItem from a JSON string
enhanced_workspace_list_item_instance = EnhancedWorkspaceListItem.from_json(json)
# print the JSON string representation of the object
print(EnhancedWorkspaceListItem.to_json())

# convert the object into a dict
enhanced_workspace_list_item_dict = enhanced_workspace_list_item_instance.to_dict()
# create an instance of EnhancedWorkspaceListItem from a dict
enhanced_workspace_list_item_from_dict = EnhancedWorkspaceListItem.from_dict(enhanced_workspace_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


