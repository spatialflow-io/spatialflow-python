# EmailTestResponse

Response for email test endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | [optional] 
**recipient** | **str** |  | [optional] 
**config** | [**EmailConfigInfo**](EmailConfigInfo.md) |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.email_test_response import EmailTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTestResponse from a JSON string
email_test_response_instance = EmailTestResponse.from_json(json)
# print the JSON string representation of the object
print(EmailTestResponse.to_json())

# convert the object into a dict
email_test_response_dict = email_test_response_instance.to_dict()
# create an instance of EmailTestResponse from a dict
email_test_response_from_dict = EmailTestResponse.from_dict(email_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


