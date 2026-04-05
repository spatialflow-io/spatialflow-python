# GeoJSONCircle

Circle geometry schema (PRD §3.1).  Represented as a GeoJSON Point with an additional radius_meters property. The backend converts this to a buffered polygon for spatial queries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**center** | **List[float]** | [longitude, latitude] of circle center | 
**radius_meters** | **float** | Circle radius in meters (max 100km) | 

## Example

```python
from spatialflow_generated.models.geo_json_circle import GeoJSONCircle

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJSONCircle from a JSON string
geo_json_circle_instance = GeoJSONCircle.from_json(json)
# print the JSON string representation of the object
print(GeoJSONCircle.to_json())

# convert the object into a dict
geo_json_circle_dict = geo_json_circle_instance.to_dict()
# create an instance of GeoJSONCircle from a dict
geo_json_circle_from_dict = GeoJSONCircle.from_dict(geo_json_circle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


