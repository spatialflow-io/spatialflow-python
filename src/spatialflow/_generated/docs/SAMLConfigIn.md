# SAMLConfigIn

Input schema for creating/updating SAML SSO configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | 
**sso_url** | **str** |  | 
**certificate** | **str** |  | 
**covered_domain** | **str** |  | 
**is_enabled** | **bool** |  | [optional] [default to True]

## Example

```python
from spatialflow_generated.models.saml_config_in import SAMLConfigIn

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLConfigIn from a JSON string
saml_config_in_instance = SAMLConfigIn.from_json(json)
# print the JSON string representation of the object
print(SAMLConfigIn.to_json())

# convert the object into a dict
saml_config_in_dict = saml_config_in_instance.to_dict()
# create an instance of SAMLConfigIn from a dict
saml_config_in_from_dict = SAMLConfigIn.from_dict(saml_config_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


