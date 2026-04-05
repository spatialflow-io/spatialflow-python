# GoogleTokenExchangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_token** | **str** |  | 

## Example

```python
from spatialflow_generated.models.google_token_exchange_request import GoogleTokenExchangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleTokenExchangeRequest from a JSON string
google_token_exchange_request_instance = GoogleTokenExchangeRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleTokenExchangeRequest.to_json())

# convert the object into a dict
google_token_exchange_request_dict = google_token_exchange_request_instance.to_dict()
# create an instance of GoogleTokenExchangeRequest from a dict
google_token_exchange_request_from_dict = GoogleTokenExchangeRequest.from_dict(google_token_exchange_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


