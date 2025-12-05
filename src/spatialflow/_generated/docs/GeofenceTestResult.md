# GeofenceTestResult

Schema for individual geofence test result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geofence_id** | **str** |  | 
**geofence_name** | **str** |  | 
**is_inside** | **bool** |  | 
**distance_meters** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.geofence_test_result import GeofenceTestResult

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceTestResult from a JSON string
geofence_test_result_instance = GeofenceTestResult.from_json(json)
# print the JSON string representation of the object
print(GeofenceTestResult.to_json())

# convert the object into a dict
geofence_test_result_dict = geofence_test_result_instance.to_dict()
# create an instance of GeofenceTestResult from a dict
geofence_test_result_from_dict = GeofenceTestResult.from_dict(geofence_test_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


