# SystemHealthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**checked_at** | **str** |  | 
**environment** | **str** |  | 
**version** | **str** |  | 
**components** | [**Dict[str, SystemHealthComponent]**](SystemHealthComponent.md) |  | 

## Example

```python
from spatialflow_generated.models.system_health_response import SystemHealthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemHealthResponse from a JSON string
system_health_response_instance = SystemHealthResponse.from_json(json)
# print the JSON string representation of the object
print(SystemHealthResponse.to_json())

# convert the object into a dict
system_health_response_dict = system_health_response_instance.to_dict()
# create an instance of SystemHealthResponse from a dict
system_health_response_from_dict = SystemHealthResponse.from_dict(system_health_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


