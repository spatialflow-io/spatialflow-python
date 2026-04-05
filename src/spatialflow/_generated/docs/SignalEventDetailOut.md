# SignalEventDetailOut


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
**reason_codes** | **List[object]** |  | [optional] [default to []]
**explanation** | **Dict[str, object]** |  | [optional] 
**contributing_locations** | [**List[ContributingLocationOut]**](ContributingLocationOut.md) |  | [optional] [default to []]
**geofence_geometry** | [**GeofenceGeometryOut**](GeofenceGeometryOut.md) |  | [optional] 

## Example

```python
from spatialflow_generated.models.signal_event_detail_out import SignalEventDetailOut

# TODO update the JSON string below
json = "{}"
# create an instance of SignalEventDetailOut from a JSON string
signal_event_detail_out_instance = SignalEventDetailOut.from_json(json)
# print the JSON string representation of the object
print(SignalEventDetailOut.to_json())

# convert the object into a dict
signal_event_detail_out_dict = signal_event_detail_out_instance.to_dict()
# create an instance of SignalEventDetailOut from a dict
signal_event_detail_out_from_dict = SignalEventDetailOut.from_dict(signal_event_detail_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


