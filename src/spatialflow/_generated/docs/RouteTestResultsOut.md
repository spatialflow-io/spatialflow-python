# RouteTestResultsOut

Full results from a route test.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **str** |  | 
**status** | **str** |  | 
**file_name** | **str** |  | 
**total_points** | **int** |  | 
**total_distance_km** | **float** |  | 
**duration_seconds** | **int** |  | 
**track_points** | **List[Dict[str, object]]** |  | [optional] 
**events** | **List[Optional[Dict[str, object]]]** |  | 
**summary** | [**RouteTestSummary**](RouteTestSummary.md) |  | 

## Example

```python
from spatialflow_generated.models.route_test_results_out import RouteTestResultsOut

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTestResultsOut from a JSON string
route_test_results_out_instance = RouteTestResultsOut.from_json(json)
# print the JSON string representation of the object
print(RouteTestResultsOut.to_json())

# convert the object into a dict
route_test_results_out_dict = route_test_results_out_instance.to_dict()
# create an instance of RouteTestResultsOut from a dict
route_test_results_out_from_dict = RouteTestResultsOut.from_dict(route_test_results_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


