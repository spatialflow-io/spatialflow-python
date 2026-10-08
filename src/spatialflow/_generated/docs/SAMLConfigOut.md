# SAMLConfigOut

Output schema for SAML SSO configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**entity_id** | **str** |  | 
**sso_url** | **str** |  | 
**certificate** | **str** |  | 
**covered_domain** | **str** |  | 
**is_enabled** | **bool** |  | 
**domain_verified** | **bool** |  | 
**domain_verified_at** | **datetime** |  | [optional] 
**domain_verification_dns_name** | **str** |  | 
**domain_verification_dns_value** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.saml_config_out import SAMLConfigOut

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLConfigOut from a JSON string
saml_config_out_instance = SAMLConfigOut.from_json(json)
# print the JSON string representation of the object
print(SAMLConfigOut.to_json())

# convert the object into a dict
saml_config_out_dict = saml_config_out_instance.to_dict()
# create an instance of SAMLConfigOut from a dict
saml_config_out_from_dict = SAMLConfigOut.from_dict(saml_config_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


