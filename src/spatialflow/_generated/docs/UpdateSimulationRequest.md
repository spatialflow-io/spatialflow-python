# UpdateSimulationRequest

Request schema for updating simulation settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**speed_multiplier** | **float** |  | [optional] 
**loop_enabled** | **bool** |  | [optional] 
**mute_external_actions** | **bool** |  | [optional] 

## Example

```python
from spatialflow_generated.models.update_simulation_request import UpdateSimulationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSimulationRequest from a JSON string
update_simulation_request_instance = UpdateSimulationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSimulationRequest.to_json())

# convert the object into a dict
update_simulation_request_dict = update_simulation_request_instance.to_dict()
# create an instance of UpdateSimulationRequest from a dict
update_simulation_request_from_dict = UpdateSimulationRequest.from_dict(update_simulation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


