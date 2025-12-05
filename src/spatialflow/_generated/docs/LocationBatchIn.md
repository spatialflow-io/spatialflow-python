# LocationBatchIn

Batch of location points for bulk ingestion.  Maximum 5000 points per batch (PRD §3.4).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | [**List[LocationPointIn]**](LocationPointIn.md) |  | 
**idempotency_key** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.location_batch_in import LocationBatchIn

# TODO update the JSON string below
json = "{}"
# create an instance of LocationBatchIn from a JSON string
location_batch_in_instance = LocationBatchIn.from_json(json)
# print the JSON string representation of the object
print(LocationBatchIn.to_json())

# convert the object into a dict
location_batch_in_dict = location_batch_in_instance.to_dict()
# create an instance of LocationBatchIn from a dict
location_batch_in_from_dict = LocationBatchIn.from_dict(location_batch_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


