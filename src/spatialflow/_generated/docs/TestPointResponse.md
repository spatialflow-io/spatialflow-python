# TestPointResponse

Schema for test point response.  Provides both the legacy `results` array (unchanged for backward compatibility) and the new `matched_geofences` array with enhanced group information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | **Dict[str, object]** |  | 
**inside_geofences** | **int** |  | 
**total_geofences** | **int** |  | 
**results** | [**List[GeofenceTestResult]**](GeofenceTestResult.md) |  | 
**matched_geofences** | [**List[MatchedGeofenceItem]**](MatchedGeofenceItem.md) | Geofences containing the test point, with group info. Ordered by distance_meters ASC, then geofence_id ASC. | [optional] 
**request_metadata** | **Dict[str, object]** |  | [optional] 

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


