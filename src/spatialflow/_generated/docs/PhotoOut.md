# PhotoOut

A session photo with where and when it was taken.  Placement uses t = ``taken_at`` when it falls within the shift (from 10 minutes before its start to 5 minutes after its end, or to now while it is open), else ``uploaded_at``, when the upload finished. ``taken_at`` is returned as the phone sent it, except that a time ahead of the server when the upload began is stored as that time. Placement tries in order: the phone's capture fix when its accuracy is 100 m or better and ``taken_at``, if sent, falls within the shift (``capture``); the nearest stored fix in the session within 60 s of t (``fix``); the latest stored fix at or before t in the session, else the first one after t (``last_fix``, approximate); interpolation along a closed session's track (``track_estimate``, approximate). A photo matching none of them has null coordinates and ``location_source``.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**file_key** | **str** |  | 
**original_name** | **str** |  | 
**content_type** | **str** |  | 
**size_bytes** | **int** |  | 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**location_source** | **str** |  | [optional] 
**location_approximate** | **bool** | True when the location is an estimate rather than a fix at the photo time. | 
**download_url** | **str** |  | 
**device_uuid** | **str** |  | 
**device_name** | **str** |  | 
**session_id** | **str** |  | 
**captured_at** | **datetime** | taken_at when the phone sent it, else uploaded_at. | 
**taken_at** | **datetime** |  | [optional] 
**uploaded_at** | **datetime** | When the upload finished. | 

## Example

```python
from spatialflow_generated.models.photo_out import PhotoOut

# TODO update the JSON string below
json = "{}"
# create an instance of PhotoOut from a JSON string
photo_out_instance = PhotoOut.from_json(json)
# print the JSON string representation of the object
print(PhotoOut.to_json())

# convert the object into a dict
photo_out_dict = photo_out_instance.to_dict()
# create an instance of PhotoOut from a dict
photo_out_from_dict = PhotoOut.from_dict(photo_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


