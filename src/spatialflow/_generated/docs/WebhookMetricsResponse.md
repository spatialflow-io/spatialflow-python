# WebhookMetricsResponse

Schema for webhook metrics (admin only)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **Dict[str, object]** |  | 
**cloudwatch_dashboard** | **Dict[str, str]** |  | 

## Example

```python
from spatialflow_generated.models.webhook_metrics_response import WebhookMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMetricsResponse from a JSON string
webhook_metrics_response_instance = WebhookMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookMetricsResponse.to_json())

# convert the object into a dict
webhook_metrics_response_dict = webhook_metrics_response_instance.to_dict()
# create an instance of WebhookMetricsResponse from a dict
webhook_metrics_response_from_dict = WebhookMetricsResponse.from_dict(webhook_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


