# BulkCreateRequest

Request body for POST /api/v1/geofences/bulk.  dedup_strategy defaults to 'skip'. Endpoint enforces workspace.bulk_create_max_batch_size; informational cap here.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BulkItemCommit]**](BulkItemCommit.md) |  | 
**dedup_strategy** | **str** |  | [optional] [default to 'skip']

## Example

```python
from spatialflow_generated.models.bulk_create_request import BulkCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateRequest from a JSON string
bulk_create_request_instance = BulkCreateRequest.from_json(json)
# print the JSON string representation of the object
print(BulkCreateRequest.to_json())

# convert the object into a dict
bulk_create_request_dict = bulk_create_request_instance.to_dict()
# create an instance of BulkCreateRequest from a dict
bulk_create_request_from_dict = BulkCreateRequest.from_dict(bulk_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


