# Geometry3

GeoJSON geometry (Polygon, MultiPolygon, or Circle)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[List[List[float]]]]** |  | 
**center** | **List[float]** | [longitude, latitude] of circle center | 
**radius_meters** | **float** | Circle radius in meters (max 100km) | 

## Example

```python
from spatialflow_generated.models.geometry3 import Geometry3

# TODO update the JSON string below
json = "{}"
# create an instance of Geometry3 from a JSON string
geometry3_instance = Geometry3.from_json(json)
# print the JSON string representation of the object
print(Geometry3.to_json())

# convert the object into a dict
geometry3_dict = geometry3_instance.to_dict()
# create an instance of Geometry3 from a dict
geometry3_from_dict = Geometry3.from_dict(geometry3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


