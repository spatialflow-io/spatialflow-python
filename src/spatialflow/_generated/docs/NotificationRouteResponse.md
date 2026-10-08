# NotificationRouteResponse

Response for one admin notification route.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**provider** | **str** |  | 
**provider_name** | **str** |  | 
**destination_label** | **str** |  | 
**webhook_url_configured** | **bool** |  | 
**event_types** | **List[str]** |  | 
**is_enabled** | **bool** |  | 
**is_default** | **bool** |  | 
**last_tested_at** | **datetime** |  | [optional] 
**last_success_at** | **datetime** |  | [optional] 
**last_failure_at** | **datetime** |  | [optional] 
**last_error** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_by_email** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.notification_route_response import NotificationRouteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRouteResponse from a JSON string
notification_route_response_instance = NotificationRouteResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationRouteResponse.to_json())

# convert the object into a dict
notification_route_response_dict = notification_route_response_instance.to_dict()
# create an instance of NotificationRouteResponse from a dict
notification_route_response_from_dict = NotificationRouteResponse.from_dict(notification_route_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


