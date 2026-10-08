# DashboardStatsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_device_count** | **int** |  | 
**live_count** | **int** |  | 
**reporting_count** | **int** |  | 
**offline_stale_count** | **int** |  | 
**expected_reporting_count** | **int** |  | 
**attention_count** | **int** |  | 
**parked_count** | **int** |  | 
**reporting_window_minutes** | **int** |  | 
**paused_count** | **int** |  | 
**off_shift_count** | **int** |  | 
**low_battery_count** | **int** |  | 
**low_battery_window_minutes** | **int** |  | 
**in_geofence_count** | **int** |  | 
**last_known_geofence_count** | **int** |  | 
**confirmed_current_geofence_count** | **int** |  | 
**alerts_open** | **int** |  | 
**workflow_failures_1h** | **int** |  | [optional] 
**webhook_retries_1h** | **int** |  | [optional] 

## Example

```python
from spatialflow_generated.models.dashboard_stats_out import DashboardStatsOut

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardStatsOut from a JSON string
dashboard_stats_out_instance = DashboardStatsOut.from_json(json)
# print the JSON string representation of the object
print(DashboardStatsOut.to_json())

# convert the object into a dict
dashboard_stats_out_dict = dashboard_stats_out_instance.to_dict()
# create an instance of DashboardStatsOut from a dict
dashboard_stats_out_from_dict = DashboardStatsOut.from_dict(dashboard_stats_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


