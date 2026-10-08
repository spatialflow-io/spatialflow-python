# BulkCreateResponse

Response body for POST /api/v1/geofences/bulk.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BulkResult]**](BulkResult.md) |  | 

## Example

```python
from spatialflow_generated.models.bulk_create_response import BulkCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateResponse from a JSON string
bulk_create_response_instance = BulkCreateResponse.from_json(json)
# print the JSON string representation of the object
print(BulkCreateResponse.to_json())

# convert the object into a dict
bulk_create_response_dict = bulk_create_response_instance.to_dict()
# create an instance of BulkCreateResponse from a dict
bulk_create_response_from_dict = BulkCreateResponse.from_dict(bulk_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


