# BulkInviteRequest

Request to bulk invite users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invites** | [**List[BulkInviteItem]**](BulkInviteItem.md) |  | 

## Example

```python
from spatialflow_generated.models.bulk_invite_request import BulkInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInviteRequest from a JSON string
bulk_invite_request_instance = BulkInviteRequest.from_json(json)
# print the JSON string representation of the object
print(BulkInviteRequest.to_json())

# convert the object into a dict
bulk_invite_request_dict = bulk_invite_request_instance.to_dict()
# create an instance of BulkInviteRequest from a dict
bulk_invite_request_from_dict = BulkInviteRequest.from_dict(bulk_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


