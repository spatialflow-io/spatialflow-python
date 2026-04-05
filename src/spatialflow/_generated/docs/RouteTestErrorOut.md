# RouteTestErrorOut

Error response for route testing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**error_code** | **str** |  | 
**line_number** | **int** |  | [optional] 

## Example

```python
from spatialflow_generated.models.route_test_error_out import RouteTestErrorOut

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTestErrorOut from a JSON string
route_test_error_out_instance = RouteTestErrorOut.from_json(json)
# print the JSON string representation of the object
print(RouteTestErrorOut.to_json())

# convert the object into a dict
route_test_error_out_dict = route_test_error_out_instance.to_dict()
# create an instance of RouteTestErrorOut from a dict
route_test_error_out_from_dict = RouteTestErrorOut.from_dict(route_test_error_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


