# WebhookIngressErrorResponse

Ingress error with legacy fields retained for existing webhook clients.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**error_code** | **str** |  | [optional] 
**details** | **Dict[str, object]** |  | [optional] 
**success** | **bool** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.webhook_ingress_error_response import WebhookIngressErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIngressErrorResponse from a JSON string
webhook_ingress_error_response_instance = WebhookIngressErrorResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookIngressErrorResponse.to_json())

# convert the object into a dict
webhook_ingress_error_response_dict = webhook_ingress_error_response_instance.to_dict()
# create an instance of WebhookIngressErrorResponse from a dict
webhook_ingress_error_response_from_dict = WebhookIngressErrorResponse.from_dict(webhook_ingress_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


