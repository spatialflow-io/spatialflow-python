# GroupTestPointOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**test_point** | [**TestPointCoordinateOut**](TestPointCoordinateOut.md) |  | 
**results** | [**List[TestPointResultOut]**](TestPointResultOut.md) |  | 
**total_geofences** | **int** |  | 
**matching_geofences** | **int** |  | 

## Example

```python
from spatialflow_generated.models.group_test_point_out import GroupTestPointOut

# TODO update the JSON string below
json = "{}"
# create an instance of GroupTestPointOut from a JSON string
group_test_point_out_instance = GroupTestPointOut.from_json(json)
# print the JSON string representation of the object
print(GroupTestPointOut.to_json())

# convert the object into a dict
group_test_point_out_dict = group_test_point_out_instance.to_dict()
# create an instance of GroupTestPointOut from a dict
group_test_point_out_from_dict = GroupTestPointOut.from_dict(group_test_point_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


