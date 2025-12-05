# AsyncUploadGeofencesResponse

Schema for async geofence upload response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** | Upload job ID to track progress | 
**status** | **str** | Job status (pending, processing, completed, failed) | 
**message** | **str** | Human-readable status message | 
**status_url** | **str** | URL to check job status | 

## Example

```python
from spatialflow_generated.models.async_upload_geofences_response import AsyncUploadGeofencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncUploadGeofencesResponse from a JSON string
async_upload_geofences_response_instance = AsyncUploadGeofencesResponse.from_json(json)
# print the JSON string representation of the object
print(AsyncUploadGeofencesResponse.to_json())

# convert the object into a dict
async_upload_geofences_response_dict = async_upload_geofences_response_instance.to_dict()
# create an instance of AsyncUploadGeofencesResponse from a dict
async_upload_geofences_response_from_dict = AsyncUploadGeofencesResponse.from_dict(async_upload_geofences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


