# CreateGeofenceRequest

Schema for creating a new geofence.  Supports three geometry types (PRD §3.1): - Polygon: Standard GeoJSON Polygon - MultiPolygon: Collection of polygons - Circle: Point with radius_meters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**geometry** | **Dict[str, object]** | GeoJSON geometry (Polygon, MultiPolygon, or Circle) | 
**webhook_url** | **str** |  | [optional] 
**webhook_events** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**group_name** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.create_geofence_request import CreateGeofenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGeofenceRequest from a JSON string
create_geofence_request_instance = CreateGeofenceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGeofenceRequest.to_json())

# convert the object into a dict
create_geofence_request_dict = create_geofence_request_instance.to_dict()
# create an instance of CreateGeofenceRequest from a dict
create_geofence_request_from_dict = CreateGeofenceRequest.from_dict(create_geofence_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


