# BulkPreviewRequest

Request body for POST /api/v1/geofences/preview.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BulkItemInput]**](BulkItemInput.md) |  | 

## Example

```python
from spatialflow_generated.models.bulk_preview_request import BulkPreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPreviewRequest from a JSON string
bulk_preview_request_instance = BulkPreviewRequest.from_json(json)
# print the JSON string representation of the object
print(BulkPreviewRequest.to_json())

# convert the object into a dict
bulk_preview_request_dict = bulk_preview_request_instance.to_dict()
# create an instance of BulkPreviewRequest from a dict
bulk_preview_request_from_dict = BulkPreviewRequest.from_dict(bulk_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


