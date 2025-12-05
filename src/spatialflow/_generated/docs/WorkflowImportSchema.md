# WorkflowImportSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | 
**workflow** | **Dict[str, object]** |  | 

## Example

```python
from spatialflow_generated.models.workflow_import_schema import WorkflowImportSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowImportSchema from a JSON string
workflow_import_schema_instance = WorkflowImportSchema.from_json(json)
# print the JSON string representation of the object
print(WorkflowImportSchema.to_json())

# convert the object into a dict
workflow_import_schema_dict = workflow_import_schema_instance.to_dict()
# create an instance of WorkflowImportSchema from a dict
workflow_import_schema_from_dict = WorkflowImportSchema.from_dict(workflow_import_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


