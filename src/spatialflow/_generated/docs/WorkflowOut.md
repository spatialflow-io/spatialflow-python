# WorkflowOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**status** | **str** |  | 
**nodes** | **List[Optional[Dict[str, object]]]** |  | 
**edges** | **List[Optional[Dict[str, object]]]** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**last_run** | **str** |  | 
**run_count** | **int** |  | 
**success_rate** | **float** |  | 
**user_id** | **str** |  | 
**workspace_id** | **str** |  | [optional] 
**version** | **int** |  | 

## Example

```python
from spatialflow_generated.models.workflow_out import WorkflowOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowOut from a JSON string
workflow_out_instance = WorkflowOut.from_json(json)
# print the JSON string representation of the object
print(WorkflowOut.to_json())

# convert the object into a dict
workflow_out_dict = workflow_out_instance.to_dict()
# create an instance of WorkflowOut from a dict
workflow_out_from_dict = WorkflowOut.from_dict(workflow_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


