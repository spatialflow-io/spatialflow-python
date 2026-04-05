# CategoryInfo

Category metadata for grouping configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**order** | **int** |  | 

## Example

```python
from spatialflow_generated.models.category_info import CategoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryInfo from a JSON string
category_info_instance = CategoryInfo.from_json(json)
# print the JSON string representation of the object
print(CategoryInfo.to_json())

# convert the object into a dict
category_info_dict = category_info_instance.to_dict()
# create an instance of CategoryInfo from a dict
category_info_from_dict = CategoryInfo.from_dict(category_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


