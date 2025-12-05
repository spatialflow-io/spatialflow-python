# WorkflowIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**nodes** | **List[Dict[str, object]]** |  | 
**edges** | **List[Dict[str, object]]** |  | 

## Example

```python
from spatialflow_generated.models.workflow_in import WorkflowIn

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowIn from a JSON string
workflow_in_instance = WorkflowIn.from_json(json)
# print the JSON string representation of the object
print(WorkflowIn.to_json())

# convert the object into a dict
workflow_in_dict = workflow_in_instance.to_dict()
# create an instance of WorkflowIn from a dict
workflow_in_from_dict = WorkflowIn.from_dict(workflow_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


