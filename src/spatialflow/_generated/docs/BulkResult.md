# BulkResult

Per-item result from POST /api/v1/geofences/bulk.  index is 0-based, mirrors input order. geofence_id present when status='created'. error_code present when status='error' and mirrors preview's top-level error_code key. error is retained for existing clients as {\"message\": str, \"code\": str}. dedup_match present when status='duplicate', or when status='created' under dedup_strategy='override' and a duplicate existed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | 
**status** | **str** |  | 
**geofence_id** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error** | **Dict[str, str]** |  | [optional] 
**dedup_match** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.bulk_result import BulkResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkResult from a JSON string
bulk_result_instance = BulkResult.from_json(json)
# print the JSON string representation of the object
print(BulkResult.to_json())

# convert the object into a dict
bulk_result_dict = bulk_result_instance.to_dict()
# create an instance of BulkResult from a dict
bulk_result_from_dict = BulkResult.from_dict(bulk_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


