# TestEventItemOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_event_id** | **str** |  | 
**event_type** | **str** |  | 
**webhook_triggered** | **bool** |  | 
**workflow_triggered** | **bool** |  | 
**execution_results** | **Dict[str, object]** |  | [optional] 
**test_metadata** | **Dict[str, object]** |  | [optional] 
**created_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.test_event_item_out import TestEventItemOut

# TODO update the JSON string below
json = "{}"
# create an instance of TestEventItemOut from a JSON string
test_event_item_out_instance = TestEventItemOut.from_json(json)
# print the JSON string representation of the object
print(TestEventItemOut.to_json())

# convert the object into a dict
test_event_item_out_dict = test_event_item_out_instance.to_dict()
# create an instance of TestEventItemOut from a dict
test_event_item_out_from_dict = TestEventItemOut.from_dict(test_event_item_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


