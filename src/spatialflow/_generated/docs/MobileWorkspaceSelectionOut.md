# MobileWorkspaceSelectionOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible_workspaces** | [**List[MobileWorkspaceRow]**](MobileWorkspaceRow.md) |  | 
**eligible_count** | **int** |  | 
**selected_workspace_id** | **str** |  | [optional] 
**selected_workspace** | [**MobileWorkspaceRow**](MobileWorkspaceRow.md) |  | [optional] 
**skip_picker** | **bool** |  | 
**selection_required** | **bool** |  | 
**access_token** | **str** |  | 
**refresh_token** | **str** |  | 
**token_type** | **str** |  | 
**expires_in** | **int** |  | 
**user** | **Dict[str, object]** |  | 

## Example

```python
from spatialflow_generated.models.mobile_workspace_selection_out import MobileWorkspaceSelectionOut

# TODO update the JSON string below
json = "{}"
# create an instance of MobileWorkspaceSelectionOut from a JSON string
mobile_workspace_selection_out_instance = MobileWorkspaceSelectionOut.from_json(json)
# print the JSON string representation of the object
print(MobileWorkspaceSelectionOut.to_json())

# convert the object into a dict
mobile_workspace_selection_out_dict = mobile_workspace_selection_out_instance.to_dict()
# create an instance of MobileWorkspaceSelectionOut from a dict
mobile_workspace_selection_out_from_dict = MobileWorkspaceSelectionOut.from_dict(mobile_workspace_selection_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


