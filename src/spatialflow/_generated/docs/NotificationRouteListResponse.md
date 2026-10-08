# NotificationRouteListResponse

Response for admin notification route list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routes** | [**List[NotificationRouteResponse]**](NotificationRouteResponse.md) |  | 
**supported_event_types** | **List[str]** |  | 
**slack_webhook_channel_bound** | **bool** |  | [optional] [default to True]

## Example

```python
from spatialflow_generated.models.notification_route_list_response import NotificationRouteListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRouteListResponse from a JSON string
notification_route_list_response_instance = NotificationRouteListResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationRouteListResponse.to_json())

# convert the object into a dict
notification_route_list_response_dict = notification_route_list_response_instance.to_dict()
# create an instance of NotificationRouteListResponse from a dict
notification_route_list_response_from_dict = NotificationRouteListResponse.from_dict(notification_route_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


