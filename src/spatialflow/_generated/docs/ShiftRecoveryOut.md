# ShiftRecoveryOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_uuid** | **str** |  | 
**device_id** | **str** |  | 
**source_session_id** | **str** |  | 
**outcome** | **str** |  | 
**reason** | **str** |  | [optional] 
**replacement** | [**ShiftRecoveryReplacementOut**](ShiftRecoveryReplacementOut.md) |  | [optional] 
**current** | [**ShiftRecoveryCurrentOut**](ShiftRecoveryCurrentOut.md) |  | 

## Example

```python
from spatialflow_generated.models.shift_recovery_out import ShiftRecoveryOut

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftRecoveryOut from a JSON string
shift_recovery_out_instance = ShiftRecoveryOut.from_json(json)
# print the JSON string representation of the object
print(ShiftRecoveryOut.to_json())

# convert the object into a dict
shift_recovery_out_dict = shift_recovery_out_instance.to_dict()
# create an instance of ShiftRecoveryOut from a dict
shift_recovery_out_from_dict = ShiftRecoveryOut.from_dict(shift_recovery_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


