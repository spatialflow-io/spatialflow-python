# SsoExchangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**refresh_token** | **str** |  | 
**token_type** | **str** |  | 
**expires_in** | **int** |  | 
**user** | **Dict[str, object]** |  | 
**created** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.sso_exchange_response import SsoExchangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SsoExchangeResponse from a JSON string
sso_exchange_response_instance = SsoExchangeResponse.from_json(json)
# print the JSON string representation of the object
print(SsoExchangeResponse.to_json())

# convert the object into a dict
sso_exchange_response_dict = sso_exchange_response_instance.to_dict()
# create an instance of SsoExchangeResponse from a dict
sso_exchange_response_from_dict = SsoExchangeResponse.from_dict(sso_exchange_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


