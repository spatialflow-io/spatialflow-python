# DeviceOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**device_id** | **str** |  | 
**name** | **str** |  | 
**device_type** | **str** |  | 
**is_active** | **bool** |  | 
**last_location** | **Dict[str, object]** |  | [optional] 
**last_location_time** | **datetime** |  | [optional] 
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


