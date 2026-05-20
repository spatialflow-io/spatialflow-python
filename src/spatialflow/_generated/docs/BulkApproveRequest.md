# BulkApproveRequest

Request to bulk approve users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | 
**notes** | **str** |  | [optional] [default to '']

## Example

```python
from spatialflow_generated.models.bulk_approve_request import BulkApproveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkApproveRequest from a JSON string
bulk_approve_request_instance = BulkApproveRequest.from_json(json)
# print the JSON string representation of the object
print(BulkApproveRequest.to_json())

# convert the object into a dict
bulk_approve_request_dict = bulk_approve_request_instance.to_dict()
# create an instance of BulkApproveRequest from a dict
bulk_approve_request_from_dict = BulkApproveRequest.from_dict(bulk_approve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


