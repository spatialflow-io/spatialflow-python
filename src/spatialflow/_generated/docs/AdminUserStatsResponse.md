# AdminUserStatsResponse

Response for admin user stats endpoint.  Returns aggregated API call counts per user within a date range. Default: last 30 days, max 90 days. Max 100 results per page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserApiStats]**](UserApiStats.md) |  | 
**total** | **int** |  | 
**days** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 
**has_more** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.admin_user_stats_response import AdminUserStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserStatsResponse from a JSON string
admin_user_stats_response_instance = AdminUserStatsResponse.from_json(json)
# print the JSON string representation of the object
print(AdminUserStatsResponse.to_json())

# convert the object into a dict
admin_user_stats_response_dict = admin_user_stats_response_instance.to_dict()
# create an instance of AdminUserStatsResponse from a dict
admin_user_stats_response_from_dict = AdminUserStatsResponse.from_dict(admin_user_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


