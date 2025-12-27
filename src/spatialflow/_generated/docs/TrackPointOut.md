# TrackPointOut

Track point with coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** |  | 
**lon** | **float** |  | 
**ele** | **float** |  | [optional] 
**time** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.track_point_out import TrackPointOut

# TODO update the JSON string below
json = "{}"
# create an instance of TrackPointOut from a JSON string
track_point_out_instance = TrackPointOut.from_json(json)
# print the JSON string representation of the object
print(TrackPointOut.to_json())

# convert the object into a dict
track_point_out_dict = track_point_out_instance.to_dict()
# create an instance of TrackPointOut from a dict
track_point_out_from_dict = TrackPointOut.from_dict(track_point_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


