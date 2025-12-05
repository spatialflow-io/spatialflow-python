# WebhookDeliveryResponse

Schema for webhook delivery response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**webhook_id** | **str** |  | 
**geofence_id** | **str** |  | 
**event_type** | **str** |  | 
**event_id** | **str** |  | 
**url** | **str** |  | 
**method** | **str** |  | 
**status** | [**DeliveryStatusEnum**](DeliveryStatusEnum.md) |  | 
**response_status_code** | **int** |  | 
**response_status** | **int** |  | [optional] 
**response_time_ms** | **float** |  | 
**error_message** | **str** |  | 
**attempt_count** | **int** |  | 
**retry_count** | **int** |  | [optional] [default to 0]
**created_at** | **datetime** |  | 
**delivered_at** | **datetime** |  | 
**next_retry_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.webhook_delivery_response import WebhookDeliveryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryResponse from a JSON string
webhook_delivery_response_instance = WebhookDeliveryResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryResponse.to_json())

# convert the object into a dict
webhook_delivery_response_dict = webhook_delivery_response_instance.to_dict()
# create an instance of WebhookDeliveryResponse from a dict
webhook_delivery_response_from_dict = WebhookDeliveryResponse.from_dict(webhook_delivery_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


