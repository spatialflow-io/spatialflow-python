# GeofenceGroupItemOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**group_name** | **str** |  | [optional] 
**geofence_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.geofence_group_item_out import GeofenceGroupItemOut

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceGroupItemOut from a JSON string
geofence_group_item_out_instance = GeofenceGroupItemOut.from_json(json)
# print the JSON string representation of the object
print(GeofenceGroupItemOut.to_json())

# convert the object into a dict
geofence_group_item_out_dict = geofence_group_item_out_instance.to_dict()
# create an instance of GeofenceGroupItemOut from a dict
geofence_group_item_out_from_dict = GeofenceGroupItemOut.from_dict(geofence_group_item_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


