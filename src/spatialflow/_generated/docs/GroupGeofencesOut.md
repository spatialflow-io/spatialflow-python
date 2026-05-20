# GroupGeofencesOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geofences** | [**List[GroupGeofenceItemOut]**](GroupGeofenceItemOut.md) |  | 
**count** | **int** |  | 
**group_id** | **str** |  | 

## Example

```python
from spatialflow_generated.models.group_geofences_out import GroupGeofencesOut

# TODO update the JSON string below
json = "{}"
# create an instance of GroupGeofencesOut from a JSON string
group_geofences_out_instance = GroupGeofencesOut.from_json(json)
# print the JSON string representation of the object
print(GroupGeofencesOut.to_json())

# convert the object into a dict
group_geofences_out_dict = group_geofences_out_instance.to_dict()
# create an instance of GroupGeofencesOut from a dict
group_geofences_out_from_dict = GroupGeofencesOut.from_dict(group_geofences_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


