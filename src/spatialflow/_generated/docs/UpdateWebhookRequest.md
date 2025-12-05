# UpdateWebhookRequest

Schema for updating an existing webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**events** | **List[str]** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**auth_type** | [**AuthTypeEnum**](AuthTypeEnum.md) |  | [optional] 
**auth_config** | **Dict[str, object]** |  | [optional] 
**method** | [**MethodEnum**](MethodEnum.md) |  | [optional] 
**content_type** | **str** |  | [optional] 
**custom_payload_template** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**max_retries** | **int** |  | [optional] 
**timeout_seconds** | **int** |  | [optional] 
**rate_limit_per_minute** | **int** |  | [optional] 

## Example

```python
from spatialflow_generated.models.update_webhook_request import UpdateWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookRequest from a JSON string
update_webhook_request_instance = UpdateWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookRequest.to_json())

# convert the object into a dict
update_webhook_request_dict = update_webhook_request_instance.to_dict()
# create an instance of UpdateWebhookRequest from a dict
update_webhook_request_from_dict = UpdateWebhookRequest.from_dict(update_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


