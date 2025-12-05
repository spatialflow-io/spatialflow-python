# DashboardComparisonMetrics

Comparison metrics vs previous period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events_change** | **int** | Absolute change in events vs previous period | 
**workflows_change** | **int** | Absolute change in active workflows vs previous period | 
**success_rate_change** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.dashboard_comparison_metrics import DashboardComparisonMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardComparisonMetrics from a JSON string
dashboard_comparison_metrics_instance = DashboardComparisonMetrics.from_json(json)
# print the JSON string representation of the object
print(DashboardComparisonMetrics.to_json())

# convert the object into a dict
dashboard_comparison_metrics_dict = dashboard_comparison_metrics_instance.to_dict()
# create an instance of DashboardComparisonMetrics from a dict
dashboard_comparison_metrics_from_dict = DashboardComparisonMetrics.from_dict(dashboard_comparison_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


