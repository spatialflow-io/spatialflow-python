# UserActivityResponse

Response for user activity timeline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**email** | **str** |  | 
**activities** | [**List[UserActivityItem]**](UserActivityItem.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from spatialflow_generated.models.user_activity_response import UserActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivityResponse from a JSON string
user_activity_response_instance = UserActivityResponse.from_json(json)
# print the JSON string representation of the object
print(UserActivityResponse.to_json())

# convert the object into a dict
user_activity_response_dict = user_activity_response_instance.to_dict()
# create an instance of UserActivityResponse from a dict
user_activity_response_from_dict = UserActivityResponse.from_dict(user_activity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


