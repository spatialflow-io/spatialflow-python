# UpdateProfileRequest

Update profile request schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**date_format** | **str** |  | [optional] 
**time_format** | **str** |  | [optional] 
**email_notifications** | **bool** |  | [optional] 
**webhook_failure_notifications** | **bool** |  | [optional] 
**workflow_failure_notifications** | **bool** |  | [optional] 
**usage_alert_notifications** | **bool** |  | [optional] 
**marketing_emails** | **bool** |  | [optional] 
**default_map_style** | **str** |  | [optional] 
**default_geofence_color** | **str** |  | [optional] 
**show_tutorial_tooltips** | **bool** |  | [optional] 
**default_api_version** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.update_profile_request import UpdateProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProfileRequest from a JSON string
update_profile_request_instance = UpdateProfileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProfileRequest.to_json())

# convert the object into a dict
update_profile_request_dict = update_profile_request_instance.to_dict()
# create an instance of UpdateProfileRequest from a dict
update_profile_request_from_dict = UpdateProfileRequest.from_dict(update_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


