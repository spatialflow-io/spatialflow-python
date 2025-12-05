# ActionRetryConfigSchema

Complete retry configuration for an action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retry_policy** | [**RetryPolicySchema**](RetryPolicySchema.md) |  | [optional] 
**circuit_breaker** | [**CircuitBreakerSchema**](CircuitBreakerSchema.md) |  | [optional] 
**retry_policy_name** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.action_retry_config_schema import ActionRetryConfigSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRetryConfigSchema from a JSON string
action_retry_config_schema_instance = ActionRetryConfigSchema.from_json(json)
# print the JSON string representation of the object
print(ActionRetryConfigSchema.to_json())

# convert the object into a dict
action_retry_config_schema_dict = action_retry_config_schema_instance.to_dict()
# create an instance of ActionRetryConfigSchema from a dict
action_retry_config_schema_from_dict = ActionRetryConfigSchema.from_dict(action_retry_config_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


