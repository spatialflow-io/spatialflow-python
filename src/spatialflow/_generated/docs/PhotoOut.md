# PhotoOut

Response item for GET /devices/{uuid}/sessions/{session_id}/photos (Phase 120-04, D-16).  Lat/lon are derived per D-07: - Nearest DeviceLocation within ±60s of captured_at, OR - ST_LineInterpolatePoint on session.track_geometry (closed sessions only), OR - None when neither path produces a result (D-09 — entry still appears in the listing).  session_id added in Phase 122-01 (D-03) so the dashboard popup can deep-link to the session detail panel. Backward-compatible addition: SDK consumers that do not read session_id continue to work; consumers that need it (Phase 122 frontend popup) can read it directly from this listing.

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
**download_url** | **str** |  | 
**device_uuid** | **str** |  | 
**device_name** | **str** |  | 
**session_id** | **str** |  | 
**captured_at** | **datetime** |  | 

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


