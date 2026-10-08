# LocalShiftStopIn

A stopped collector's boundary, scoped to the exact shift it stopped.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shift_started_at** | **datetime** |  | 
**stopped_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.local_shift_stop_in import LocalShiftStopIn

# TODO update the JSON string below
json = "{}"
# create an instance of LocalShiftStopIn from a JSON string
local_shift_stop_in_instance = LocalShiftStopIn.from_json(json)
# print the JSON string representation of the object
print(LocalShiftStopIn.to_json())

# convert the object into a dict
local_shift_stop_in_dict = local_shift_stop_in_instance.to_dict()
# create an instance of LocalShiftStopIn from a dict
local_shift_stop_in_from_dict = LocalShiftStopIn.from_dict(local_shift_stop_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


