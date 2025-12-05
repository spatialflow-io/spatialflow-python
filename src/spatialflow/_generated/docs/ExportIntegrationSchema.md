# ExportIntegrationSchema

Schema for exported integration data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**description** | **str** |  | 
**config** | **Dict[str, object]** |  | 
**tags** | **List[str]** |  | 
**version** | **str** |  | [optional] [default to '1.0']

## Example

```python
from spatialflow_generated.models.export_integration_schema import ExportIntegrationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ExportIntegrationSchema from a JSON string
export_integration_schema_instance = ExportIntegrationSchema.from_json(json)
# print the JSON string representation of the object
print(ExportIntegrationSchema.to_json())

# convert the object into a dict
export_integration_schema_dict = export_integration_schema_instance.to_dict()
# create an instance of ExportIntegrationSchema from a dict
export_integration_schema_from_dict = ExportIntegrationSchema.from_dict(export_integration_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


