# WorkspaceIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**logo_url** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.workspace_in import WorkspaceIn

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceIn from a JSON string
workspace_in_instance = WorkspaceIn.from_json(json)
# print the JSON string representation of the object
print(WorkspaceIn.to_json())

# convert the object into a dict
workspace_in_dict = workspace_in_instance.to_dict()
# create an instance of WorkspaceIn from a dict
workspace_in_from_dict = WorkspaceIn.from_dict(workspace_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


