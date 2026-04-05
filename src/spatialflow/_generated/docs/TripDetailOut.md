# TripDetailOut


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
**planned_route_geojson** | **Dict[str, object]** |  | [optional] 
**track_geometry_geojson** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.trip_detail_out import TripDetailOut

# TODO update the JSON string below
json = "{}"
# create an instance of TripDetailOut from a JSON string
trip_detail_out_instance = TripDetailOut.from_json(json)
# print the JSON string representation of the object
print(TripDetailOut.to_json())

# convert the object into a dict
trip_detail_out_dict = trip_detail_out_instance.to_dict()
# create an instance of TripDetailOut from a dict
trip_detail_out_from_dict = TripDetailOut.from_dict(trip_detail_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


