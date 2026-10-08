# GeofenceResponse

Schema for geofence response.  Supports all geometry types: - Polygon: Standard GeoJSON Polygon - MultiPolygon: Collection of polygons - Circle: Custom format with center and radius_meters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**geometry** | [**Geometry**](Geometry.md) |  | 
**geometry_type** | **str** | Logical geometry type: Polygon, MultiPolygon, or Circle | 
**radius_meters** | **float** |  | [optional] 
**webhook_url** | **str** |  | 
**webhook_events** | **List[str]** |  | 
**metadata** | **Dict[str, object]** |  | 
**is_active** | **bool** |  | 
**group_id** | **str** |  | 
**group_name** | **str** |  | 
**source** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**buffer_meters** | **int** |  | [optional] 
**archived** | **bool** | Whether the geofence is archived (hidden from default list and map). | [optional] [default to False]
**point** | **List[float]** |  | [optional] 
**tags** | **List[str]** | Names of tags attached to this geofence (case as originally entered). | [optional] 
**source_id** | **str** |  | [optional] 
**pre_upgrade_geometry** | **Dict[str, object]** |  | [optional] 
**building_provenance** | **Dict[str, object]** |  | [optional] 
**effective_radius_meters** | **float** |  | [optional] 
**below_min_trigger_radius** | **bool** | True iff effective_radius_meters is strictly less than MIN_TRIGGER_RADIUS_METERS (50m). When True, the geofence fires within ~50m of the center. Non-blocking — the client should show a reassuring informational warning, not block Save. | [optional] [default to False]
**is_example** | **bool** |  | [optional] [default to False]
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


