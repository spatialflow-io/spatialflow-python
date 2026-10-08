# BulkItemCommit

Input item for POST /api/v1/geofences/bulk commit request.  index is 0-based. override_dedup lets a caller override dedup handling for this specific item even under dedup_strategy='skip'.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | 
**address** | **str** |  | 
**name** | **str** |  | [optional] 
**buffer_meters** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**status** | **str** |  | 
**override_dedup** | **bool** |  | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.bulk_item_commit import BulkItemCommit

# TODO update the JSON string below
json = "{}"
# create an instance of BulkItemCommit from a JSON string
bulk_item_commit_instance = BulkItemCommit.from_json(json)
# print the JSON string representation of the object
print(BulkItemCommit.to_json())

# convert the object into a dict
bulk_item_commit_dict = bulk_item_commit_instance.to_dict()
# create an instance of BulkItemCommit from a dict
bulk_item_commit_from_dict = BulkItemCommit.from_dict(bulk_item_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


