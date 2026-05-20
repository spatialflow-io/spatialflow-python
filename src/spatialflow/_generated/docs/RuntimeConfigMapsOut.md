# RuntimeConfigMapsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dark_basemap_tile_url** | **str** |  | [optional] 
**satellite_basemap_tile_url** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.runtime_config_maps_out import RuntimeConfigMapsOut

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeConfigMapsOut from a JSON string
runtime_config_maps_out_instance = RuntimeConfigMapsOut.from_json(json)
# print the JSON string representation of the object
print(RuntimeConfigMapsOut.to_json())

# convert the object into a dict
runtime_config_maps_out_dict = runtime_config_maps_out_instance.to_dict()
# create an instance of RuntimeConfigMapsOut from a dict
runtime_config_maps_out_from_dict = RuntimeConfigMapsOut.from_dict(runtime_config_maps_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


