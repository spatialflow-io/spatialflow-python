# PresignedUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_type** | **str** |  | 
**filename** | **str** |  | 
**file_size** | **int** |  | 

## Example

```python
from spatialflow_generated.models.presigned_url_request import PresignedUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PresignedUrlRequest from a JSON string
presigned_url_request_instance = PresignedUrlRequest.from_json(json)
# print the JSON string representation of the object
print(PresignedUrlRequest.to_json())

# convert the object into a dict
presigned_url_request_dict = presigned_url_request_instance.to_dict()
# create an instance of PresignedUrlRequest from a dict
presigned_url_request_from_dict = PresignedUrlRequest.from_dict(presigned_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


