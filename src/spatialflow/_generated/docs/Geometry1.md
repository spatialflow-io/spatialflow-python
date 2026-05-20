# Geometry1

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
from spatialflow_generated.models.geometry1 import Geometry1

# TODO update the JSON string below
json = "{}"
# create an instance of Geometry1 from a JSON string
geometry1_instance = Geometry1.from_json(json)
# print the JSON string representation of the object
print(Geometry1.to_json())

# convert the object into a dict
geometry1_dict = geometry1_instance.to_dict()
# create an instance of Geometry1 from a dict
geometry1_from_dict = Geometry1.from_dict(geometry1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


