# UserUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**email** | **str** |  | 
**workspace** | [**WorkspaceDetail**](WorkspaceDetail.md) |  | [optional] 
**api_usage** | [**APIUsageStats**](APIUsageStats.md) |  | 
**email_stats** | [**EmailStats**](EmailStats.md) |  | 
**geofence_stats** | [**GeofenceStats**](GeofenceStats.md) |  | 
**activity_summary** | [**List[ActivitySummary]**](ActivitySummary.md) |  | 
**recent_activities** | [**List[RecentActivity]**](RecentActivity.md) |  | 
**account_created** | **str** |  | 
**last_login** | **str** |  | 

## Example

```python
from spatialflow_generated.models.user_usage_response import UserUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserUsageResponse from a JSON string
user_usage_response_instance = UserUsageResponse.from_json(json)
# print the JSON string representation of the object
print(UserUsageResponse.to_json())

# convert the object into a dict
user_usage_response_dict = user_usage_response_instance.to_dict()
# create an instance of UserUsageResponse from a dict
user_usage_response_from_dict = UserUsageResponse.from_dict(user_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


