# ConfigurationUpdateRequest

Request to update a configuration value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** |  | 

## Example

```python
from spatialflow_generated.models.configuration_update_request import ConfigurationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationUpdateRequest from a JSON string
configuration_update_request_instance = ConfigurationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ConfigurationUpdateRequest.to_json())

# convert the object into a dict
configuration_update_request_dict = configuration_update_request_instance.to_dict()
# create an instance of ConfigurationUpdateRequest from a dict
configuration_update_request_from_dict = ConfigurationUpdateRequest.from_dict(configuration_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


