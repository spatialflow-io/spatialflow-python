# CurrentSessionOut

The open session of an active or paused shift, with its evidence counts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**started_at** | **datetime** |  | 
**photo_count** | **int** |  | 
**note_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.current_session_out import CurrentSessionOut

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentSessionOut from a JSON string
current_session_out_instance = CurrentSessionOut.from_json(json)
# print the JSON string representation of the object
print(CurrentSessionOut.to_json())

# convert the object into a dict
current_session_out_dict = current_session_out_instance.to_dict()
# create an instance of CurrentSessionOut from a dict
current_session_out_from_dict = CurrentSessionOut.from_dict(current_session_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


