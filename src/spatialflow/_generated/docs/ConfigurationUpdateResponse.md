# ConfigurationUpdateResponse

Response for configuration update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**requires_restart** | **bool** |  | 
**error** | **str** |  | [optional] 
**effective_value** | [**AnyOf**](AnyOf.md) |  | [optional] 

## Example

```python
from spatialflow_generated.models.configuration_update_response import ConfigurationUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationUpdateResponse from a JSON string
configuration_update_response_instance = ConfigurationUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigurationUpdateResponse.to_json())

# convert the object into a dict
configuration_update_response_dict = configuration_update_response_instance.to_dict()
# create an instance of ConfigurationUpdateResponse from a dict
configuration_update_response_from_dict = ConfigurationUpdateResponse.from_dict(configuration_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


