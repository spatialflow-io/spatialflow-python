# MobileWorkspaceRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**slug** | **str** |  | 
**role** | **str** |  | 
**logo_url** | **str** |  | [optional] 
**timezone** | **str** |  | 
**unit_system** | **str** |  | 
**is_selected** | **bool** |  | 
**member_count** | **int** |  | [optional] [default to 0]

## Example

```python
from spatialflow_generated.models.mobile_workspace_row import MobileWorkspaceRow

# TODO update the JSON string below
json = "{}"
# create an instance of MobileWorkspaceRow from a JSON string
mobile_workspace_row_instance = MobileWorkspaceRow.from_json(json)
# print the JSON string representation of the object
print(MobileWorkspaceRow.to_json())

# convert the object into a dict
mobile_workspace_row_dict = mobile_workspace_row_instance.to_dict()
# create an instance of MobileWorkspaceRow from a dict
mobile_workspace_row_from_dict = MobileWorkspaceRow.from_dict(mobile_workspace_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


