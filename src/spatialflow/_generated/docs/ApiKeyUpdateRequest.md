# ApiKeyUpdateRequest

API key update request schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**rate_limit_per_hour** | **int** |  | [optional] 

## Example

```python
from spatialflow_generated.models.api_key_update_request import ApiKeyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyUpdateRequest from a JSON string
api_key_update_request_instance = ApiKeyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiKeyUpdateRequest.to_json())

# convert the object into a dict
api_key_update_request_dict = api_key_update_request_instance.to_dict()
# create an instance of ApiKeyUpdateRequest from a dict
api_key_update_request_from_dict = ApiKeyUpdateRequest.from_dict(api_key_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


