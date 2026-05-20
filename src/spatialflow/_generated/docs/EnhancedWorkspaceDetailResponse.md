# EnhancedWorkspaceDetailResponse

Enhanced workspace detail with subscription and usage limits.

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
**subscription** | [**SubscriptionInfo**](SubscriptionInfo.md) |  | 
**usage** | [**UsageLimits**](UsageLimits.md) |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.enhanced_workspace_detail_response import EnhancedWorkspaceDetailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnhancedWorkspaceDetailResponse from a JSON string
enhanced_workspace_detail_response_instance = EnhancedWorkspaceDetailResponse.from_json(json)
# print the JSON string representation of the object
print(EnhancedWorkspaceDetailResponse.to_json())

# convert the object into a dict
enhanced_workspace_detail_response_dict = enhanced_workspace_detail_response_instance.to_dict()
# create an instance of EnhancedWorkspaceDetailResponse from a dict
enhanced_workspace_detail_response_from_dict = EnhancedWorkspaceDetailResponse.from_dict(enhanced_workspace_detail_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


