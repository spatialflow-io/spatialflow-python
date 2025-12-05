# OAuthProvidersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | **List[Optional[Dict[str, object]]]** |  | 

## Example

```python
from spatialflow_generated.models.o_auth_providers_response import OAuthProvidersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthProvidersResponse from a JSON string
o_auth_providers_response_instance = OAuthProvidersResponse.from_json(json)
# print the JSON string representation of the object
print(OAuthProvidersResponse.to_json())

# convert the object into a dict
o_auth_providers_response_dict = o_auth_providers_response_instance.to_dict()
# create an instance of OAuthProvidersResponse from a dict
o_auth_providers_response_from_dict = OAuthProvidersResponse.from_dict(o_auth_providers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


