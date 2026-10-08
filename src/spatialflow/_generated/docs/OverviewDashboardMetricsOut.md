# OverviewDashboardMetricsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | **str** |  | 
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 
**active_workflows** | **int** |  | 
**events_total** | **int** |  | 
**action_delivery_success** | [**OverviewActionDeliveryOut**](OverviewActionDeliveryOut.md) |  | 
**comparison** | [**OverviewComparisonOut**](OverviewComparisonOut.md) |  | 

## Example

```python
from spatialflow_generated.models.overview_dashboard_metrics_out import OverviewDashboardMetricsOut

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewDashboardMetricsOut from a JSON string
overview_dashboard_metrics_out_instance = OverviewDashboardMetricsOut.from_json(json)
# print the JSON string representation of the object
print(OverviewDashboardMetricsOut.to_json())

# convert the object into a dict
overview_dashboard_metrics_out_dict = overview_dashboard_metrics_out_instance.to_dict()
# create an instance of OverviewDashboardMetricsOut from a dict
overview_dashboard_metrics_out_from_dict = OverviewDashboardMetricsOut.from_dict(overview_dashboard_metrics_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


