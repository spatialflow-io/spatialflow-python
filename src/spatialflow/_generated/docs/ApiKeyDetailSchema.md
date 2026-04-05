# ApiKeyDetailSchema

Schema for API key details returned after creation or rotation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**api_key** | **str** |  | 
**created_at** | **datetime** |  | 
**read_only** | **bool** |  | 
**description** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.api_key_detail_schema import ApiKeyDetailSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyDetailSchema from a JSON string
api_key_detail_schema_instance = ApiKeyDetailSchema.from_json(json)
# print the JSON string representation of the object
print(ApiKeyDetailSchema.to_json())

# convert the object into a dict
api_key_detail_schema_dict = api_key_detail_schema_instance.to_dict()
# create an instance of ApiKeyDetailSchema from a dict
api_key_detail_schema_from_dict = ApiKeyDetailSchema.from_dict(api_key_detail_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


