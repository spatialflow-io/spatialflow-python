# OverviewOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | [**BadgeCountsOut**](BadgeCountsOut.md) |  | 
**incidents** | [**List[IncidentOut]**](IncidentOut.md) |  | 
**dashboard_stats** | [**OverviewDashboardStatsOut**](OverviewDashboardStatsOut.md) |  | 
**dashboard_metrics** | [**OverviewDashboardMetricsOut**](OverviewDashboardMetricsOut.md) |  | 
**dlq_stats** | [**OverviewDlqStatsOut**](OverviewDlqStatsOut.md) |  | [optional] 
**workflow_stats** | [**OverviewWorkflowStatsOut**](OverviewWorkflowStatsOut.md) |  | [optional] 
**recent_events** | [**List[OverviewEventOut]**](OverviewEventOut.md) |  | 

## Example

```python
from spatialflow_generated.models.overview_out import OverviewOut

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewOut from a JSON string
overview_out_instance = OverviewOut.from_json(json)
# print the JSON string representation of the object
print(OverviewOut.to_json())

# convert the object into a dict
overview_out_dict = overview_out_instance.to_dict()
# create an instance of OverviewOut from a dict
overview_out_from_dict = OverviewOut.from_dict(overview_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


