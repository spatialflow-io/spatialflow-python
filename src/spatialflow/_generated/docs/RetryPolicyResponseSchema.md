# RetryPolicyResponseSchema

Response schema for retry policy information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_policies** | **Dict[str, Optional[Dict[str, object]]]** |  | 
**retry_strategies** | **List[str]** |  | 
**circuit_breaker_defaults** | [**CircuitBreakerSchema**](CircuitBreakerSchema.md) |  | 

## Example

```python
from spatialflow_generated.models.retry_policy_response_schema import RetryPolicyResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RetryPolicyResponseSchema from a JSON string
retry_policy_response_schema_instance = RetryPolicyResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RetryPolicyResponseSchema.to_json())

# convert the object into a dict
retry_policy_response_schema_dict = retry_policy_response_schema_instance.to_dict()
# create an instance of RetryPolicyResponseSchema from a dict
retry_policy_response_schema_from_dict = RetryPolicyResponseSchema.from_dict(retry_policy_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


