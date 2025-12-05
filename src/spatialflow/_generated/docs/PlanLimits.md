# PlanLimits

Usage limits for a subscription plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_calls** | **int** | Monthly API call limit (-1 for unlimited) | 
**geofences** | **int** | Maximum number of geofences (-1 for unlimited) | 
**webhooks_delivered** | **int** | Monthly webhook delivery limit (-1 for unlimited) | 
**test_points** | **int** | Monthly test point limit (-1 for unlimited) | 
**rate_limit_per_hour** | **int** | Hourly rate limit | 

## Example

```python
from spatialflow_generated.models.plan_limits import PlanLimits

# TODO update the JSON string below
json = "{}"
# create an instance of PlanLimits from a JSON string
plan_limits_instance = PlanLimits.from_json(json)
# print the JSON string representation of the object
print(PlanLimits.to_json())

# convert the object into a dict
plan_limits_dict = plan_limits_instance.to_dict()
# create an instance of PlanLimits from a dict
plan_limits_from_dict = PlanLimits.from_dict(plan_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


