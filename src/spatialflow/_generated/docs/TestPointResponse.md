# TestPointResponse

Schema for test point response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | **Dict[str, object]** |  | 
**inside_geofences** | **int** |  | 
**total_geofences** | **int** |  | 
**results** | [**List[GeofenceTestResult]**](GeofenceTestResult.md) |  | 

## Example

```python
from spatialflow_generated.models.test_point_response import TestPointResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointResponse from a JSON string
test_point_response_instance = TestPointResponse.from_json(json)
# print the JSON string representation of the object
print(TestPointResponse.to_json())

# convert the object into a dict
test_point_response_dict = test_point_response_instance.to_dict()
# create an instance of TestPointResponse from a dict
test_point_response_from_dict = TestPointResponse.from_dict(test_point_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


