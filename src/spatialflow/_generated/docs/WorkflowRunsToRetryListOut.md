# WorkflowRunsToRetryListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[WorkflowRunsToRetryOut]**](WorkflowRunsToRetryOut.md) |  | 
**next_cursor** | **str** |  | [optional] 
**has_more** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.workflow_runs_to_retry_list_out import WorkflowRunsToRetryListOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRunsToRetryListOut from a JSON string
workflow_runs_to_retry_list_out_instance = WorkflowRunsToRetryListOut.from_json(json)
# print the JSON string representation of the object
print(WorkflowRunsToRetryListOut.to_json())

# convert the object into a dict
workflow_runs_to_retry_list_out_dict = workflow_runs_to_retry_list_out_instance.to_dict()
# create an instance of WorkflowRunsToRetryListOut from a dict
workflow_runs_to_retry_list_out_from_dict = WorkflowRunsToRetryListOut.from_dict(workflow_runs_to_retry_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


