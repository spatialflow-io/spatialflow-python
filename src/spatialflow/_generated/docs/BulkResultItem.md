# BulkResultItem

Result for a single item in a bulk operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**success** | **bool** |  | 
**message** | **str** |  | 

## Example

```python
from spatialflow_generated.models.bulk_result_item import BulkResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkResultItem from a JSON string
bulk_result_item_instance = BulkResultItem.from_json(json)
# print the JSON string representation of the object
print(BulkResultItem.to_json())

# convert the object into a dict
bulk_result_item_dict = bulk_result_item_instance.to_dict()
# create an instance of BulkResultItem from a dict
bulk_result_item_from_dict = BulkResultItem.from_dict(bulk_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


