# PrivacyErasureResponse

Response schema for privacy erasure job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 
**estimated_count** | **int** |  | 
**deleted_count** | **int** |  | 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**dry_run** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.privacy_erasure_response import PrivacyErasureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PrivacyErasureResponse from a JSON string
privacy_erasure_response_instance = PrivacyErasureResponse.from_json(json)
# print the JSON string representation of the object
print(PrivacyErasureResponse.to_json())

# convert the object into a dict
privacy_erasure_response_dict = privacy_erasure_response_instance.to_dict()
# create an instance of PrivacyErasureResponse from a dict
privacy_erasure_response_from_dict = PrivacyErasureResponse.from_dict(privacy_erasure_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


