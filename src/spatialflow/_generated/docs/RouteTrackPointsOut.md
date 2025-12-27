# RouteTrackPointsOut

Route with track points for map visualization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_id** | **str** |  | 
**simulated_device_name** | **str** |  | 
**track_points** | [**List[TrackPointOut]**](TrackPointOut.md) |  | 

## Example

```python
from spatialflow_generated.models.route_track_points_out import RouteTrackPointsOut

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTrackPointsOut from a JSON string
route_track_points_out_instance = RouteTrackPointsOut.from_json(json)
# print the JSON string representation of the object
print(RouteTrackPointsOut.to_json())

# convert the object into a dict
route_track_points_out_dict = route_track_points_out_instance.to_dict()
# create an instance of RouteTrackPointsOut from a dict
route_track_points_out_from_dict = RouteTrackPointsOut.from_dict(route_track_points_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


