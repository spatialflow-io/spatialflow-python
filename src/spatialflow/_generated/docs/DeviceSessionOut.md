# DeviceSessionOut

Response schema for a completed tracking session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**started_at** | **datetime** |  | 
**ended_at** | **datetime** |  | 
**duration_seconds** | **int** |  | 
**location_count** | **int** |  | 
**distance_meters** | **float** |  | [optional] 
**notes** | **str** |  | 
**has_track_geometry** | **bool** |  | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.device_session_out import DeviceSessionOut

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSessionOut from a JSON string
device_session_out_instance = DeviceSessionOut.from_json(json)
# print the JSON string representation of the object
print(DeviceSessionOut.to_json())

# convert the object into a dict
device_session_out_dict = device_session_out_instance.to_dict()
# create an instance of DeviceSessionOut from a dict
device_session_out_from_dict = DeviceSessionOut.from_dict(device_session_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


