# CircuitBreakerSchema

Circuit breaker configuration schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**failure_threshold** | **int** |  | [optional] [default to 5]
**recovery_timeout_ms** | **int** |  | [optional] [default to 60000]
**success_threshold** | **int** |  | [optional] [default to 2]

## Example

```python
from spatialflow_generated.models.circuit_breaker_schema import CircuitBreakerSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CircuitBreakerSchema from a JSON string
circuit_breaker_schema_instance = CircuitBreakerSchema.from_json(json)
# print the JSON string representation of the object
print(CircuitBreakerSchema.to_json())

# convert the object into a dict
circuit_breaker_schema_dict = circuit_breaker_schema_instance.to_dict()
# create an instance of CircuitBreakerSchema from a dict
circuit_breaker_schema_from_dict = CircuitBreakerSchema.from_dict(circuit_breaker_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


