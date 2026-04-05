# GoogleTokenExchangeResponse


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
from spatialflow_generated.models.google_token_exchange_response import GoogleTokenExchangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleTokenExchangeResponse from a JSON string
google_token_exchange_response_instance = GoogleTokenExchangeResponse.from_json(json)
# print the JSON string representation of the object
print(GoogleTokenExchangeResponse.to_json())

# convert the object into a dict
google_token_exchange_response_dict = google_token_exchange_response_instance.to_dict()
# create an instance of GoogleTokenExchangeResponse from a dict
google_token_exchange_response_from_dict = GoogleTokenExchangeResponse.from_dict(google_token_exchange_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


