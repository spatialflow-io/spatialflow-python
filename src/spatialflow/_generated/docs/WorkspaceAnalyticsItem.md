# WorkspaceAnalyticsItem

Single workspace in analytics view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**member_count** | **int** |  | 
**subscription_tier** | **str** |  | [optional] [default to 'free']
**subscription_status** | **str** |  | [optional] [default to 'none']
**location_events** | **int** |  | [optional] [default to 0]
**action_deliveries** | **int** |  | [optional] [default to 0]
**event_units** | **float** |  | [optional] [default to 0.0]
**last_activity** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.workspace_analytics_item import WorkspaceAnalyticsItem

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceAnalyticsItem from a JSON string
workspace_analytics_item_instance = WorkspaceAnalyticsItem.from_json(json)
# print the JSON string representation of the object
print(WorkspaceAnalyticsItem.to_json())

# convert the object into a dict
workspace_analytics_item_dict = workspace_analytics_item_instance.to_dict()
# create an instance of WorkspaceAnalyticsItem from a dict
workspace_analytics_item_from_dict = WorkspaceAnalyticsItem.from_dict(workspace_analytics_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


