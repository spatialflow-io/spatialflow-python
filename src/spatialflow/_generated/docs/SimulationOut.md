# SimulationOut

Output schema for Simulation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**status** | **str** |  | 
**speed_multiplier** | **float** |  | 
**loop_enabled** | **bool** |  | 
**mute_external_actions** | **bool** |  | 
**progress_percent** | **float** |  | 
**total_events_triggered** | **int** |  | 
**route_count** | **int** |  | 
**created_at** | **str** |  | 
**started_at** | **str** |  | 
**paused_at** | **str** |  | 
**completed_at** | **str** |  | 
**error_message** | **str** |  | 

## Example

```python
from spatialflow_generated.models.simulation_out import SimulationOut

# TODO update the JSON string below
json = "{}"
# create an instance of SimulationOut from a JSON string
simulation_out_instance = SimulationOut.from_json(json)
# print the JSON string representation of the object
print(SimulationOut.to_json())

# convert the object into a dict
simulation_out_dict = simulation_out_instance.to_dict()
# create an instance of SimulationOut from a dict
simulation_out_from_dict = SimulationOut.from_dict(simulation_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


