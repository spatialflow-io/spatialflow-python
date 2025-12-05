# GPXRouteOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**device_id** | **str** |  | 
**device_name** | **str** |  | 
**total_points** | **int** |  | 
**total_distance_km** | **float** |  | 
**total_duration_seconds** | **float** |  | 
**start_time** | **str** |  | 
**end_time** | **str** |  | 
**is_active** | **bool** |  | 
**created_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.gpx_route_out import GPXRouteOut

# TODO update the JSON string below
json = "{}"
# create an instance of GPXRouteOut from a JSON string
gpx_route_out_instance = GPXRouteOut.from_json(json)
# print the JSON string representation of the object
print(GPXRouteOut.to_json())

# convert the object into a dict
gpx_route_out_dict = gpx_route_out_instance.to_dict()
# create an instance of GPXRouteOut from a dict
gpx_route_out_from_dict = GPXRouteOut.from_dict(gpx_route_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


