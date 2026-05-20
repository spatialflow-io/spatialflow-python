# GeofenceGroupUpdateOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**updated_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.geofence_group_update_out import GeofenceGroupUpdateOut

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceGroupUpdateOut from a JSON string
geofence_group_update_out_instance = GeofenceGroupUpdateOut.from_json(json)
# print the JSON string representation of the object
print(GeofenceGroupUpdateOut.to_json())

# convert the object into a dict
geofence_group_update_out_dict = geofence_group_update_out_instance.to_dict()
# create an instance of GeofenceGroupUpdateOut from a dict
geofence_group_update_out_from_dict = GeofenceGroupUpdateOut.from_dict(geofence_group_update_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


