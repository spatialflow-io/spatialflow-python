# UserActivityItem

Single activity entry for a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** |  | 
**resource_type** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**created_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.user_activity_item import UserActivityItem

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivityItem from a JSON string
user_activity_item_instance = UserActivityItem.from_json(json)
# print the JSON string representation of the object
print(UserActivityItem.to_json())

# convert the object into a dict
user_activity_item_dict = user_activity_item_instance.to_dict()
# create an instance of UserActivityItem from a dict
user_activity_item_from_dict = UserActivityItem.from_dict(user_activity_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


