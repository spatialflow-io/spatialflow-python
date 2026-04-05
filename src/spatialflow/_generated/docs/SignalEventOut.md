# SignalEventOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**device_id** | **str** |  | 
**device_name** | **str** |  | 
**signal_type** | **str** |  | 
**state** | **str** |  | 
**started_at** | **datetime** |  | 
**confirmed_at** | **datetime** |  | [optional] 
**ended_at** | **datetime** |  | [optional] 
**geofence_id** | **str** |  | [optional] 
**geofence_name** | **str** |  | [optional] 
**has_explanation** | **bool** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.signal_event_out import SignalEventOut

# TODO update the JSON string below
json = "{}"
# create an instance of SignalEventOut from a JSON string
signal_event_out_instance = SignalEventOut.from_json(json)
# print the JSON string representation of the object
print(SignalEventOut.to_json())

# convert the object into a dict
signal_event_out_dict = signal_event_out_instance.to_dict()
# create an instance of SignalEventOut from a dict
signal_event_out_from_dict = SignalEventOut.from_dict(signal_event_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


