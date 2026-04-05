# ConfigurationResetResponse

Response for configuration reset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**new_source** | **str** |  | 
**effective_value** | [**AnyOf**](AnyOf.md) |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.configuration_reset_response import ConfigurationResetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationResetResponse from a JSON string
configuration_reset_response_instance = ConfigurationResetResponse.from_json(json)
# print the JSON string representation of the object
print(ConfigurationResetResponse.to_json())

# convert the object into a dict
configuration_reset_response_dict = configuration_reset_response_instance.to_dict()
# create an instance of ConfigurationResetResponse from a dict
configuration_reset_response_from_dict = ConfigurationResetResponse.from_dict(configuration_reset_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


