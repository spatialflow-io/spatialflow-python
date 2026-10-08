# BulkItemPreview

Per-item preview result returned from POST /api/v1/geofences/preview.  index is 0-based in the API.  outcome_class and the match-metadata fields are additive: all are Optional with safe defaults so existing clients are unaffected. outcome_class values: \"success\" | \"low_confidence\" | \"interpolated\" | \"ambiguous\"                       | \"no_match\" | \"duplicate\"

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | 
**input_address** | **str** |  | 
**status** | **str** |  | 
**normalized_address** | **str** |  | [optional] 
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 
**confidence** | **float** |  | [optional] 
**dedup_match** | **Dict[str, object]** |  | [optional] 
**error_reason** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**outcome_class** | **str** |  | [optional] 
**match_type** | **str** |  | [optional] 
**interpolated** | **bool** |  | [optional] 
**candidate_count** | **int** |  | [optional] 

## Example

```python
from spatialflow_generated.models.bulk_item_preview import BulkItemPreview

# TODO update the JSON string below
json = "{}"
# create an instance of BulkItemPreview from a JSON string
bulk_item_preview_instance = BulkItemPreview.from_json(json)
# print the JSON string representation of the object
print(BulkItemPreview.to_json())

# convert the object into a dict
bulk_item_preview_dict = bulk_item_preview_instance.to_dict()
# create an instance of BulkItemPreview from a dict
bulk_item_preview_from_dict = BulkItemPreview.from_dict(bulk_item_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


