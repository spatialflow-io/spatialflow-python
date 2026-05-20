# WorkspacePhotosOut

Response wrapper for GET /api/v1/devices/photos (Phase 122-01, D-03).  The workspace-wide photo listing uses a soft cap of 500 newest photos per D-26: when the database has more matching rows than ``limit``, the response returns exactly ``limit`` rows ordered newest-first and ``has_more=True``. No full COUNT(*) is run; the caller can narrow the time range to see older rows. There is no offset/limit pagination for this endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**photos** | [**List[PhotoOut]**](PhotoOut.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.workspace_photos_out import WorkspacePhotosOut

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacePhotosOut from a JSON string
workspace_photos_out_instance = WorkspacePhotosOut.from_json(json)
# print the JSON string representation of the object
print(WorkspacePhotosOut.to_json())

# convert the object into a dict
workspace_photos_out_dict = workspace_photos_out_instance.to_dict()
# create an instance of WorkspacePhotosOut from a dict
workspace_photos_out_from_dict = WorkspacePhotosOut.from_dict(workspace_photos_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


