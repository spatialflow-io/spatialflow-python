# WorkflowRetryPolicyUpdateSchema

Schema for updating retry policies for a workflow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_id** | **str** |  | 
**default_retry_policy** | **str** |  | [optional] 
**step_overrides** | [**List[WorkflowStepRetrySchema]**](WorkflowStepRetrySchema.md) |  | [optional] 

## Example

```python
from spatialflow_generated.models.workflow_retry_policy_update_schema import WorkflowRetryPolicyUpdateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRetryPolicyUpdateSchema from a JSON string
workflow_retry_policy_update_schema_instance = WorkflowRetryPolicyUpdateSchema.from_json(json)
# print the JSON string representation of the object
print(WorkflowRetryPolicyUpdateSchema.to_json())

# convert the object into a dict
workflow_retry_policy_update_schema_dict = workflow_retry_policy_update_schema_instance.to_dict()
# create an instance of WorkflowRetryPolicyUpdateSchema from a dict
workflow_retry_policy_update_schema_from_dict = WorkflowRetryPolicyUpdateSchema.from_dict(workflow_retry_policy_update_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


