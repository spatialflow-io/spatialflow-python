# TripsListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trips** | [**List[TripOut]**](TripOut.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.trips_list_out import TripsListOut

# TODO update the JSON string below
json = "{}"
# create an instance of TripsListOut from a JSON string
trips_list_out_instance = TripsListOut.from_json(json)
# print the JSON string representation of the object
print(TripsListOut.to_json())

# convert the object into a dict
trips_list_out_dict = trips_list_out_instance.to_dict()
# create an instance of TripsListOut from a dict
trips_list_out_from_dict = TripsListOut.from_dict(trips_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


