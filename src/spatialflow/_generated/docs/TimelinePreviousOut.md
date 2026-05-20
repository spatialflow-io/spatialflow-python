# TimelinePreviousOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_count** | **int** |  | 
**offline_stale_count** | **int** |  | 
**in_geofence_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.timeline_previous_out import TimelinePreviousOut

# TODO update the JSON string below
json = "{}"
# create an instance of TimelinePreviousOut from a JSON string
timeline_previous_out_instance = TimelinePreviousOut.from_json(json)
# print the JSON string representation of the object
print(TimelinePreviousOut.to_json())

# convert the object into a dict
timeline_previous_out_dict = timeline_previous_out_instance.to_dict()
# create an instance of TimelinePreviousOut from a dict
timeline_previous_out_from_dict = TimelinePreviousOut.from_dict(timeline_previous_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


