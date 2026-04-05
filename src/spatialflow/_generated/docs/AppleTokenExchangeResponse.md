# AppleTokenExchangeResponse


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
from spatialflow_generated.models.apple_token_exchange_response import AppleTokenExchangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppleTokenExchangeResponse from a JSON string
apple_token_exchange_response_instance = AppleTokenExchangeResponse.from_json(json)
# print the JSON string representation of the object
print(AppleTokenExchangeResponse.to_json())

# convert the object into a dict
apple_token_exchange_response_dict = apple_token_exchange_response_instance.to_dict()
# create an instance of AppleTokenExchangeResponse from a dict
apple_token_exchange_response_from_dict = AppleTokenExchangeResponse.from_dict(apple_token_exchange_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


