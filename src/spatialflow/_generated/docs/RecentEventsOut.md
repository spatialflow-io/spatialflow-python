# RecentEventsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GeofenceEventOut]**](GeofenceEventOut.md) |  | 
**total_count** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from spatialflow_generated.models.recent_events_out import RecentEventsOut

# TODO update the JSON string below
json = "{}"
# create an instance of RecentEventsOut from a JSON string
recent_events_out_instance = RecentEventsOut.from_json(json)
# print the JSON string representation of the object
print(RecentEventsOut.to_json())

# convert the object into a dict
recent_events_out_dict = recent_events_out_instance.to_dict()
# create an instance of RecentEventsOut from a dict
recent_events_out_from_dict = RecentEventsOut.from_dict(recent_events_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


