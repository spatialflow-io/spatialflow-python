# ShiftActionOut

Response for shift control actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**device_id** | **str** |  | 
**shift_status** | **str** |  | 
**shift_started_at** | **datetime** |  | [optional] 
**shift_paused_at** | **datetime** |  | [optional] 
**shift_ended_at** | **datetime** |  | [optional] 
**message** | **str** |  | 

## Example

```python
from spatialflow_generated.models.shift_action_out import ShiftActionOut

# TODO update the JSON string below
json = "{}"
# create an instance of ShiftActionOut from a JSON string
shift_action_out_instance = ShiftActionOut.from_json(json)
# print the JSON string representation of the object
print(ShiftActionOut.to_json())

# convert the object into a dict
shift_action_out_dict = shift_action_out_instance.to_dict()
# create an instance of ShiftActionOut from a dict
shift_action_out_from_dict = ShiftActionOut.from_dict(shift_action_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


