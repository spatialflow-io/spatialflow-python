# ShiftRecoveryCurrentOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | 
**session_id** | **str** |  | [optional] 
**shift_status** | **str** |  | 
**shift_started_at** | **datetime** |  | [optional] 
**shift_paused_at** | **datetime** |  | [optional] 
**shift_resumed_at** | **datetime** |  | [optional] 
**shift_ended_at** | **datetime** |  | [optional] 

## Example

```python
from spatialflow_generated.models.shift_recovery_current_out import ShiftRecoveryCurrentOut

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftRecoveryCurrentOut from a JSON string
shift_recovery_current_out_instance = ShiftRecoveryCurrentOut.from_json(json)
# print the JSON string representation of the object
print(ShiftRecoveryCurrentOut.to_json())

# convert the object into a dict
shift_recovery_current_out_dict = shift_recovery_current_out_instance.to_dict()
# create an instance of ShiftRecoveryCurrentOut from a dict
shift_recovery_current_out_from_dict = ShiftRecoveryCurrentOut.from_dict(shift_recovery_current_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


