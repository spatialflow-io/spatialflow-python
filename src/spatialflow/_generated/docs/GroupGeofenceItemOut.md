# GroupGeofenceItemOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**group_id** | **str** |  | 
**group_name** | **str** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.group_geofence_item_out import GroupGeofenceItemOut

# TODO update the JSON string below
json = "{}"
# create an instance of GroupGeofenceItemOut from a JSON string
group_geofence_item_out_instance = GroupGeofenceItemOut.from_json(json)
# print the JSON string representation of the object
print(GroupGeofenceItemOut.to_json())

# convert the object into a dict
group_geofence_item_out_dict = group_geofence_item_out_instance.to_dict()
# create an instance of GroupGeofenceItemOut from a dict
group_geofence_item_out_from_dict = GroupGeofenceItemOut.from_dict(group_geofence_item_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


