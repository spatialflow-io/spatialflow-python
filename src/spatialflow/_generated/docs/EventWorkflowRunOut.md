# EventWorkflowRunOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** |  | 
**id** | **str** |  | 
**workflow_id** | **str** |  | 

## Example

```python
from spatialflow_generated.models.event_workflow_run_out import EventWorkflowRunOut

# TODO update the JSON string below
json = "{}"
# create an instance of EventWorkflowRunOut from a JSON string
event_workflow_run_out_instance = EventWorkflowRunOut.from_json(json)
# print the JSON string representation of the object
print(EventWorkflowRunOut.to_json())

# convert the object into a dict
event_workflow_run_out_dict = event_workflow_run_out_instance.to_dict()
# create an instance of EventWorkflowRunOut from a dict
event_workflow_run_out_from_dict = EventWorkflowRunOut.from_dict(event_workflow_run_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


