# WorkspacePatchIn

Partial workspace update. Same fields and validation, nothing required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**support_email** | **str** |  | [optional] 
**slack_connect_url** | **str** |  | [optional] 
**unit_system** | **str** |  | [optional] 
**map_home** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.workspace_patch_in import WorkspacePatchIn

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacePatchIn from a JSON string
workspace_patch_in_instance = WorkspacePatchIn.from_json(json)
# print the JSON string representation of the object
print(WorkspacePatchIn.to_json())

# convert the object into a dict
workspace_patch_in_dict = workspace_patch_in_instance.to_dict()
# create an instance of WorkspacePatchIn from a dict
workspace_patch_in_from_dict = WorkspacePatchIn.from_dict(workspace_patch_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


