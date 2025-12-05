# UploadGeofencesRequest

Schema for uploading geofences from a file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** | ID of the uploaded file from storage service | 
**group_name** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.upload_geofences_request import UploadGeofencesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadGeofencesRequest from a JSON string
upload_geofences_request_instance = UploadGeofencesRequest.from_json(json)
# print the JSON string representation of the object
print(UploadGeofencesRequest.to_json())

# convert the object into a dict
upload_geofences_request_dict = upload_geofences_request_instance.to_dict()
# create an instance of UploadGeofencesRequest from a dict
upload_geofences_request_from_dict = UploadGeofencesRequest.from_dict(upload_geofences_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


