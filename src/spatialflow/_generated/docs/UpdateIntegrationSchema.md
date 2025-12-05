# UpdateIntegrationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**config** | **Dict[str, object]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from spatialflow_generated.models.update_integration_schema import UpdateIntegrationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationSchema from a JSON string
update_integration_schema_instance = UpdateIntegrationSchema.from_json(json)
# print the JSON string representation of the object
print(UpdateIntegrationSchema.to_json())

# convert the object into a dict
update_integration_schema_dict = update_integration_schema_instance.to_dict()
# create an instance of UpdateIntegrationSchema from a dict
update_integration_schema_from_dict = UpdateIntegrationSchema.from_dict(update_integration_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


