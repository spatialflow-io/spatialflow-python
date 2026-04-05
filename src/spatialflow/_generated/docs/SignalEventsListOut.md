# SignalEventsListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signals** | [**List[SignalEventOut]**](SignalEventOut.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.signal_events_list_out import SignalEventsListOut

# TODO update the JSON string below
json = "{}"
# create an instance of SignalEventsListOut from a JSON string
signal_events_list_out_instance = SignalEventsListOut.from_json(json)
# print the JSON string representation of the object
print(SignalEventsListOut.to_json())

# convert the object into a dict
signal_events_list_out_dict = signal_events_list_out_instance.to_dict()
# create an instance of SignalEventsListOut from a dict
signal_events_list_out_from_dict = SignalEventsListOut.from_dict(signal_events_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


