# TestPointResultOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geofence_id** | **str** |  | 
**geofence_name** | **str** |  | 
**contains** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.test_point_result_out import TestPointResultOut

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointResultOut from a JSON string
test_point_result_out_instance = TestPointResultOut.from_json(json)
# print the JSON string representation of the object
print(TestPointResultOut.to_json())

# convert the object into a dict
test_point_result_out_dict = test_point_result_out_instance.to_dict()
# create an instance of TestPointResultOut from a dict
test_point_result_out_from_dict = TestPointResultOut.from_dict(test_point_result_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


