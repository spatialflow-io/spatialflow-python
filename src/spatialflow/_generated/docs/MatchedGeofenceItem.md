# MatchedGeofenceItem

Schema for matched geofence in test response.  Provides detailed information about geofences that contain the test point, including group membership for filtering and organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geofence_id** | **str** |  | 
**geofence_name** | **str** |  | 
**group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**distance_meters** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.matched_geofence_item import MatchedGeofenceItem

# TODO update the JSON string below
json = "{}"
# create an instance of MatchedGeofenceItem from a JSON string
matched_geofence_item_instance = MatchedGeofenceItem.from_json(json)
# print the JSON string representation of the object
print(MatchedGeofenceItem.to_json())

# convert the object into a dict
matched_geofence_item_dict = matched_geofence_item_instance.to_dict()
# create an instance of MatchedGeofenceItem from a dict
matched_geofence_item_from_dict = MatchedGeofenceItem.from_dict(matched_geofence_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


