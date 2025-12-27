# UserApiStats

Per-user API call statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**api_calls** | **int** |  | 

## Example

```python
from spatialflow_generated.models.user_api_stats import UserApiStats

# TODO update the JSON string below
json = "{}"
# create an instance of UserApiStats from a JSON string
user_api_stats_instance = UserApiStats.from_json(json)
# print the JSON string representation of the object
print(UserApiStats.to_json())

# convert the object into a dict
user_api_stats_dict = user_api_stats_instance.to_dict()
# create an instance of UserApiStats from a dict
user_api_stats_from_dict = UserApiStats.from_dict(user_api_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


