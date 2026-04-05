# UpdateDeviceIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**device_type** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.update_device_in import UpdateDeviceIn

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeviceIn from a JSON string
update_device_in_instance = UpdateDeviceIn.from_json(json)
# print the JSON string representation of the object
print(UpdateDeviceIn.to_json())

# convert the object into a dict
update_device_in_dict = update_device_in_instance.to_dict()
# create an instance of UpdateDeviceIn from a dict
update_device_in_from_dict = UpdateDeviceIn.from_dict(update_device_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


