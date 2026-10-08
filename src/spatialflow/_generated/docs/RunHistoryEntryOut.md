# RunHistoryEntryOut

One evaluation entry from WorkflowEvaluationTrace, optionally joined to execution detail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**evaluated_at** | **datetime** |  | 
**trigger_type** | **str** |  | 
**device_id** | **str** |  | [optional] 
**geofence_id** | **str** |  | [optional] 
**signal_event_id** | **str** |  | [optional] 
**event_timestamp** | **datetime** |  | [optional] 
**matched** | **bool** |  | 
**skip_reason** | **str** |  | [optional] 
**skip_reason_label** | **str** |  | [optional] 
**execution** | [**ExecutionOut**](ExecutionOut.md) |  | [optional] 
**actions** | [**List[ActionDeliveryOut]**](ActionDeliveryOut.md) |  | [optional] [default to []]

## Example

```python
from spatialflow_generated.models.run_history_entry_out import RunHistoryEntryOut

# TODO update the JSON string below
json = "{}"
# create an instance of RunHistoryEntryOut from a JSON string
run_history_entry_out_instance = RunHistoryEntryOut.from_json(json)
# print the JSON string representation of the object
print(RunHistoryEntryOut.to_json())

# convert the object into a dict
run_history_entry_out_dict = run_history_entry_out_instance.to_dict()
# create an instance of RunHistoryEntryOut from a dict
run_history_entry_out_from_dict = RunHistoryEntryOut.from_dict(run_history_entry_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


