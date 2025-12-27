# SimulationDetailOut

Detailed simulation output including routes and recent events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**simulation** | [**SimulationOut**](SimulationOut.md) |  | 
**routes** | [**List[SimulationRouteOut]**](SimulationRouteOut.md) |  | 
**recent_events** | [**List[SimulationEventOut]**](SimulationEventOut.md) |  | 

## Example

```python
from spatialflow_generated.models.simulation_detail_out import SimulationDetailOut

# TODO update the JSON string below
json = "{}"
# create an instance of SimulationDetailOut from a JSON string
simulation_detail_out_instance = SimulationDetailOut.from_json(json)
# print the JSON string representation of the object
print(SimulationDetailOut.to_json())

# convert the object into a dict
simulation_detail_out_dict = simulation_detail_out_instance.to_dict()
# create an instance of SimulationDetailOut from a dict
simulation_detail_out_from_dict = SimulationDetailOut.from_dict(simulation_detail_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


