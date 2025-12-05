# UpdateGeofenceRequest

Schema for updating an existing geofence.  Supports three geometry types (PRD §3.1): - Polygon: Standard GeoJSON Polygon - MultiPolygon: Collection of polygons - Circle: Point with radius_meters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**geometry** | **Dict[str, object]** |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**webhook_events** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**group_name** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.update_geofence_request import UpdateGeofenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGeofenceRequest from a JSON string
update_geofence_request_instance = UpdateGeofenceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGeofenceRequest.to_json())

# convert the object into a dict
update_geofence_request_dict = update_geofence_request_instance.to_dict()
# create an instance of UpdateGeofenceRequest from a dict
update_geofence_request_from_dict = UpdateGeofenceRequest.from_dict(update_geofence_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


