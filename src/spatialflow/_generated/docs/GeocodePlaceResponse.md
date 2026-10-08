# GeocodePlaceResponse

Response for GET /api/v1/geofences/geocode/place.  point is [longitude, latitude] — matches GeocodeResult convention. confidence is 1.0 for place_id lookups (GetPlace returns a known place_id from autocomplete and has no Relevance score).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | **List[float]** | [longitude, latitude] of the geocoded address. | 
**confidence** | **float** | Geocoder confidence score (0-1). | 
**normalized_address** | **str** | Full normalized address string from geocoder. | 
**normalized_components** | **Dict[str, str]** | Structured address components from geocoder. | 

## Example

```python
from spatialflow_generated.models.geocode_place_response import GeocodePlaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodePlaceResponse from a JSON string
geocode_place_response_instance = GeocodePlaceResponse.from_json(json)
# print the JSON string representation of the object
print(GeocodePlaceResponse.to_json())

# convert the object into a dict
geocode_place_response_dict = geocode_place_response_instance.to_dict()
# create an instance of GeocodePlaceResponse from a dict
geocode_place_response_from_dict = GeocodePlaceResponse.from_dict(geocode_place_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


