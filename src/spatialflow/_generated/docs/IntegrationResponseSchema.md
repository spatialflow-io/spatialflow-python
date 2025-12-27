# IntegrationResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**description** | **str** |  | 
**is_active** | **bool** |  | 
**is_verified** | **bool** |  | 
**health_status** | **str** |  | 
**health_message** | **str** |  | 
**usage_count** | **int** |  | 
**last_used_at** | **str** |  | [optional] 
**last_verified_at** | **str** |  | [optional] 
**tags** | **List[str]** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.integration_response_schema import IntegrationResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationResponseSchema from a JSON string
integration_response_schema_instance = IntegrationResponseSchema.from_json(json)
# print the JSON string representation of the object
print(IntegrationResponseSchema.to_json())

# convert the object into a dict
integration_response_schema_dict = integration_response_schema_instance.to_dict()
# create an instance of IntegrationResponseSchema from a dict
integration_response_schema_from_dict = IntegrationResponseSchema.from_dict(integration_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


