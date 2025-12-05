# WebhookDeliveryListResponse

Schema for webhook delivery list response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliveries** | [**List[WebhookDeliveryResponse]**](WebhookDeliveryResponse.md) |  | 
**pagination** | **Dict[str, object]** |  | 

## Example

```python
from spatialflow_generated.models.webhook_delivery_list_response import WebhookDeliveryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeliveryListResponse from a JSON string
webhook_delivery_list_response_instance = WebhookDeliveryListResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookDeliveryListResponse.to_json())

# convert the object into a dict
webhook_delivery_list_response_dict = webhook_delivery_list_response_instance.to_dict()
# create an instance of WebhookDeliveryListResponse from a dict
webhook_delivery_list_response_from_dict = WebhookDeliveryListResponse.from_dict(webhook_delivery_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


