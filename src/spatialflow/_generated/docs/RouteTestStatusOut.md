# RouteTestStatusOut

Status response for a route test.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_id** | **str** |  | 
**status** | **str** |  | 
**progress** | [**RouteTestProgress**](RouteTestProgress.md) |  | [optional] 
**results** | **Dict[str, object]** |  | [optional] 
**error_message** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.route_test_status_out import RouteTestStatusOut

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTestStatusOut from a JSON string
route_test_status_out_instance = RouteTestStatusOut.from_json(json)
# print the JSON string representation of the object
print(RouteTestStatusOut.to_json())

# convert the object into a dict
route_test_status_out_dict = route_test_status_out_instance.to_dict()
# create an instance of RouteTestStatusOut from a dict
route_test_status_out_from_dict = RouteTestStatusOut.from_dict(route_test_status_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


