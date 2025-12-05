# TestPointRequest

Schema for testing a point against geofences

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geometry** | [**GeoJSONPoint**](GeoJSONPoint.md) |  | [optional] 
**lat** | **float** |  | [optional] 
**lng** | **float** |  | [optional] 
**geofence_ids** | **List[str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.test_point_request import TestPointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointRequest from a JSON string
test_point_request_instance = TestPointRequest.from_json(json)
# print the JSON string representation of the object
print(TestPointRequest.to_json())

# convert the object into a dict
test_point_request_dict = test_point_request_instance.to_dict()
# create an instance of TestPointRequest from a dict
test_point_request_from_dict = TestPointRequest.from_dict(test_point_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


