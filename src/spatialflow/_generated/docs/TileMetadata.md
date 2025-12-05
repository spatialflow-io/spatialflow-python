# TileMetadata

Tile service metadata response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**format** | **str** |  | 
**minzoom** | **int** |  | 
**maxzoom** | **int** |  | 
**bounds** | **List[float]** |  | 
**center** | **List[float]** |  | 
**layers** | **List[Optional[Dict[str, object]]]** |  | 

## Example

```python
from spatialflow_generated.models.tile_metadata import TileMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TileMetadata from a JSON string
tile_metadata_instance = TileMetadata.from_json(json)
# print the JSON string representation of the object
print(TileMetadata.to_json())

# convert the object into a dict
tile_metadata_dict = tile_metadata_instance.to_dict()
# create an instance of TileMetadata from a dict
tile_metadata_from_dict = TileMetadata.from_dict(tile_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


