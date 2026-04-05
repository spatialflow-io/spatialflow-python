# AppleTokenExchangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_token** | **str** |  | 
**authorization_code** | **str** |  | 
**full_name** | [**AppleFullName**](AppleFullName.md) |  | [optional] 
**nonce** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.apple_token_exchange_request import AppleTokenExchangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppleTokenExchangeRequest from a JSON string
apple_token_exchange_request_instance = AppleTokenExchangeRequest.from_json(json)
# print the JSON string representation of the object
print(AppleTokenExchangeRequest.to_json())

# convert the object into a dict
apple_token_exchange_request_dict = apple_token_exchange_request_instance.to_dict()
# create an instance of AppleTokenExchangeRequest from a dict
apple_token_exchange_request_from_dict = AppleTokenExchangeRequest.from_dict(apple_token_exchange_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


