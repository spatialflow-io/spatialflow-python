# PresignedUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_url** | **str** |  | 
**key** | **str** |  | 
**expires_in** | **int** |  | 
**file_type** | **str** |  | 
**filename** | **str** |  | 
**file_id** | **str** |  | 
**content_type** | **str** |  | 

## Example

```python
from spatialflow_generated.models.presigned_url_response import PresignedUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PresignedUrlResponse from a JSON string
presigned_url_response_instance = PresignedUrlResponse.from_json(json)
# print the JSON string representation of the object
print(PresignedUrlResponse.to_json())

# convert the object into a dict
presigned_url_response_dict = presigned_url_response_instance.to_dict()
# create an instance of PresignedUrlResponse from a dict
presigned_url_response_from_dict = PresignedUrlResponse.from_dict(presigned_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


