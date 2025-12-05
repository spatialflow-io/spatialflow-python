# DeviceIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | 
**name** | **str** |  | 
**device_type** | **str** |  | [optional] [default to 'mobile']
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.device_in import DeviceIn

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceIn from a JSON string
device_in_instance = DeviceIn.from_json(json)
# print the JSON string representation of the object
print(DeviceIn.to_json())

# convert the object into a dict
device_in_dict = device_in_instance.to_dict()
# create an instance of DeviceIn from a dict
device_in_from_dict = DeviceIn.from_dict(device_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


