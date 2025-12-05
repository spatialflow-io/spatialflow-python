# GPXPlaybackOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**route_id** | **str** |  | 
**route_name** | **str** |  | 
**device_id** | **str** |  | 
**status** | **str** |  | 
**speed_multiplier** | **float** |  | 
**loop_enabled** | **bool** |  | 
**current_point_index** | **int** |  | 
**progress_percent** | **float** |  | 
**events_triggered** | **int** |  | 
**started_at** | **str** |  | 
**paused_at** | **str** |  | 
**completed_at** | **str** |  | 
**error_message** | **str** |  | 

## Example

```python
from spatialflow_generated.models.gpx_playback_out import GPXPlaybackOut

# TODO update the JSON string below
json = "{}"
# create an instance of GPXPlaybackOut from a JSON string
gpx_playback_out_instance = GPXPlaybackOut.from_json(json)
# print the JSON string representation of the object
print(GPXPlaybackOut.to_json())

# convert the object into a dict
gpx_playback_out_dict = gpx_playback_out_instance.to_dict()
# create an instance of GPXPlaybackOut from a dict
gpx_playback_out_from_dict = GPXPlaybackOut.from_dict(gpx_playback_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


