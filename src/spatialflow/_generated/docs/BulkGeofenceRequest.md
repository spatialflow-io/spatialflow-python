# BulkGeofenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geofences** | [**List[CreateGeofenceRequest]**](CreateGeofenceRequest.md) |  | 

## Example

```python
from spatialflow_generated.models.bulk_geofence_request import BulkGeofenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGeofenceRequest from a JSON string
bulk_geofence_request_instance = BulkGeofenceRequest.from_json(json)
# print the JSON string representation of the object
print(BulkGeofenceRequest.to_json())

# convert the object into a dict
bulk_geofence_request_dict = bulk_geofence_request_instance.to_dict()
# create an instance of BulkGeofenceRequest from a dict
bulk_geofence_request_from_dict = BulkGeofenceRequest.from_dict(bulk_geofence_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


