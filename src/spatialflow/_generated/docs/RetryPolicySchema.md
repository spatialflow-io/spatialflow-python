# RetryPolicySchema

Retry policy configuration schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**max_attempts** | **int** |  | [optional] [default to 3]
**strategy** | [**RetryStrategyEnum**](RetryStrategyEnum.md) |  | [optional] 
**base_delay_ms** | **int** |  | [optional] [default to 1000]
**max_delay_ms** | **int** |  | [optional] [default to 30000]
**jitter** | **bool** |  | [optional] [default to True]

## Example

```python
from spatialflow_generated.models.retry_policy_schema import RetryPolicySchema

# TODO update the JSON string below
json = "{}"
# create an instance of RetryPolicySchema from a JSON string
retry_policy_schema_instance = RetryPolicySchema.from_json(json)
# print the JSON string representation of the object
print(RetryPolicySchema.to_json())

# convert the object into a dict
retry_policy_schema_dict = retry_policy_schema_instance.to_dict()
# create an instance of RetryPolicySchema from a dict
retry_policy_schema_from_dict = RetryPolicySchema.from_dict(retry_policy_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


