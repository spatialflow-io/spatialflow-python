# OverviewEventDeviceOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**device_id** | **str** |  | 
**name** | **str** |  | 
**driver_name** | **str** |  | [optional] 
**type** | **str** |  | 
**last_accuracy** | **float** |  | [optional] 
**last_battery_level** | **int** |  | [optional] 
**last_battery_charging** | **bool** |  | [optional] 
**last_battery_time** | **datetime** |  | [optional] 

## Example

```python
from spatialflow_generated.models.overview_event_device_out import OverviewEventDeviceOut

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewEventDeviceOut from a JSON string
overview_event_device_out_instance = OverviewEventDeviceOut.from_json(json)
# print the JSON string representation of the object
print(OverviewEventDeviceOut.to_json())

# convert the object into a dict
overview_event_device_out_dict = overview_event_device_out_instance.to_dict()
# create an instance of OverviewEventDeviceOut from a dict
overview_event_device_out_from_dict = OverviewEventDeviceOut.from_dict(overview_event_device_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


