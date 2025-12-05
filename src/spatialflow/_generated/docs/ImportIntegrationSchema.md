# ImportIntegrationSchema

Schema for importing integration data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExportIntegrationSchema**](ExportIntegrationSchema.md) |  | 
**overwrite** | **bool** | Overwrite existing integration with same name | [optional] [default to False]
**decrypt_key** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.import_integration_schema import ImportIntegrationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportIntegrationSchema from a JSON string
import_integration_schema_instance = ImportIntegrationSchema.from_json(json)
# print the JSON string representation of the object
print(ImportIntegrationSchema.to_json())

# convert the object into a dict
import_integration_schema_dict = import_integration_schema_instance.to_dict()
# create an instance of ImportIntegrationSchema from a dict
import_integration_schema_from_dict = ImportIntegrationSchema.from_dict(import_integration_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


