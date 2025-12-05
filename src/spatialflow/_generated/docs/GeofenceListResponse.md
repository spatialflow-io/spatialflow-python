# GeofenceListResponse

Schema for geofence list response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geofences** | [**List[GeofenceResponse]**](GeofenceResponse.md) |  | 
**count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.geofence_list_response import GeofenceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceListResponse from a JSON string
geofence_list_response_instance = GeofenceListResponse.from_json(json)
# print the JSON string representation of the object
print(GeofenceListResponse.to_json())

# convert the object into a dict
geofence_list_response_dict = geofence_list_response_instance.to_dict()
# create an instance of GeofenceListResponse from a dict
geofence_list_response_from_dict = GeofenceListResponse.from_dict(geofence_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


