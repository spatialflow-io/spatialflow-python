# LocationPointOut

Location point for API responses (matches mobile LocationPoint type).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**timestamp** | **datetime** |  | 
**accuracy** | **float** |  | [optional] 
**speed** | **float** |  | [optional] 
**heading** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.location_point_out import LocationPointOut

# TODO update the JSON string below
json = "{}"
# create an instance of LocationPointOut from a JSON string
location_point_out_instance = LocationPointOut.from_json(json)
# print the JSON string representation of the object
print(LocationPointOut.to_json())

# convert the object into a dict
location_point_out_dict = location_point_out_instance.to_dict()
# create an instance of LocationPointOut from a dict
location_point_out_from_dict = LocationPointOut.from_dict(location_point_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


