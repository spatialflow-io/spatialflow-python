# RouteUploadResponse

Response for route upload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route** | [**SimulationRouteOut**](SimulationRouteOut.md) |  | 
**gpx_route_id** | **str** |  | 
**total_points** | **int** |  | 
**total_distance_km** | **float** |  | 
**total_duration_seconds** | **float** |  | 

## Example

```python
from spatialflow_generated.models.route_upload_response import RouteUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteUploadResponse from a JSON string
route_upload_response_instance = RouteUploadResponse.from_json(json)
# print the JSON string representation of the object
print(RouteUploadResponse.to_json())

# convert the object into a dict
route_upload_response_dict = route_upload_response_instance.to_dict()
# create an instance of RouteUploadResponse from a dict
route_upload_response_from_dict = RouteUploadResponse.from_dict(route_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


