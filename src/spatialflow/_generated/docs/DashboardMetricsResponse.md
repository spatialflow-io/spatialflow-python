# DashboardMetricsResponse

Dashboard metrics response schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | **str** | Time range: today, 7d, 30d, or custom | 
**period_start** | **datetime** | Start of the period | 
**period_end** | **datetime** | End of the period | 
**active_workflows** | **int** | Number of active workflows in period | 
**events_total** | **int** | Total geofence events (entry/exit) in period | 
**action_delivery_success** | [**ActionDeliverySuccessMetrics**](ActionDeliverySuccessMetrics.md) | Action delivery success metrics (north-star KPI) | 
**comparison** | [**DashboardComparisonMetrics**](DashboardComparisonMetrics.md) | Comparison vs previous period | 

## Example

```python
from spatialflow_generated.models.dashboard_metrics_response import DashboardMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardMetricsResponse from a JSON string
dashboard_metrics_response_instance = DashboardMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardMetricsResponse.to_json())

# convert the object into a dict
dashboard_metrics_response_dict = dashboard_metrics_response_instance.to_dict()
# create an instance of DashboardMetricsResponse from a dict
dashboard_metrics_response_from_dict = DashboardMetricsResponse.from_dict(dashboard_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


