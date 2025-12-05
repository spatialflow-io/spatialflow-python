# ConfigFieldDefinitionResponse

Response schema for ConfigFieldDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**integration_type_id** | **str** |  | 
**name** | **str** |  | 
**label** | **str** |  | 
**field_type** | **str** |  | 
**required** | **bool** |  | 
**placeholder** | **str** |  | 
**help_text** | **str** |  | 
**default_value** | **str** |  | 
**validation_rules** | **Dict[str, object]** |  | 
**options** | **List[Dict[str, str]]** |  | 
**order** | **int** |  | 
**depends_on** | **str** |  | 
**depends_on_value** | **str** |  | 

## Example

```python
from spatialflow_generated.models.config_field_definition_response import ConfigFieldDefinitionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFieldDefinitionResponse from a JSON string
config_field_definition_response_instance = ConfigFieldDefinitionResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigFieldDefinitionResponse.to_json())

# convert the object into a dict
config_field_definition_response_dict = config_field_definition_response_instance.to_dict()
# create an instance of ConfigFieldDefinitionResponse from a dict
config_field_definition_response_from_dict = ConfigFieldDefinitionResponse.from_dict(config_field_definition_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


