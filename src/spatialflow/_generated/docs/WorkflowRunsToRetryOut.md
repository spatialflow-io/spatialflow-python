# WorkflowRunsToRetryOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** |  | 
**workflow_name** | **str** |  | 
**retryable_count** | **int** |  | 
**capped** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.workflow_runs_to_retry_out import WorkflowRunsToRetryOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRunsToRetryOut from a JSON string
workflow_runs_to_retry_out_instance = WorkflowRunsToRetryOut.from_json(json)
# print the JSON string representation of the object
print(WorkflowRunsToRetryOut.to_json())

# convert the object into a dict
workflow_runs_to_retry_out_dict = workflow_runs_to_retry_out_instance.to_dict()
# create an instance of WorkflowRunsToRetryOut from a dict
workflow_runs_to_retry_out_from_dict = WorkflowRunsToRetryOut.from_dict(workflow_runs_to_retry_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


