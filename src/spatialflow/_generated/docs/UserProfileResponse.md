# UserProfileResponse

User profile response schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**is_staff** | **bool** |  | [optional] [default to False]
**is_superuser** | **bool** |  | [optional] [default to False]
**email_verified** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**bio** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] [default to 'UTC']
**date_format** | **str** |  | [optional] [default to 'YYYY-MM-DD']
**time_format** | **str** |  | [optional] [default to '24h']
**email_notifications** | **bool** |  | [optional] [default to True]
**webhook_failure_notifications** | **bool** |  | [optional] [default to True]
**workflow_failure_notifications** | **bool** |  | [optional] [default to True]
**usage_alert_notifications** | **bool** |  | [optional] [default to True]
**marketing_emails** | **bool** |  | [optional] [default to False]
**default_map_style** | **str** |  | [optional] [default to 'streets']
**default_geofence_color** | **str** |  | [optional] [default to '#3B82F6']
**show_tutorial_tooltips** | **bool** |  | [optional] [default to True]
**default_api_version** | **str** |  | [optional] [default to 'v1']
**selected_plan** | **str** |  | [optional] [default to 'free']
**company** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.user_profile_response import UserProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfileResponse from a JSON string
user_profile_response_instance = UserProfileResponse.from_json(json)
# print the JSON string representation of the object
print(UserProfileResponse.to_json())

# convert the object into a dict
user_profile_response_dict = user_profile_response_instance.to_dict()
# create an instance of UserProfileResponse from a dict
user_profile_response_from_dict = UserProfileResponse.from_dict(user_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


