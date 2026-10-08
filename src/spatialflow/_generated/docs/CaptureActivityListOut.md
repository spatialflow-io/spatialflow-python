# CaptureActivityListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captures** | [**List[CaptureActivityOut]**](CaptureActivityOut.md) |  | 
**has_more** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.capture_activity_list_out import CaptureActivityListOut

# TODO update the JSON string below
json = "{}"
# create an instance of CaptureActivityListOut from a JSON string
capture_activity_list_out_instance = CaptureActivityListOut.from_json(json)
# print the JSON string representation of the object
print(CaptureActivityListOut.to_json())

# convert the object into a dict
capture_activity_list_out_dict = capture_activity_list_out_instance.to_dict()
# create an instance of CaptureActivityListOut from a dict
capture_activity_list_out_from_dict = CaptureActivityListOut.from_dict(capture_activity_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


