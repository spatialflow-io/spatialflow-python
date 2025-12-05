# WebhookTestResponse

Schema for webhook test response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**test_id** | **str** |  | 
**payload_sent** | **Dict[str, object]** |  | 
**message** | **str** |  | 
**response_status_code** | **int** |  | [optional] 
**response_time_ms** | **float** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.webhook_test_response import WebhookTestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTestResponse from a JSON string
webhook_test_response_instance = WebhookTestResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookTestResponse.to_json())

# convert the object into a dict
webhook_test_response_dict = webhook_test_response_instance.to_dict()
# create an instance of WebhookTestResponse from a dict
webhook_test_response_from_dict = WebhookTestResponse.from_dict(webhook_test_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


