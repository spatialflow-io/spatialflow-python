# OverviewWorkflowStatsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_runs_24h** | **int** |  | 
**successful_runs_24h** | **int** |  | 
**failed_runs_24h** | **int** |  | 
**success_rate** | **float** |  | [optional] 
**source** | **str** |  | 

## Example

```python
from spatialflow_generated.models.overview_workflow_stats_out import OverviewWorkflowStatsOut

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewWorkflowStatsOut from a JSON string
overview_workflow_stats_out_instance = OverviewWorkflowStatsOut.from_json(json)
# print the JSON string representation of the object
print(OverviewWorkflowStatsOut.to_json())

# convert the object into a dict
overview_workflow_stats_out_dict = overview_workflow_stats_out_instance.to_dict()
# create an instance of OverviewWorkflowStatsOut from a dict
overview_workflow_stats_out_from_dict = OverviewWorkflowStatsOut.from_dict(overview_workflow_stats_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


