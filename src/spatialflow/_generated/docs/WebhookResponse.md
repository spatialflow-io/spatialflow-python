# WebhookResponse

Schema for webhook response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**url** | **str** |  | 
**events** | **List[str]** |  | 
**headers** | **Dict[str, str]** |  | 
**auth_type** | **str** |  | 
**method** | **str** |  | 
**content_type** | **str** |  | 
**custom_payload_template** | **str** |  | 
**is_active** | **bool** |  | 
**max_retries** | **int** |  | 
**timeout_seconds** | **int** |  | 
**rate_limit_per_minute** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**last_triggered_at** | **datetime** |  | 
**total_deliveries** | **int** |  | 
**successful_deliveries** | **int** |  | 
**failed_deliveries** | **int** |  | 
**success_rate** | **float** |  | 

## Example

```python
from spatialflow_generated.models.webhook_response import WebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookResponse from a JSON string
webhook_response_instance = WebhookResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookResponse.to_json())

# convert the object into a dict
webhook_response_dict = webhook_response_instance.to_dict()
# create an instance of WebhookResponse from a dict
webhook_response_from_dict = WebhookResponse.from_dict(webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


