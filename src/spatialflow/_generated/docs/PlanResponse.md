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


