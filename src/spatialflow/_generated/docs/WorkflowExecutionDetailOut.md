# WorkflowExecutionDetailOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**workflow_id** | **str** |  | 
**workflow_name** | **str** |  | 
**execution_id** | **str** |  | 
**trigger_source** | **str** |  | 
**trigger_data** | **Dict[str, object]** |  | [optional] 
**status** | **str** |  | 
**current_step** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**started_at** | **str** |  | [optional] 
**completed_at** | **str** |  | [optional] 
**duration_seconds** | **float** |  | [optional] 
**steps** | [**List[ExecutionStepDetailOut]**](ExecutionStepDetailOut.md) |  | 
**execution_data** | **Dict[str, object]** |  | [optional] 
**workflow_config** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.workflow_execution_detail_out import WorkflowExecutionDetailOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecutionDetailOut from a JSON string
workflow_execution_detail_out_instance = WorkflowExecutionDetailOut.from_json(json)
# print the JSON string representation of the object
print(WorkflowExecutionDetailOut.to_json())

# convert the object into a dict
workflow_execution_detail_out_dict = workflow_execution_detail_out_instance.to_dict()
# create an instance of WorkflowExecutionDetailOut from a dict
workflow_execution_detail_out_from_dict = WorkflowExecutionDetailOut.from_dict(workflow_execution_detail_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


