# CaptureActivityOut

Photos or a note the device's worker added to one session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**device_uuid** | **str** |  | 
**device_name** | **str** |  | 
**worker_name** | **str** |  | 
**session_id** | **str** |  | 
**count** | **int** |  | 
**at** | **datetime** | Latest upload or note time in the group. | 

## Example

```python
from spatialflow_generated.models.capture_activity_out import CaptureActivityOut

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureActivityOut from a JSON string
capture_activity_out_instance = CaptureActivityOut.from_json(json)
# print the JSON string representation of the object
print(CaptureActivityOut.to_json())

# convert the object into a dict
capture_activity_out_dict = capture_activity_out_instance.to_dict()
# create an instance of CaptureActivityOut from a dict
capture_activity_out_from_dict = CaptureActivityOut.from_dict(capture_activity_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


