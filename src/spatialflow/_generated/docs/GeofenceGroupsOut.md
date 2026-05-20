# GeofenceGroupsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[GeofenceGroupItemOut]**](GeofenceGroupItemOut.md) |  | 
**count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.geofence_groups_out import GeofenceGroupsOut

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceGroupsOut from a JSON string
geofence_groups_out_instance = GeofenceGroupsOut.from_json(json)
# print the JSON string representation of the object
print(GeofenceGroupsOut.to_json())

# convert the object into a dict
geofence_groups_out_dict = geofence_groups_out_instance.to_dict()
# create an instance of GeofenceGroupsOut from a dict
geofence_groups_out_from_dict = GeofenceGroupsOut.from_dict(geofence_groups_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


