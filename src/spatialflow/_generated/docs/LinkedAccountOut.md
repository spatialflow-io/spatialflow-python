# LinkedAccountOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**display_name** | **str** |  | 
**linked_at** | **datetime** |  | 
**avatar_url** | **str** |  | [optional] 
**profile_url** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.linked_account_out import LinkedAccountOut

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedAccountOut from a JSON string
linked_account_out_instance = LinkedAccountOut.from_json(json)
# print the JSON string representation of the object
print(LinkedAccountOut.to_json())

# convert the object into a dict
linked_account_out_dict = linked_account_out_instance.to_dict()
# create an instance of LinkedAccountOut from a dict
linked_account_out_from_dict = LinkedAccountOut.from_dict(linked_account_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


