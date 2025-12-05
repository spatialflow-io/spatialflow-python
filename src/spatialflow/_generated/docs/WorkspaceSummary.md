# WorkspaceSummary

Workspace summary for displaying in lists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 

## Example

```python
from spatialflow_generated.models.workspace_summary import WorkspaceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceSummary from a JSON string
workspace_summary_instance = WorkspaceSummary.from_json(json)
# print the JSON string representation of the object
print(WorkspaceSummary.to_json())

# convert the object into a dict
workspace_summary_dict = workspace_summary_instance.to_dict()
# create an instance of WorkspaceSummary from a dict
workspace_summary_from_dict = WorkspaceSummary.from_dict(workspace_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


