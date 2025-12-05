# UploadJobStatus

Schema for upload job status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 
**file_name** | **str** |  | 
**file_format** | **str** |  | 
**created_at** | **datetime** |  | 
**started_at** | **datetime** |  | 
**completed_at** | **datetime** |  | 
**duration** | **float** |  | [optional] 
**total_features** | **int** |  | 
**created_count** | **int** |  | 
**failed_count** | **int** |  | 
**results** | **Dict[str, object]** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.upload_job_status import UploadJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UploadJobStatus from a JSON string
upload_job_status_instance = UploadJobStatus.from_json(json)
# print the JSON string representation of the object
print(UploadJobStatus.to_json())

# convert the object into a dict
upload_job_status_dict = upload_job_status_instance.to_dict()
# create an instance of UploadJobStatus from a dict
upload_job_status_from_dict = UploadJobStatus.from_dict(upload_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


