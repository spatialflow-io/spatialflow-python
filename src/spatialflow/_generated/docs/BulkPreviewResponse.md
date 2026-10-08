# BulkPreviewResponse

Response body for POST /api/v1/geofences/preview.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BulkItemPreview]**](BulkItemPreview.md) |  | 
**total** | **int** |  | 
**ok_count** | **int** |  | 
**dedup_count** | **int** |  | 
**error_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.bulk_preview_response import BulkPreviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPreviewResponse from a JSON string
bulk_preview_response_instance = BulkPreviewResponse.from_json(json)
# print the JSON string representation of the object
print(BulkPreviewResponse.to_json())

# convert the object into a dict
bulk_preview_response_dict = bulk_preview_response_instance.to_dict()
# create an instance of BulkPreviewResponse from a dict
bulk_preview_response_from_dict = BulkPreviewResponse.from_dict(bulk_preview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


