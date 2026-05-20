# OwnershipTransferResponse

Response for ownership transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**workspace_id** | **str** |  | 
**previous_owner_id** | **str** |  | 
**new_owner_id** | **str** |  | 

## Example

```python
from spatialflow_generated.models.ownership_transfer_response import OwnershipTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipTransferResponse from a JSON string
ownership_transfer_response_instance = OwnershipTransferResponse.from_json(json)
# print the JSON string representation of the object
print(OwnershipTransferResponse.to_json())

# convert the object into a dict
ownership_transfer_response_dict = ownership_transfer_response_instance.to_dict()
# create an instance of OwnershipTransferResponse from a dict
ownership_transfer_response_from_dict = OwnershipTransferResponse.from_dict(ownership_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


