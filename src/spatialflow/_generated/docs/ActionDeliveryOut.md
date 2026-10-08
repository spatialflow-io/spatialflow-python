# ActionDeliveryOut

Per-step delivery outcome for a WorkflowExecution step.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_index** | **int** |  | 
**node_id** | **str** |  | [optional] 
**step_type** | **str** |  | 
**step_name** | **str** |  | 
**step_status** | **str** |  | 
**delivery_status** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**condition_passed** | **bool** |  | [optional] 

## Example

```python
from spatialflow_generated.models.action_delivery_out import ActionDeliveryOut

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDeliveryOut from a JSON string
action_delivery_out_instance = ActionDeliveryOut.from_json(json)
# print the JSON string representation of the object
print(ActionDeliveryOut.to_json())

# convert the object into a dict
action_delivery_out_dict = action_delivery_out_instance.to_dict()
# create an instance of ActionDeliveryOut from a dict
action_delivery_out_from_dict = ActionDeliveryOut.from_dict(action_delivery_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


