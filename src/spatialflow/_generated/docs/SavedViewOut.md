# SavedViewOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**workspace_id** | **str** |  | 
**user_id** | **str** |  | 
**surface** | **str** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**is_shared** | **bool** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.saved_view_out import SavedViewOut

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewOut from a JSON string
saved_view_out_instance = SavedViewOut.from_json(json)
# print the JSON string representation of the object
print(SavedViewOut.to_json())

# convert the object into a dict
saved_view_out_dict = saved_view_out_instance.to_dict()
# create an instance of SavedViewOut from a dict
saved_view_out_from_dict = SavedViewOut.from_dict(saved_view_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


