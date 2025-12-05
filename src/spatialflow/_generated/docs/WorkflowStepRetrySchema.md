# WorkflowStepRetrySchema

Retry configuration for a workflow step.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_index** | **int** |  | 
**step_name** | **str** |  | [optional] 
**action_type** | **str** |  | 
**retry_config** | [**ActionRetryConfigSchema**](ActionRetryConfigSchema.md) |  | 

## Example

```python
from spatialflow_generated.models.workflow_step_retry_schema import WorkflowStepRetrySchema

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepRetrySchema from a JSON string
workflow_step_retry_schema_instance = WorkflowStepRetrySchema.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepRetrySchema.to_json())

# convert the object into a dict
workflow_step_retry_schema_dict = workflow_step_retry_schema_instance.to_dict()
# create an instance of WorkflowStepRetrySchema from a dict
workflow_step_retry_schema_from_dict = WorkflowStepRetrySchema.from_dict(workflow_step_retry_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


