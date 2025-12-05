# LocationUpdateOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**device_id** | **str** |  | 
**events_triggered** | **int** |  | 
**message** | **str** |  | 

## Example

```python
from spatialflow_generated.models.location_update_out import LocationUpdateOut

# TODO update the JSON string below
json = "{}"
# create an instance of LocationUpdateOut from a JSON string
location_update_out_instance = LocationUpdateOut.from_json(json)
# print the JSON string representation of the object
print(LocationUpdateOut.to_json())

# convert the object into a dict
location_update_out_dict = location_update_out_instance.to_dict()
# create an instance of LocationUpdateOut from a dict
location_update_out_from_dict = LocationUpdateOut.from_dict(location_update_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


