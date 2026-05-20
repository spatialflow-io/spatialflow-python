# EventGeofenceOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.event_geofence_out import EventGeofenceOut

# TODO update the JSON string below
json = "{}"
# create an instance of EventGeofenceOut from a JSON string
event_geofence_out_instance = EventGeofenceOut.from_json(json)
# print the JSON string representation of the object
print(EventGeofenceOut.to_json())

# convert the object into a dict
event_geofence_out_dict = event_geofence_out_instance.to_dict()
# create an instance of EventGeofenceOut from a dict
event_geofence_out_from_dict = EventGeofenceOut.from_dict(event_geofence_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


