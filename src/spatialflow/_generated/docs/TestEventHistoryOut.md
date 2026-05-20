# TestEventHistoryOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geofence_id** | **str** |  | 
**geofence_name** | **str** |  | 
**test_events** | [**List[TestEventItemOut]**](TestEventItemOut.md) |  | 
**count** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from spatialflow_generated.models.test_event_history_out import TestEventHistoryOut

# TODO update the JSON string below
json = "{}"
# create an instance of TestEventHistoryOut from a JSON string
test_event_history_out_instance = TestEventHistoryOut.from_json(json)
# print the JSON string representation of the object
print(TestEventHistoryOut.to_json())

# convert the object into a dict
test_event_history_out_dict = test_event_history_out_instance.to_dict()
# create an instance of TestEventHistoryOut from a dict
test_event_history_out_from_dict = TestEventHistoryOut.from_dict(test_event_history_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


