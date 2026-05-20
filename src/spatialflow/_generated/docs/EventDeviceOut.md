# EventDeviceOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**device_id** | **str** |  | 
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from spatialflow_generated.models.event_device_out import EventDeviceOut

# TODO update the JSON string below
json = "{}"
# create an instance of EventDeviceOut from a JSON string
event_device_out_instance = EventDeviceOut.from_json(json)
# print the JSON string representation of the object
print(EventDeviceOut.to_json())

# convert the object into a dict
event_device_out_dict = event_device_out_instance.to_dict()
# create an instance of EventDeviceOut from a dict
event_device_out_from_dict = EventDeviceOut.from_dict(event_device_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


