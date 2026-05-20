# GeofenceEventOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**event_type** | **str** |  | 
**device** | [**EventDeviceOut**](EventDeviceOut.md) |  | 
**geofence** | [**EventGeofenceOut**](EventGeofenceOut.md) |  | 
**timestamp** | **str** |  | 
**location** | [**EventLocationOut**](EventLocationOut.md) |  | 
**workflows_triggered** | **List[str]** |  | [optional] [default to []]
**webhooks_triggered** | **List[str]** |  | [optional] [default to []]
**created_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.geofence_event_out import GeofenceEventOut

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceEventOut from a JSON string
geofence_event_out_instance = GeofenceEventOut.from_json(json)
# print the JSON string representation of the object
print(GeofenceEventOut.to_json())

# convert the object into a dict
geofence_event_out_dict = geofence_event_out_instance.to_dict()
# create an instance of GeofenceEventOut from a dict
geofence_event_out_from_dict = GeofenceEventOut.from_dict(geofence_event_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


