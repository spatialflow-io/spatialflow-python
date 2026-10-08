# TagSchema

Workspace tag with usage count.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**normalized_name** | **str** |  | 
**usage_count** | **int** | Count of geofences in the workspace carrying this tag. | [optional] [default to 0]

## Example

```python
from spatialflow_generated.models.tag_schema import TagSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TagSchema from a JSON string
tag_schema_instance = TagSchema.from_json(json)
# print the JSON string representation of the object
print(TagSchema.to_json())

# convert the object into a dict
tag_schema_dict = tag_schema_instance.to_dict()
# create an instance of TagSchema from a dict
tag_schema_from_dict = TagSchema.from_dict(tag_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


