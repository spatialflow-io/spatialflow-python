# BulkDeactivateRequest

Request to bulk deactivate users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** |  | 

## Example

```python
from spatialflow_generated.models.bulk_deactivate_request import BulkDeactivateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeactivateRequest from a JSON string
bulk_deactivate_request_instance = BulkDeactivateRequest.from_json(json)
# print the JSON string representation of the object
print(BulkDeactivateRequest.to_json())

# convert the object into a dict
bulk_deactivate_request_dict = bulk_deactivate_request_instance.to_dict()
# create an instance of BulkDeactivateRequest from a dict
bulk_deactivate_request_from_dict = BulkDeactivateRequest.from_dict(bulk_deactivate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


