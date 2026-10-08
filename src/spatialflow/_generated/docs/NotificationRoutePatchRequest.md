# NotificationRoutePatchRequest

Partial update for a notification route.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**destination_label** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**event_types** | **List[str]** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from spatialflow_generated.models.notification_route_patch_request import NotificationRoutePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRoutePatchRequest from a JSON string
notification_route_patch_request_instance = NotificationRoutePatchRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationRoutePatchRequest.to_json())

# convert the object into a dict
notification_route_patch_request_dict = notification_route_patch_request_instance.to_dict()
# create an instance of NotificationRoutePatchRequest from a dict
notification_route_patch_request_from_dict = NotificationRoutePatchRequest.from_dict(notification_route_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


