# BatchResendItemOut

Outcome for one invitation in a batch resend.  `invitation` carries the exact same shape the single resend endpoint returns for its 200 -- an `InvitationIssuedOut` -- so a client already handling that response can reuse it here. `detail`/`error_code` mirror the single endpoint's error body for a skipped row (not found, an owner invitation a manager may not touch, or one that stopped being pending).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation_id** | **str** |  | 
**status** | **str** |  | 
**invitation** | [**InvitationIssuedOut**](InvitationIssuedOut.md) |  | [optional] 
**detail** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.batch_resend_item_out import BatchResendItemOut

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResendItemOut from a JSON string
batch_resend_item_out_instance = BatchResendItemOut.from_json(json)
# print the JSON string representation of the object
print(BatchResendItemOut.to_json())

# convert the object into a dict
batch_resend_item_out_dict = batch_resend_item_out_instance.to_dict()
# create an instance of BatchResendItemOut from a dict
batch_resend_item_out_from_dict = BatchResendItemOut.from_dict(batch_resend_item_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


