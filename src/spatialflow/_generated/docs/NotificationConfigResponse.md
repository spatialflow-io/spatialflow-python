# NotificationConfigResponse

Response for notification configuration (supports Slack, Teams, Generic).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | 
**provider_name** | **str** |  | 
**webhook_url_placeholder** | **str** |  | 
**is_enabled** | **bool** |  | 
**webhook_url_configured** | **bool** |  | 
**notify_new_signups** | **bool** |  | 
**notify_admin_approvals** | **bool** |  | 
**notify_subscription_changes** | **bool** |  | 
**notify_payment_failures** | **bool** |  | 
**notify_privacy_erasures** | **bool** |  | 
**notify_dlq_threshold** | **bool** |  | 
**notify_service_health** | **bool** |  | 
**dlq_threshold** | **int** |  | 
**updated_at** | **str** |  | [optional] 
**updated_by_email** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.notification_config_response import NotificationConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationConfigResponse from a JSON string
notification_config_response_instance = NotificationConfigResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationConfigResponse.to_json())

# convert the object into a dict
notification_config_response_dict = notification_config_response_instance.to_dict()
# create an instance of NotificationConfigResponse from a dict
notification_config_response_from_dict = NotificationConfigResponse.from_dict(notification_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


