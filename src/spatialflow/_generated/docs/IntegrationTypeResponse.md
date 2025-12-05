# IntegrationTypeResponse

Response schema for IntegrationType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**icon** | **str** |  | 
**category** | **str** |  | 
**handler_class** | **str** |  | 
**validator_class** | **str** |  | 
**is_active** | **bool** |  | 
**is_builtin** | **bool** |  | 
**oauth_enabled** | **bool** |  | 
**oauth_config** | **Dict[str, object]** |  | 
**documentation_url** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**config_fields_count** | **int** |  | [optional] [default to 0]

## Example

```python
from spatialflow_generated.models.integration_type_response import IntegrationTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationTypeResponse from a JSON string
integration_type_response_instance = IntegrationTypeResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationTypeResponse.to_json())

# convert the object into a dict
integration_type_response_dict = integration_type_response_instance.to_dict()
# create an instance of IntegrationTypeResponse from a dict
integration_type_response_from_dict = IntegrationTypeResponse.from_dict(integration_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


