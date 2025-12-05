# WorkflowUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**nodes** | **List[Dict[str, object]]** |  | [optional] 
**edges** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.workflow_update import WorkflowUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowUpdate from a JSON string
workflow_update_instance = WorkflowUpdate.from_json(json)
# print the JSON string representation of the object
print(WorkflowUpdate.to_json())

# convert the object into a dict
workflow_update_dict = workflow_update_instance.to_dict()
# create an instance of WorkflowUpdate from a dict
workflow_update_from_dict = WorkflowUpdate.from_dict(workflow_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


