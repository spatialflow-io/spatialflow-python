# LocationPointIn

Single location point for ingestion.  PRD Reference: §3.4 Location Ingest Format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | 
**lat** | **float** |  | 
**lon** | **float** |  | 
**ts** | **datetime** |  | 
**accuracy** | **float** |  | [optional] 
**speed** | **float** |  | [optional] 
**heading** | **float** |  | [optional] 
**altitude** | **float** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.location_point_in import LocationPointIn

# TODO update the JSON string below
json = "{}"
# create an instance of LocationPointIn from a JSON string
location_point_in_instance = LocationPointIn.from_json(json)
# print the JSON string representation of the object
print(LocationPointIn.to_json())

# convert the object into a dict
location_point_in_dict = location_point_in_instance.to_dict()
# create an instance of LocationPointIn from a dict
location_point_in_from_dict = LocationPointIn.from_dict(location_point_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


