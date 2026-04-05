# SessionLocationsOut

Response for session locations with pagination or simplification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | 
**locations** | [**List[LocationPointOut]**](LocationPointOut.md) |  | 
**total_count** | **int** |  | 
**offset** | **int** |  | 
**limit** | **int** |  | 
**simplified** | **bool** |  | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.session_locations_out import SessionLocationsOut

# TODO update the JSON string below
json = "{}"
# create an instance of SessionLocationsOut from a JSON string
session_locations_out_instance = SessionLocationsOut.from_json(json)
# print the JSON string representation of the object
print(SessionLocationsOut.to_json())

# convert the object into a dict
session_locations_out_dict = session_locations_out_instance.to_dict()
# create an instance of SessionLocationsOut from a dict
session_locations_out_from_dict = SessionLocationsOut.from_dict(session_locations_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


