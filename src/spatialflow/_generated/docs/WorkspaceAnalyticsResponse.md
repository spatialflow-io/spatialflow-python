# WorkspaceAnalyticsResponse

Response for workspace analytics endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspaces** | [**List[WorkspaceAnalyticsItem]**](WorkspaceAnalyticsItem.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from spatialflow_generated.models.workspace_analytics_response import WorkspaceAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceAnalyticsResponse from a JSON string
workspace_analytics_response_instance = WorkspaceAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceAnalyticsResponse.to_json())

# convert the object into a dict
workspace_analytics_response_dict = workspace_analytics_response_instance.to_dict()
# create an instance of WorkspaceAnalyticsResponse from a dict
workspace_analytics_response_from_dict = WorkspaceAnalyticsResponse.from_dict(workspace_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


