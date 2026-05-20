# BulkInviteItem

Single invite in a bulk invite request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**workspace_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] [default to 'field_worker']

## Example

```python
from spatialflow_generated.models.bulk_invite_item import BulkInviteItem

# TODO update the JSON string below
json = "{}"
# create an instance of BulkInviteItem from a JSON string
bulk_invite_item_instance = BulkInviteItem.from_json(json)
# print the JSON string representation of the object
print(BulkInviteItem.to_json())

# convert the object into a dict
bulk_invite_item_dict = bulk_invite_item_instance.to_dict()
# create an instance of BulkInviteItem from a dict
bulk_invite_item_from_dict = BulkInviteItem.from_dict(bulk_invite_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


