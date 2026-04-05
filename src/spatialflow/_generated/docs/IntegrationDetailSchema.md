# IntegrationDetailSchema

Detailed integration response with masked config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
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
**config** | **Dict[str, object]** |  | 

## Example

```python
from spatialflow_generated.models.integration_detail_schema import IntegrationDetailSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationDetailSchema from a JSON string
integration_detail_schema_instance = IntegrationDetailSchema.from_json(json)
# print the JSON string representation of the object
print(IntegrationDetailSchema.to_json())

# convert the object into a dict
integration_detail_schema_dict = integration_detail_schema_instance.to_dict()
# create an instance of IntegrationDetailSchema from a dict
integration_detail_schema_from_dict = IntegrationDetailSchema.from_dict(integration_detail_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


