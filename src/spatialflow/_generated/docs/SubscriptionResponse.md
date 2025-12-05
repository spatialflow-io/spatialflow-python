# SubscriptionResponse

User subscription details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**plan** | [**PlanResponse**](PlanResponse.md) |  | 
**status** | **str** | Subscription status (active/canceled/past_due) | 
**current_period_start** | **str** |  | [optional] 
**current_period_end** | **str** |  | [optional] 
**cancel_at_period_end** | **bool** |  | [optional] [default to False]
**created_at** | **str** | ISO 8601 datetime | 

## Example

```python
from spatialflow_generated.models.subscription_response import SubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponse from a JSON string
subscription_response_instance = SubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponse.to_json())

# convert the object into a dict
subscription_response_dict = subscription_response_instance.to_dict()
# create an instance of SubscriptionResponse from a dict
subscription_response_from_dict = SubscriptionResponse.from_dict(subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


