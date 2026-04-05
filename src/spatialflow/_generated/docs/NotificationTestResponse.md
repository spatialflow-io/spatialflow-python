# NotificationTestResponse

Response for notification test endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**provider** | **str** |  | 
**message** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**response_time_ms** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.notification_test_response import NotificationTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTestResponse from a JSON string
notification_test_response_instance = NotificationTestResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationTestResponse.to_json())

# convert the object into a dict
notification_test_response_dict = notification_test_response_instance.to_dict()
# create an instance of NotificationTestResponse from a dict
notification_test_response_from_dict = NotificationTestResponse.from_dict(notification_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


