# RecentExecutionOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**execution_id** | **str** |  | 
**status** | **str** |  | 
**trigger_source** | **str** |  | 
**started_at** | **str** |  | [optional] 
**duration_seconds** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.recent_execution_out import RecentExecutionOut

# TODO update the JSON string below
json = "{}"
# create an instance of RecentExecutionOut from a JSON string
recent_execution_out_instance = RecentExecutionOut.from_json(json)
# print the JSON string representation of the object
print(RecentExecutionOut.to_json())

# convert the object into a dict
recent_execution_out_dict = recent_execution_out_instance.to_dict()
# create an instance of RecentExecutionOut from a dict
recent_execution_out_from_dict = RecentExecutionOut.from_dict(recent_execution_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


