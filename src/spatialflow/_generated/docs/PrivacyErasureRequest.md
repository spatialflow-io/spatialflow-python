# PrivacyErasureRequest

Request schema for creating privacy erasure job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | Erasure scope: org, device, date_range, tag | 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 
**device_ids** | **List[str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**dry_run** | **bool** | If true, estimate deletions without actually deleting | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.privacy_erasure_request import PrivacyErasureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PrivacyErasureRequest from a JSON string
privacy_erasure_request_instance = PrivacyErasureRequest.from_json(json)
# print the JSON string representation of the object
print(PrivacyErasureRequest.to_json())

# convert the object into a dict
privacy_erasure_request_dict = privacy_erasure_request_instance.to_dict()
# create an instance of PrivacyErasureRequest from a dict
privacy_erasure_request_from_dict = PrivacyErasureRequest.from_dict(privacy_erasure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


