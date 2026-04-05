# DeviceSessionsOut

Response for listing device sessions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions** | [**List[DeviceSessionOut]**](DeviceSessionOut.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.device_sessions_out import DeviceSessionsOut

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSessionsOut from a JSON string
device_sessions_out_instance = DeviceSessionsOut.from_json(json)
# print the JSON string representation of the object
print(DeviceSessionsOut.to_json())

# convert the object into a dict
device_sessions_out_dict = device_sessions_out_instance.to_dict()
# create an instance of DeviceSessionsOut from a dict
device_sessions_out_from_dict = DeviceSessionsOut.from_dict(device_sessions_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


