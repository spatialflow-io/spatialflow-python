# RouteTestProgress

Progress for async tests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points_processed** | **int** |  | 
**total_points** | **int** |  | 
**percent** | **float** |  | 

## Example

```python
from spatialflow_generated.models.route_test_progress import RouteTestProgress

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTestProgress from a JSON string
route_test_progress_instance = RouteTestProgress.from_json(json)
# print the JSON string representation of the object
print(RouteTestProgress.to_json())

# convert the object into a dict
route_test_progress_dict = route_test_progress_instance.to_dict()
# create an instance of RouteTestProgress from a dict
route_test_progress_from_dict = RouteTestProgress.from_dict(route_test_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


