# SimulationRouteOut

Output schema for SimulationRoute model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**simulation_id** | **str** |  | 
**gpx_route_id** | **str** |  | 
**gpx_route_name** | **str** |  | 
**simulated_device_name** | **str** |  | 
**simulated_device_type** | **str** |  | 
**status** | **str** |  | 
**current_point_index** | **int** |  | 
**total_points** | **int** |  | 
**progress_percent** | **float** |  | 
**events_triggered** | **int** |  | 
**created_at** | **str** |  | 
**started_at** | **str** |  | 
**paused_at** | **str** |  | 
**completed_at** | **str** |  | 
**error_message** | **str** |  | 

## Example

```python
from spatialflow_generated.models.simulation_route_out import SimulationRouteOut

# TODO update the JSON string below
json = "{}"
# create an instance of SimulationRouteOut from a JSON string
simulation_route_out_instance = SimulationRouteOut.from_json(json)
# print the JSON string representation of the object
print(SimulationRouteOut.to_json())

# convert the object into a dict
simulation_route_out_dict = simulation_route_out_instance.to_dict()
# create an instance of SimulationRouteOut from a dict
simulation_route_out_from_dict = SimulationRouteOut.from_dict(simulation_route_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


