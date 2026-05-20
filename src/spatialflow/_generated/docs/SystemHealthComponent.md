# SystemHealthComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**status** | **str** |  | 
**detail** | **str** |  | 
**value** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.system_health_component import SystemHealthComponent

# TODO update the JSON string below
json = "{}"
# create an instance of SystemHealthComponent from a JSON string
system_health_component_instance = SystemHealthComponent.from_json(json)
# print the JSON string representation of the object
print(SystemHealthComponent.to_json())

# convert the object into a dict
system_health_component_dict = system_health_component_instance.to_dict()
# create an instance of SystemHealthComponent from a dict
system_health_component_from_dict = SystemHealthComponent.from_dict(system_health_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


