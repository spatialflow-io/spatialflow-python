# WorkspaceDetailResponse

Detailed workspace information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**billing_email** | **str** |  | 
**website** | **str** |  | 
**logo_url** | **str** |  | 
**timezone** | **str** |  | 
**stripe_customer_id** | **str** |  | 
**member_count** | **int** |  | 
**usage_stats** | [**UsageStats**](UsageStats.md) |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.workspace_detail_response import WorkspaceDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceDetailResponse from a JSON string
workspace_detail_response_instance = WorkspaceDetailResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceDetailResponse.to_json())

# convert the object into a dict
workspace_detail_response_dict = workspace_detail_response_instance.to_dict()
# create an instance of WorkspaceDetailResponse from a dict
workspace_detail_response_from_dict = WorkspaceDetailResponse.from_dict(workspace_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


