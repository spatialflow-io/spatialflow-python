# UsageLimits

Usage vs limits for workspace detail view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_events** | **int** |  | [optional] [default to 0]
**action_deliveries** | **int** |  | [optional] [default to 0]
**event_units** | **float** |  | [optional] [default to 0.0]
**max_geofences** | **int** |  | [optional] 
**max_devices** | **int** |  | [optional] 
**max_events_per_month** | **int** |  | [optional] 
**geofence_count** | **int** |  | [optional] [default to 0]
**device_count** | **int** |  | [optional] [default to 0]

## Example

```python
from spatialflow_generated.models.usage_limits import UsageLimits

# TODO update the JSON string below
json = "{}"
# create an instance of UsageLimits from a JSON string
usage_limits_instance = UsageLimits.from_json(json)
# print the JSON string representation of the object
print(UsageLimits.to_json())

# convert the object into a dict
usage_limits_dict = usage_limits_instance.to_dict()
# create an instance of UsageLimits from a dict
usage_limits_from_dict = UsageLimits.from_dict(usage_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


