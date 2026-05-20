# SubscriptionInfo

Subscription details for workspace detail view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_name** | **str** |  | [optional] [default to 'free']
**status** | **str** |  | [optional] [default to 'none']
**billing_period** | **str** |  | [optional] 
**current_period_end** | **str** |  | [optional] 
**last_payment_amount** | **float** |  | [optional] 
**last_payment_date** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.subscription_info import SubscriptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionInfo from a JSON string
subscription_info_instance = SubscriptionInfo.from_json(json)
# print the JSON string representation of the object
print(SubscriptionInfo.to_json())

# convert the object into a dict
subscription_info_dict = subscription_info_instance.to_dict()
# create an instance of SubscriptionInfo from a dict
subscription_info_from_dict = SubscriptionInfo.from_dict(subscription_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


