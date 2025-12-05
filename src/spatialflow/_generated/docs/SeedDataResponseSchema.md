# SeedDataResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**details** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.seed_data_response_schema import SeedDataResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SeedDataResponseSchema from a JSON string
seed_data_response_schema_instance = SeedDataResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SeedDataResponseSchema.to_json())

# convert the object into a dict
seed_data_response_schema_dict = seed_data_response_schema_instance.to_dict()
# create an instance of SeedDataResponseSchema from a dict
seed_data_response_schema_from_dict = SeedDataResponseSchema.from_dict(seed_data_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


