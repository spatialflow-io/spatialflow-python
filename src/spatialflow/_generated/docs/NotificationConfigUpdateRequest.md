# NotificationConfigUpdateRequest

Request to update notification configuration.  Provider switching rules: - If provider changes and webhook_url is not provided, the existing webhook_url is cleared - webhook_url must match the pattern for the target provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**notify_new_signups** | **bool** |  | [optional] 
**notify_admin_approvals** | **bool** |  | [optional] 
**notify_subscription_changes** | **bool** |  | [optional] 
**notify_payment_failures** | **bool** |  | [optional] 
**notify_privacy_erasures** | **bool** |  | [optional] 
**notify_dlq_threshold** | **bool** |  | [optional] 
**notify_service_health** | **bool** |  | [optional] 
**dlq_threshold** | **int** |  | [optional] 

## Example

```python
from spatialflow_generated.models.notification_config_update_request import NotificationConfigUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationConfigUpdateRequest from a JSON string
notification_config_update_request_instance = NotificationConfigUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationConfigUpdateRequest.to_json())

# convert the object into a dict
notification_config_update_request_dict = notification_config_update_request_instance.to_dict()
# create an instance of NotificationConfigUpdateRequest from a dict
notification_config_update_request_from_dict = NotificationConfigUpdateRequest.from_dict(notification_config_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


