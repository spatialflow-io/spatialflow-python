# StartPlaybackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**speed_multiplier** | **float** |  | [optional] [default to 1.0]
**loop_enabled** | **bool** |  | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.start_playback_request import StartPlaybackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartPlaybackRequest from a JSON string
start_playback_request_instance = StartPlaybackRequest.from_json(json)
# print the JSON string representation of the object
print(StartPlaybackRequest.to_json())

# convert the object into a dict
start_playback_request_dict = start_playback_request_instance.to_dict()
# create an instance of StartPlaybackRequest from a dict
start_playback_request_from_dict = StartPlaybackRequest.from_dict(start_playback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


