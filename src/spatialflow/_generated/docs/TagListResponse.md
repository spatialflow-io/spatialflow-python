# TagListResponse

Response for GET /api/v1/geofences/tags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[TagSchema]**](TagSchema.md) |  | 
**total** | **int** |  | 
**truncated** | **bool** | True if the workspace has more than the cap (500) tags and the list was truncated. | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.tag_list_response import TagListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TagListResponse from a JSON string
tag_list_response_instance = TagListResponse.from_json(json)
# print the JSON string representation of the object
print(TagListResponse.to_json())

# convert the object into a dict
tag_list_response_dict = tag_list_response_instance.to_dict()
# create an instance of TagListResponse from a dict
tag_list_response_from_dict = TagListResponse.from_dict(tag_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


