# DeviceOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**device_id** | **str** |  | 
**name** | **str** |  | 
**device_type** | **str** |  | 
**is_active** | **bool** |  | 
**shift_status** | **str** |  | 
**shift_started_at** | **datetime** |  | [optional] 
**shift_paused_at** | **datetime** |  | [optional] 
**shift_ended_at** | **datetime** |  | [optional] 
**shift_resumed_at** | **datetime** |  | [optional] 
**last_location** | [**LatLonOut**](LatLonOut.md) |  | [optional] 
**last_location_time** | **datetime** |  | [optional] 
**last_heading** | **float** |  | [optional] 
**current_session_notes** | **str** |  | [optional] [default to '']
**in_geofence_ids** | **List[str]** |  | [optional] [default to []]
**in_geofence_entries** | **Dict[str, str]** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.device_out import DeviceOut

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceOut from a JSON string
device_out_instance = DeviceOut.from_json(json)
# print the JSON string representation of the object
print(DeviceOut.to_json())

# convert the object into a dict
device_out_dict = device_out_instance.to_dict()
# create an instance of DeviceOut from a dict
device_out_from_dict = DeviceOut.from_dict(device_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


