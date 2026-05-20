# DeviceStatsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_devices** | **int** |  | 
**active_devices** | **int** |  | 
**inactive_devices** | **int** |  | 
**events_today** | **int** |  | 
**events_yesterday** | **int** |  | 
**events_this_week** | **int** |  | 
**events_last_week** | **int** |  | 
**entries_today** | **int** |  | 
**exits_today** | **int** |  | 
**active_geofences** | **int** |  | 

## Example

```python
from spatialflow_generated.models.device_stats_out import DeviceStatsOut

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceStatsOut from a JSON string
device_stats_out_instance = DeviceStatsOut.from_json(json)
# print the JSON string representation of the object
print(DeviceStatsOut.to_json())

# convert the object into a dict
device_stats_out_dict = device_stats_out_instance.to_dict()
# create an instance of DeviceStatsOut from a dict
device_stats_out_from_dict = DeviceStatsOut.from_dict(device_stats_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


