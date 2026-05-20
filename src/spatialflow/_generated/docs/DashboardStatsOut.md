# DashboardStatsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_count** | **int** |  | 
**offline_stale_count** | **int** |  | 
**in_geofence_count** | **int** |  | 
**alerts_open** | **int** |  | 
**workflow_failures_1h** | **int** |  | 
**webhook_retries_1h** | **int** |  | 

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


