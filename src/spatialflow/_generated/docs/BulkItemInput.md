# BulkItemInput

Input item for bulk preview requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**name** | **str** |  | [optional] 
**buffer_meters** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.bulk_item_input import BulkItemInput

# TODO update the JSON string below
json = "{}"
# create an instance of BulkItemInput from a JSON string
bulk_item_input_instance = BulkItemInput.from_json(json)
# print the JSON string representation of the object
print(BulkItemInput.to_json())

# convert the object into a dict
bulk_item_input_dict = bulk_item_input_instance.to_dict()
# create an instance of BulkItemInput from a dict
bulk_item_input_from_dict = BulkItemInput.from_dict(bulk_item_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


