# TileHealthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**service** | **str** |  | 
**mvt_enabled** | **bool** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.tile_health_response import TileHealthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TileHealthResponse from a JSON string
tile_health_response_instance = TileHealthResponse.from_json(json)
# print the JSON string representation of the object
print(TileHealthResponse.to_json())

# convert the object into a dict
tile_health_response_dict = tile_health_response_instance.to_dict()
# create an instance of TileHealthResponse from a dict
tile_health_response_from_dict = TileHealthResponse.from_dict(tile_health_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


