# ImportResultSchema

Result of import operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**integration_id** | **str** |  | [optional] 
**message** | **str** |  | 
**conflicts** | **List[str]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.import_result_schema import ImportResultSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ImportResultSchema from a JSON string
import_result_schema_instance = ImportResultSchema.from_json(json)
# print the JSON string representation of the object
print(ImportResultSchema.to_json())

# convert the object into a dict
import_result_schema_dict = import_result_schema_instance.to_dict()
# create an instance of ImportResultSchema from a dict
import_result_schema_from_dict = ImportResultSchema.from_dict(import_result_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


