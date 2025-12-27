# CreateSimulationRequest

Request schema for creating a new simulation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] [default to '']
**speed_multiplier** | **float** |  | [optional] [default to 1.0]
**loop_enabled** | **bool** |  | [optional] [default to False]
**mute_external_actions** | **bool** |  | [optional] [default to True]

## Example

```python
from spatialflow_generated.models.create_simulation_request import CreateSimulationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSimulationRequest from a JSON string
create_simulation_request_instance = CreateSimulationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSimulationRequest.to_json())

# convert the object into a dict
create_simulation_request_dict = create_simulation_request_instance.to_dict()
# create an instance of CreateSimulationRequest from a dict
create_simulation_request_from_dict = CreateSimulationRequest.from_dict(create_simulation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


