# DormantWorkspaceResponse

Response for dormant workspaces endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[DormantWorkspaceItem]**](DormantWorkspaceItem.md) |  | 
**total** | **int** |  | 
**inactive_days_threshold** | **int** |  | 

## Example

```python
from spatialflow_generated.models.dormant_workspace_response import DormantWorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DormantWorkspaceResponse from a JSON string
dormant_workspace_response_instance = DormantWorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(DormantWorkspaceResponse.to_json())

# convert the object into a dict
dormant_workspace_response_dict = dormant_workspace_response_instance.to_dict()
# create an instance of DormantWorkspaceResponse from a dict
dormant_workspace_response_from_dict = DormantWorkspaceResponse.from_dict(dormant_workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


