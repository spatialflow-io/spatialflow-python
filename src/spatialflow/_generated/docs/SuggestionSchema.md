# SuggestionSchema

A single autocomplete suggestion from the geocoder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**place_id** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.suggestion_schema import SuggestionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestionSchema from a JSON string
suggestion_schema_instance = SuggestionSchema.from_json(json)
# print the JSON string representation of the object
print(SuggestionSchema.to_json())

# convert the object into a dict
suggestion_schema_dict = suggestion_schema_instance.to_dict()
# create an instance of SuggestionSchema from a dict
suggestion_schema_from_dict = SuggestionSchema.from_dict(suggestion_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


