# GeofenceGeometryOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | **Dict[str, object]** |  | [optional] 
**geometry_type** | **str** |  | [optional] 
**radius_meters** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.geofence_geometry_out import GeofenceGeometryOut

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceGeometryOut from a JSON string
geofence_geometry_out_instance = GeofenceGeometryOut.from_json(json)
# print the JSON string representation of the object
print(GeofenceGeometryOut.to_json())

# convert the object into a dict
geofence_geometry_out_dict = geofence_geometry_out_instance.to_dict()
# create an instance of GeofenceGeometryOut from a dict
geofence_geometry_out_from_dict = GeofenceGeometryOut.from_dict(geofence_geometry_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


