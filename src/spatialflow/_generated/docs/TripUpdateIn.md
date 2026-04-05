# TripUpdateIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**planned_route** | **Dict[str, object]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.trip_update_in import TripUpdateIn

# TODO update the JSON string below
json = "{}"
# create an instance of TripUpdateIn from a JSON string
trip_update_in_instance = TripUpdateIn.from_json(json)
# print the JSON string representation of the object
print(TripUpdateIn.to_json())

# convert the object into a dict
trip_update_in_dict = trip_update_in_instance.to_dict()
# create an instance of TripUpdateIn from a dict
trip_update_in_from_dict = TripUpdateIn.from_dict(trip_update_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


