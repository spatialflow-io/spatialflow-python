# PlanResponse

Subscription plan details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**price** | **float** |  | 
**interval** | **str** | Billing interval (month/year) | 
**features** | [**PlanFeatures**](PlanFeatures.md) |  | 
**limits** | [**PlanLimits**](PlanLimits.md) |  | 
**stripe_price_id** | **str** |  | [optional] 
**tier** | **str** | Lowercase plan name (e.g., &#39;free&#39;, &#39;pro&#39;) | [optional] [default to '']
**display_name** | **str** | Human-readable plan name | [optional] [default to '']
**price_monthly** | **float** | Monthly price in dollars | [optional] [default to 0]
**price_yearly** | **float** | Yearly price in dollars | [optional] [default to 0]
**stripe_price_monthly_id** | **str** |  | [optional] 
**stripe_price_yearly_id** | **str** |  | [optional] 
**event_overage_rate** | **float** | Price per extra 100k events | [optional] [default to 0]
**geofence_overage_rate** | **float** | Price per extra 100 geofences | [optional] [default to 0]
**is_featured** | **bool** | Whether this plan is featured/recommended | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.plan_response import PlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanResponse from a JSON string
plan_response_instance = PlanResponse.from_json(json)
# print the JSON string representation of the object
print(PlanResponse.to_json())

# convert the object into a dict
plan_response_dict = plan_response_instance.to_dict()
# create an instance of PlanResponse from a dict
plan_response_from_dict = PlanResponse.from_dict(plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


