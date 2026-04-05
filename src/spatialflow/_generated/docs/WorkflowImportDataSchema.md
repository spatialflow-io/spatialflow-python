# WorkflowImportDataSchema

Schema for the workflow data within an import payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**trigger_config** | **Dict[str, object]** |  | [optional] 
**steps** | **List[Dict[str, object]]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**category** | **str** |  | [optional] 
**is_test_mode** | **bool** |  | [optional] 

## Example

```python
from spatialflow_generated.models.workflow_import_data_schema import WorkflowImportDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowImportDataSchema from a JSON string
workflow_import_data_schema_instance = WorkflowImportDataSchema.from_json(json)
# print the JSON string representation of the object
print(WorkflowImportDataSchema.to_json())

# convert the object into a dict
workflow_import_data_schema_dict = workflow_import_data_schema_instance.to_dict()
# create an instance of WorkflowImportDataSchema from a dict
workflow_import_data_schema_from_dict = WorkflowImportDataSchema.from_dict(workflow_import_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


