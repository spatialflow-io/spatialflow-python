# RouteTestSummary

Summary statistics for a route test.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_events** | **int** |  | 
**geofence_enters** | **int** |  | 
**geofence_exits** | **int** |  | 
**geofence_dwells** | **int** |  | 
**workflows_triggered** | **int** |  | 
**geofences_crossed** | **List[str]** |  | 

## Example

```python
from spatialflow_generated.models.route_test_summary import RouteTestSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTestSummary from a JSON string
route_test_summary_instance = RouteTestSummary.from_json(json)
# print the JSON string representation of the object
print(RouteTestSummary.to_json())

# convert the object into a dict
route_test_summary_dict = route_test_summary_instance.to_dict()
# create an instance of RouteTestSummary from a dict
route_test_summary_from_dict = RouteTestSummary.from_dict(route_test_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


