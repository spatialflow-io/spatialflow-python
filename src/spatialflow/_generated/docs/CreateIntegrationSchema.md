# CreateIntegrationSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User-friendly name for the integration | 
**type** | **str** | Integration type (webhook, slack, twilio_sms, etc.) | 
**description** | **str** |  | [optional] 
**config** | **Dict[str, object]** | Integration-specific configuration | 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.create_integration_schema import CreateIntegrationSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIntegrationSchema from a JSON string
create_integration_schema_instance = CreateIntegrationSchema.from_json(json)
# print the JSON string representation of the object
print(CreateIntegrationSchema.to_json())

# convert the object into a dict
create_integration_schema_dict = create_integration_schema_instance.to_dict()
# create an instance of CreateIntegrationSchema from a dict
create_integration_schema_from_dict = CreateIntegrationSchema.from_dict(create_integration_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


