# SubscriptionUsageResponse

Usage metrics with limits.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**period_start** | **str** | ISO 8601 datetime | 
**period_end** | **str** | ISO 8601 datetime | 
**usage** | [**UsageMetrics**](UsageMetrics.md) |  | 
**limits** | [**PlanLimits**](PlanLimits.md) |  | 
**plan_name** | **str** |  | 
**throttle_status** | **str** | Current throttle status: ok, warning, alert, throttled, blocked | [optional] [default to 'ok']
**is_first_billing_month** | **bool** | Whether workspace is in its first billing month | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.subscription_usage_response import SubscriptionUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionUsageResponse from a JSON string
subscription_usage_response_instance = SubscriptionUsageResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionUsageResponse.to_json())

# convert the object into a dict
subscription_usage_response_dict = subscription_usage_response_instance.to_dict()
# create an instance of SubscriptionUsageResponse from a dict
subscription_usage_response_from_dict = SubscriptionUsageResponse.from_dict(subscription_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


