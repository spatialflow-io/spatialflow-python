# WorkflowRunsStatsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_runs_24h** | **int** |  | 
**successful_runs_24h** | **int** |  | 
**failed_runs_24h** | **int** |  | 
**success_rate** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.workflow_runs_stats_out import WorkflowRunsStatsOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRunsStatsOut from a JSON string
workflow_runs_stats_out_instance = WorkflowRunsStatsOut.from_json(json)
# print the JSON string representation of the object
print(WorkflowRunsStatsOut.to_json())

# convert the object into a dict
workflow_runs_stats_out_dict = workflow_runs_stats_out_instance.to_dict()
# create an instance of WorkflowRunsStatsOut from a dict
workflow_runs_stats_out_from_dict = WorkflowRunsStatsOut.from_dict(workflow_runs_stats_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


