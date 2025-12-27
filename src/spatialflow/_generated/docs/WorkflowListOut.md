# WorkflowListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**last_run** | **str** |  | 
**run_count** | **int** |  | 
**success_rate** | **float** |  | 
**user_id** | **str** |  | 
**version** | **int** |  | 

## Example

```python
from spatialflow_generated.models.workflow_list_out import WorkflowListOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowListOut from a JSON string
workflow_list_out_instance = WorkflowListOut.from_json(json)
# print the JSON string representation of the object
print(WorkflowListOut.to_json())

# convert the object into a dict
workflow_list_out_dict = workflow_list_out_instance.to_dict()
# create an instance of WorkflowListOut from a dict
workflow_list_out_from_dict = WorkflowListOut.from_dict(workflow_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


