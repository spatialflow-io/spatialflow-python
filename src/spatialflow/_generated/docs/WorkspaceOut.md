# WorkspaceOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**slug** | **str** |  | 
**logo_url** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**timezone** | **str** | Workspace default timezone | [optional] [default to 'UTC']
**support_email** | **str** |  | [optional] 
**slack_connect_url** | **str** |  | [optional] 
**unit_system** | **str** | Unit system for display (imperial: mi/mph/ft, metric: km/kph/m) | [optional] [default to 'imperial']
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.workspace_out import WorkspaceOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceOut from a JSON string
workspace_out_instance = WorkspaceOut.from_json(json)
# print the JSON string representation of the object
print(WorkspaceOut.to_json())

# convert the object into a dict
workspace_out_dict = workspace_out_instance.to_dict()
# create an instance of WorkspaceOut from a dict
workspace_out_from_dict = WorkspaceOut.from_dict(workspace_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


