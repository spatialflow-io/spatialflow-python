# LocationImportResponse

Response schema for location import job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 
**filename** | **str** |  | 
**total_rows** | **int** |  | [optional] [default to 0]
**valid_rows** | **int** |  | [optional] [default to 0]
**invalid_rows** | **int** |  | [optional] [default to 0]
**processed_rows** | **int** |  | [optional] [default to 0]
**error_rate** | **float** |  | [optional] [default to 0.0]
**errors** | **List[Optional[Dict[str, object]]]** |  | [optional] [default to []]
**created_at** | **datetime** |  | 
**started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 

## Example

```python
from spatialflow_generated.models.location_import_response import LocationImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LocationImportResponse from a JSON string
location_import_response_instance = LocationImportResponse.from_json(json)
# print the JSON string representation of the object
print(LocationImportResponse.to_json())

# convert the object into a dict
location_import_response_dict = location_import_response_instance.to_dict()
# create an instance of LocationImportResponse from a dict
location_import_response_from_dict = LocationImportResponse.from_dict(location_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


