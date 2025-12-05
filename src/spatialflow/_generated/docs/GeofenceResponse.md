# GeofenceResponse

Schema for geofence response.  Supports all geometry types (PRD §3.1): - Polygon: Standard GeoJSON Polygon - MultiPolygon: Collection of polygons - Circle: Custom format with center and radius_meters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**geometry** | **Dict[str, object]** | GeoJSON geometry (Polygon, MultiPolygon, or Circle) | 
**geometry_type** | **str** | Logical geometry type: Polygon, MultiPolygon, or Circle | 
**radius_meters** | **float** |  | [optional] 
**webhook_url** | **str** |  | 
**webhook_events** | **List[str]** |  | 
**metadata** | **Dict[str, object]** |  | 
**is_active** | **bool** |  | 
**group_id** | **str** |  | 
**group_name** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.geofence_response import GeofenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceResponse from a JSON string
geofence_response_instance = GeofenceResponse.from_json(json)
# print the JSON string representation of the object
print(GeofenceResponse.to_json())

# convert the object into a dict
geofence_response_dict = geofence_response_instance.to_dict()
# create an instance of GeofenceResponse from a dict
geofence_response_from_dict = GeofenceResponse.from_dict(geofence_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


