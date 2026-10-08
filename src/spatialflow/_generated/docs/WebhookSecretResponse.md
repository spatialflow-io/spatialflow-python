# WebhookSecretResponse

A webhook plus its signing secret.  Only create and rotate-secret return this; list, get and update never include the secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**url** | **str** |  | 
**events** | **List[str]** |  | 
**headers** | **Dict[str, str]** |  | 
**sensitive_headers_configured** | **List[str]** |  | [optional] 
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
**attached_geofence_count** | **int** |  | [optional] [default to 0]
**secret** | **str** | HMAC-SHA256 key that signs every delivery&#39;s X-SF-Signature header. Shown only in this response; store it now, or rotate the secret to get a new one. | 

## Example

```python
from spatialflow_generated.models.webhook_secret_response import WebhookSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecretResponse from a JSON string
webhook_secret_response_instance = WebhookSecretResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookSecretResponse.to_json())

# convert the object into a dict
webhook_secret_response_dict = webhook_secret_response_instance.to_dict()
# create an instance of WebhookSecretResponse from a dict
webhook_secret_response_from_dict = WebhookSecretResponse.from_dict(webhook_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


