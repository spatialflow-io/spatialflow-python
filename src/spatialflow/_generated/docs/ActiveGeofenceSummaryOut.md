# ActiveGeofenceSummaryOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geofences** | [**List[ActiveGeofenceSummaryItemOut]**](ActiveGeofenceSummaryItemOut.md) |  | 

## Example

```python
from spatialflow_generated.models.active_geofence_summary_out import ActiveGeofenceSummaryOut

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveGeofenceSummaryOut from a JSON string
active_geofence_summary_out_instance = ActiveGeofenceSummaryOut.from_json(json)
# print the JSON string representation of the object
print(ActiveGeofenceSummaryOut.to_json())

# convert the object into a dict
active_geofence_summary_out_dict = active_geofence_summary_out_instance.to_dict()
# create an instance of ActiveGeofenceSummaryOut from a dict
active_geofence_summary_out_from_dict = ActiveGeofenceSummaryOut.from_dict(active_geofence_summary_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


