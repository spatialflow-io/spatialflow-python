# ExecutionStepDetailOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_index** | **int** |  | 
**node_id** | **str** |  | [optional] 
**step_name** | **str** |  | 
**step_type** | **str** |  | 
**status** | **str** |  | 
**started_at** | **str** |  | [optional] 
**completed_at** | **str** |  | [optional] 
**duration_ms** | **float** |  | [optional] 
**error_message** | **str** |  | [optional] 
**input_data** | **Dict[str, object]** |  | [optional] 
**output_data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.execution_step_detail_out import ExecutionStepDetailOut

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionStepDetailOut from a JSON string
execution_step_detail_out_instance = ExecutionStepDetailOut.from_json(json)
# print the JSON string representation of the object
print(ExecutionStepDetailOut.to_json())

# convert the object into a dict
execution_step_detail_out_dict = execution_step_detail_out_instance.to_dict()
# create an instance of ExecutionStepDetailOut from a dict
execution_step_detail_out_from_dict = ExecutionStepDetailOut.from_dict(execution_step_detail_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


