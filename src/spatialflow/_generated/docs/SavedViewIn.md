# SavedViewIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**surface** | **str** |  | 
**name** | **str** |  | 
**url** | **str** | A path on this site with an optional query and fragment, such as /events?severity&#x3D;critical. Path segments are never empty or start with a dot, the path has no encoded dot, slash or backslash, and the URL has no backslash or control characters. | 
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


