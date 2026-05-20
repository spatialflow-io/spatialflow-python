# OwnershipTransferRequest

Request to transfer workspace ownership.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_owner_id** | **str** |  | 

## Example

```python
from spatialflow_generated.models.ownership_transfer_request import OwnershipTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipTransferRequest from a JSON string
ownership_transfer_request_instance = OwnershipTransferRequest.from_json(json)
# print the JSON string representation of the object
print(OwnershipTransferRequest.to_json())

# convert the object into a dict
ownership_transfer_request_dict = ownership_transfer_request_instance.to_dict()
# create an instance of OwnershipTransferRequest from a dict
ownership_transfer_request_from_dict = OwnershipTransferRequest.from_dict(ownership_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


