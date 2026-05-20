# WorkflowStatisticsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_executions** | **int** |  | [optional] [default to 0]
**successful_executions** | **int** |  | [optional] [default to 0]
**failed_executions** | **int** |  | [optional] [default to 0]
**running_executions** | **int** |  | [optional] [default to 0]
**cancelled_executions** | **int** |  | [optional] [default to 0]
**success_rate** | **float** |  | [optional] [default to 0.0]
**average_duration_seconds** | **float** |  | [optional] 
**recent_executions** | [**List[RecentExecutionOut]**](RecentExecutionOut.md) |  | [optional] 
**last_7_days** | **Dict[str, object]** |  | [optional] 
**last_30_days** | **Dict[str, object]** |  | [optional] 
**executions_by_day** | **List[object]** |  | [optional] 
**common_errors** | **List[object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.workflow_statistics_out import WorkflowStatisticsOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStatisticsOut from a JSON string
workflow_statistics_out_instance = WorkflowStatisticsOut.from_json(json)
# print the JSON string representation of the object
print(WorkflowStatisticsOut.to_json())

# convert the object into a dict
workflow_statistics_out_dict = workflow_statistics_out_instance.to_dict()
# create an instance of WorkflowStatisticsOut from a dict
workflow_statistics_out_from_dict = WorkflowStatisticsOut.from_dict(workflow_statistics_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


