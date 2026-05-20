# HealthOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**service** | **str** |  | 
**timestamp** | **str** |  | 
**checks** | [**HealthChecksOut**](HealthChecksOut.md) |  | 

## Example

```python
from spatialflow_generated.models.health_out import HealthOut

# TODO update the JSON string below
json = "{}"
# create an instance of HealthOut from a JSON string
health_out_instance = HealthOut.from_json(json)
# print the JSON string representation of the object
print(HealthOut.to_json())

# convert the object into a dict
health_out_dict = health_out_instance.to_dict()
# create an instance of HealthOut from a dict
health_out_from_dict = HealthOut.from_dict(health_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


