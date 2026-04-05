# RecentLocationsOut

Response for recent device locations (session-independent).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | [**List[LocationPointOut]**](LocationPointOut.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.recent_locations_out import RecentLocationsOut

# TODO update the JSON string below
json = "{}"
# create an instance of RecentLocationsOut from a JSON string
recent_locations_out_instance = RecentLocationsOut.from_json(json)
# print the JSON string representation of the object
print(RecentLocationsOut.to_json())

# convert the object into a dict
recent_locations_out_dict = recent_locations_out_instance.to_dict()
# create an instance of RecentLocationsOut from a dict
recent_locations_out_from_dict = RecentLocationsOut.from_dict(recent_locations_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


