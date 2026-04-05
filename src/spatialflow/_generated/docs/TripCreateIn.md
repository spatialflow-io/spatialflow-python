# TripCreateIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | 
**name** | **str** |  | [optional] [default to '']
**planned_route** | **Dict[str, object]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.trip_create_in import TripCreateIn

# TODO update the JSON string below
json = "{}"
# create an instance of TripCreateIn from a JSON string
trip_create_in_instance = TripCreateIn.from_json(json)
# print the JSON string representation of the object
print(TripCreateIn.to_json())

# convert the object into a dict
trip_create_in_dict = trip_create_in_instance.to_dict()
# create an instance of TripCreateIn from a dict
trip_create_in_from_dict = TripCreateIn.from_dict(trip_create_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


