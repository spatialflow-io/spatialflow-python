# CreateWebhookRequest

Schema for creating a new webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**url** | **str** |  | 
**events** | **List[str]** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**auth_type** | [**AuthTypeEnum**](AuthTypeEnum.md) |  | [optional] 
**auth_config** | **Dict[str, object]** |  | [optional] 
**method** | [**MethodEnum**](MethodEnum.md) |  | [optional] 
**content_type** | **str** |  | [optional] [default to 'application/json']
**custom_payload_template** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**max_retries** | **int** |  | [optional] [default to 3]
**timeout_seconds** | **int** |  | [optional] [default to 30]
**rate_limit_per_minute** | **int** |  | [optional] [default to 60]

## Example

```python
from spatialflow_generated.models.create_webhook_request import CreateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookRequest from a JSON string
create_webhook_request_instance = CreateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookRequest.to_json())

# convert the object into a dict
create_webhook_request_dict = create_webhook_request_instance.to_dict()
# create an instance of CreateWebhookRequest from a dict
create_webhook_request_from_dict = CreateWebhookRequest.from_dict(create_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


