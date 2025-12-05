# OAuthCallbackQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**state** | **str** |  | 
**error** | **str** |  | [optional] 
**error_description** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.o_auth_callback_query import OAuthCallbackQuery

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthCallbackQuery from a JSON string
o_auth_callback_query_instance = OAuthCallbackQuery.from_json(json)
# print the JSON string representation of the object
print(OAuthCallbackQuery.to_json())

# convert the object into a dict
o_auth_callback_query_dict = o_auth_callback_query_instance.to_dict()
# create an instance of OAuthCallbackQuery from a dict
o_auth_callback_query_from_dict = OAuthCallbackQuery.from_dict(o_auth_callback_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


