# DashboardStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_users** | **int** |  | 
**active_users** | **int** |  | 
**new_users_this_week** | **int** |  | 
**total_workspaces** | **int** |  | 

## Example

```python
from spatialflow_generated.models.dashboard_stats_response import DashboardStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardStatsResponse from a JSON string
dashboard_stats_response_instance = DashboardStatsResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardStatsResponse.to_json())

# convert the object into a dict
dashboard_stats_response_dict = dashboard_stats_response_instance.to_dict()
# create an instance of DashboardStatsResponse from a dict
dashboard_stats_response_from_dict = DashboardStatsResponse.from_dict(dashboard_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


