# ExecutionDetailOut


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

## Example

```python
from spatialflow_generated.models.execution_detail_out import ExecutionDetailOut

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionDetailOut from a JSON string
execution_detail_out_instance = ExecutionDetailOut.from_json(json)
# print the JSON string representation of the object
print(ExecutionDetailOut.to_json())

# convert the object into a dict
execution_detail_out_dict = execution_detail_out_instance.to_dict()
# create an instance of ExecutionDetailOut from a dict
execution_detail_out_from_dict = ExecutionDetailOut.from_dict(execution_detail_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


