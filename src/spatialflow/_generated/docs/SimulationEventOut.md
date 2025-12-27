# SimulationEventOut

Output schema for SimulationEvent model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**event_type** | **str** |  | 
**geofence_name** | **str** |  | 
**workflow_name** | **str** |  | 
**action_type** | **str** |  | 
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**details** | **Dict[str, object]** |  | 
**dwell_duration_seconds** | **float** |  | [optional] 
**timestamp** | **str** |  | 

## Example

```python
from spatialflow_generated.models.simulation_event_out import SimulationEventOut

# TODO update the JSON string below
json = "{}"
# create an instance of SimulationEventOut from a JSON string
simulation_event_out_instance = SimulationEventOut.from_json(json)
# print the JSON string representation of the object
print(SimulationEventOut.to_json())

# convert the object into a dict
simulation_event_out_dict = simulation_event_out_instance.to_dict()
# create an instance of SimulationEventOut from a dict
simulation_event_out_from_dict = SimulationEventOut.from_dict(simulation_event_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


