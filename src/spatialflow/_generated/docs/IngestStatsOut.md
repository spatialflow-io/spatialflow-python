# IngestStatsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_ingested_today** | **int** |  | 
**total_ingested_week** | **int** |  | 
**devices_active** | **int** |  | 
**last_ingest** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.ingest_stats_out import IngestStatsOut

# TODO update the JSON string below
json = "{}"
# create an instance of IngestStatsOut from a JSON string
ingest_stats_out_instance = IngestStatsOut.from_json(json)
# print the JSON string representation of the object
print(IngestStatsOut.to_json())

# convert the object into a dict
ingest_stats_out_dict = ingest_stats_out_instance.to_dict()
# create an instance of IngestStatsOut from a dict
ingest_stats_out_from_dict = IngestStatsOut.from_dict(ingest_stats_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


