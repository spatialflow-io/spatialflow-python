# EnhancedDashboardStatsResponse

Enhanced dashboard stats with revenue metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_users** | **int** |  | 
**active_users** | **int** |  | 
**new_users_this_week** | **int** |  | 
**total_workspaces** | **int** |  | 
**paid_subscriptions** | **int** |  | [optional] [default to 0]
**trial_subscriptions** | **int** |  | [optional] [default to 0]
**canceled_subscriptions** | **int** |  | [optional] [default to 0]
**monthly_recurring_revenue** | **float** |  | [optional] [default to 0.0]

## Example

```python
from spatialflow_generated.models.enhanced_dashboard_stats_response import EnhancedDashboardStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancedDashboardStatsResponse from a JSON string
enhanced_dashboard_stats_response_instance = EnhancedDashboardStatsResponse.from_json(json)
# print the JSON string representation of the object
print(EnhancedDashboardStatsResponse.to_json())

# convert the object into a dict
enhanced_dashboard_stats_response_dict = enhanced_dashboard_stats_response_instance.to_dict()
# create an instance of EnhancedDashboardStatsResponse from a dict
enhanced_dashboard_stats_response_from_dict = EnhancedDashboardStatsResponse.from_dict(enhanced_dashboard_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


