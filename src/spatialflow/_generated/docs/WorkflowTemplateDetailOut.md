# WorkflowTemplateDetailOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**category** | **str** |  | 
**lane** | **str** |  | 
**trigger_config** | **Dict[str, object]** |  | 
**steps** | **List[object]** |  | 
**tags** | **List[str]** |  | [optional] 
**is_featured** | **bool** |  | 
**usage_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.workflow_template_detail_out import WorkflowTemplateDetailOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTemplateDetailOut from a JSON string
workflow_template_detail_out_instance = WorkflowTemplateDetailOut.from_json(json)
# print the JSON string representation of the object
print(WorkflowTemplateDetailOut.to_json())

# convert the object into a dict
workflow_template_detail_out_dict = workflow_template_detail_out_instance.to_dict()
# create an instance of WorkflowTemplateDetailOut from a dict
workflow_template_detail_out_from_dict = WorkflowTemplateDetailOut.from_dict(workflow_template_detail_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


