# TestIntegrationResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**verified** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.test_integration_response_schema import TestIntegrationResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TestIntegrationResponseSchema from a JSON string
test_integration_response_schema_instance = TestIntegrationResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TestIntegrationResponseSchema.to_json())

# convert the object into a dict
test_integration_response_schema_dict = test_integration_response_schema_instance.to_dict()
# create an instance of TestIntegrationResponseSchema from a dict
test_integration_response_schema_from_dict = TestIntegrationResponseSchema.from_dict(test_integration_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


