# ExecutionOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**workflow_id** | **str** |  | 
**workflow_name** | **str** |  | 
**execution_id** | **str** |  | 
**trigger_source** | **str** |  | 
**status** | **str** |  | 
**started_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**duration_seconds** | **float** |  | 
**error_message** | **str** |  | 

## Example

```python
from spatialflow_generated.models.execution_out import ExecutionOut

# TODO update the JSON string below
json = "{}"
# create an instance of ExecutionOut from a JSON string
execution_out_instance = ExecutionOut.from_json(json)
# print the JSON string representation of the object
print(ExecutionOut.to_json())

# convert the object into a dict
execution_out_dict = execution_out_instance.to_dict()
# create an instance of ExecutionOut from a dict
execution_out_from_dict = ExecutionOut.from_dict(execution_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


