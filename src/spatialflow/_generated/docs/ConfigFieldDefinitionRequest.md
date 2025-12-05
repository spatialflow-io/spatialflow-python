# ConfigFieldDefinitionRequest

Request schema for creating/updating config field definitions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Field name in the configuration | 
**label** | **str** | Display label for this field | 
**field_type** | **str** | Field type: text, password, url, email, tel, number, select, boolean, json, textarea | [optional] [default to 'text']
**required** | **bool** | Whether this field is required | [optional] [default to False]
**placeholder** | **str** |  | [optional] 
**help_text** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
**validation_rules** | **Dict[str, object]** | JSON validation rules | [optional] 
**options** | **List[Dict[str, str]]** | Options for select fields | [optional] 
**order** | **int** | Display order for this field | [optional] [default to 0]
**depends_on** | **str** |  | [optional] 
**depends_on_value** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.config_field_definition_request import ConfigFieldDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigFieldDefinitionRequest from a JSON string
config_field_definition_request_instance = ConfigFieldDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print(ConfigFieldDefinitionRequest.to_json())

# convert the object into a dict
config_field_definition_request_dict = config_field_definition_request_instance.to_dict()
# create an instance of ConfigFieldDefinitionRequest from a dict
config_field_definition_request_from_dict = ConfigFieldDefinitionRequest.from_dict(config_field_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


