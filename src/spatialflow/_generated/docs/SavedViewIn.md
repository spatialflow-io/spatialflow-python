# SavedViewIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surface** | **str** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**is_shared** | **bool** |  | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.saved_view_in import SavedViewIn

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewIn from a JSON string
saved_view_in_instance = SavedViewIn.from_json(json)
# print the JSON string representation of the object
print(SavedViewIn.to_json())

# convert the object into a dict
saved_view_in_dict = saved_view_in_instance.to_dict()
# create an instance of SavedViewIn from a dict
saved_view_in_from_dict = SavedViewIn.from_dict(saved_view_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


