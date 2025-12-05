# WorkspaceMembersResponse

Response for workspace members list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[MemberSummary]**](MemberSummary.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**limit** | **int** |  | 
**pages** | **int** |  | 
**workspace** | [**WorkspaceSummary**](WorkspaceSummary.md) |  | 

## Example

```python
from spatialflow_generated.models.workspace_members_response import WorkspaceMembersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMembersResponse from a JSON string
workspace_members_response_instance = WorkspaceMembersResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMembersResponse.to_json())

# convert the object into a dict
workspace_members_response_dict = workspace_members_response_instance.to_dict()
# create an instance of WorkspaceMembersResponse from a dict
workspace_members_response_from_dict = WorkspaceMembersResponse.from_dict(workspace_members_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


