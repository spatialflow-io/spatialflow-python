# GeofenceStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_geofences** | **int** |  | 
**active_geofences** | **int** |  | 

## Example

```python
from spatialflow_generated.models.geofence_stats import GeofenceStats

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceStats from a JSON string
geofence_stats_instance = GeofenceStats.from_json(json)
# print the JSON string representation of the object
print(GeofenceStats.to_json())

# convert the object into a dict
geofence_stats_dict = geofence_stats_instance.to_dict()
# create an instance of GeofenceStats from a dict
geofence_stats_from_dict = GeofenceStats.from_dict(geofence_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


