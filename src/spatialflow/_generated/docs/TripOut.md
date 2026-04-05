# TripOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**device_id** | **str** |  | 
**device_name** | **str** |  | 
**status** | **str** |  | 
**name** | **str** |  | 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**duration_seconds** | **int** |  | [optional] 
**distance_meters** | **float** |  | [optional] 
**session_id** | **str** |  | [optional] 
**has_planned_route** | **bool** |  | [optional] [default to False]
**has_track_geometry** | **bool** |  | [optional] [default to False]
**metadata** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.trip_out import TripOut

# TODO update the JSON string below
json = "{}"
# create an instance of TripOut from a JSON string
trip_out_instance = TripOut.from_json(json)
# print the JSON string representation of the object
print(TripOut.to_json())

# convert the object into a dict
trip_out_dict = trip_out_instance.to_dict()
# create an instance of TripOut from a dict
trip_out_from_dict = TripOut.from_dict(trip_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


