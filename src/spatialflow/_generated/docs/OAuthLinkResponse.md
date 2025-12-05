# OAuthLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**provider** | **str** |  | 

## Example

```python
from spatialflow_generated.models.o_auth_link_response import OAuthLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthLinkResponse from a JSON string
o_auth_link_response_instance = OAuthLinkResponse.from_json(json)
# print the JSON string representation of the object
print(OAuthLinkResponse.to_json())

# convert the object into a dict
o_auth_link_response_dict = o_auth_link_response_instance.to_dict()
# create an instance of OAuthLinkResponse from a dict
o_auth_link_response_from_dict = OAuthLinkResponse.from_dict(o_auth_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


