# NotificationRouteRequest

Create or update a notification route.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**provider** | **str** |  | [optional] [default to 'slack']
**destination_label** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**event_types** | **List[str]** |  | [optional] [default to []]
**is_enabled** | **bool** |  | [optional] [default to True]
**is_default** | **bool** |  | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.notification_route_request import NotificationRouteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRouteRequest from a JSON string
notification_route_request_instance = NotificationRouteRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationRouteRequest.to_json())

# convert the object into a dict
notification_route_request_dict = notification_route_request_instance.to_dict()
# create an instance of NotificationRouteRequest from a dict
notification_route_request_from_dict = NotificationRouteRequest.from_dict(notification_route_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


