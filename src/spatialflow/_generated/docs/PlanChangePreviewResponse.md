# PlanChangePreviewResponse

Preview of plan change with proration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_plan** | [**PlanResponse**](PlanResponse.md) |  | 
**new_plan** | [**PlanResponse**](PlanResponse.md) |  | 
**prorated_amount** | **int** |  | 
**immediate_charge** | **int** |  | 
**next_invoice_change** | **int** |  | 
**effective_date** | **str** |  | 

## Example

```python
from spatialflow_generated.models.plan_change_preview_response import PlanChangePreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanChangePreviewResponse from a JSON string
plan_change_preview_response_instance = PlanChangePreviewResponse.from_json(json)
# print the JSON string representation of the object
print(PlanChangePreviewResponse.to_json())

# convert the object into a dict
plan_change_preview_response_dict = plan_change_preview_response_instance.to_dict()
# create an instance of PlanChangePreviewResponse from a dict
plan_change_preview_response_from_dict = PlanChangePreviewResponse.from_dict(plan_change_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


