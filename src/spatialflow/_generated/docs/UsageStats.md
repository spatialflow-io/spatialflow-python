# UsageStats

Usage statistics for a workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_events** | **int** |  | 
**action_deliveries** | **int** |  | 
**event_units** | **float** |  | 

## Example

```python
from spatialflow_generated.models.usage_stats import UsageStats

# TODO update the JSON string below
json = "{}"
# create an instance of UsageStats from a JSON string
usage_stats_instance = UsageStats.from_json(json)
# print the JSON string representation of the object
print(UsageStats.to_json())

# convert the object into a dict
usage_stats_dict = usage_stats_instance.to_dict()
# create an instance of UsageStats from a dict
usage_stats_from_dict = UsageStats.from_dict(usage_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


