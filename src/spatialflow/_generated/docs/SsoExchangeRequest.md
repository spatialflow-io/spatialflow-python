# SsoExchangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**code_verifier** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from spatialflow_generated.models.sso_exchange_request import SsoExchangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SsoExchangeRequest from a JSON string
sso_exchange_request_instance = SsoExchangeRequest.from_json(json)
# print the JSON string representation of the object
print(SsoExchangeRequest.to_json())

# convert the object into a dict
sso_exchange_request_dict = sso_exchange_request_instance.to_dict()
# create an instance of SsoExchangeRequest from a dict
sso_exchange_request_from_dict = SsoExchangeRequest.from_dict(sso_exchange_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


