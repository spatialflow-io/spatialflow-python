# LocationIngestResponse

Response for location ingestion (PRD §3.4 compliant).  Returns counts and event IDs/idempotency keys for tracking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **int** |  | 
**rejected** | **int** |  | 
**ids** | **List[str]** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**errors** | **List[Dict[str, object]]** |  | [optional] 
**task_ids** | **List[str]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.location_ingest_response import LocationIngestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LocationIngestResponse from a JSON string
location_ingest_response_instance = LocationIngestResponse.from_json(json)
# print the JSON string representation of the object
print(LocationIngestResponse.to_json())

# convert the object into a dict
location_ingest_response_dict = location_ingest_response_instance.to_dict()
# create an instance of LocationIngestResponse from a dict
location_ingest_response_from_dict = LocationIngestResponse.from_dict(location_ingest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


