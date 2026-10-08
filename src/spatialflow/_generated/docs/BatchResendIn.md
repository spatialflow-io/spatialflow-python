# BatchResendIn

Request payload for POST /invitations/resend-missing.  `invitation_ids` names exactly which invitations to reissue -- what the print sheet sends, since it already knows which rows have no link in this tab. Omitted (or null), it selects the newest pending page in the caller's workspace. If that page is capped, pass the returned `next_cursor` as `before` to continue through the original keyset window without selecting the newer replacement rows created by earlier pages.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation_ids** | **List[str]** |  | [optional] 
**before** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.batch_resend_in import BatchResendIn

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResendIn from a JSON string
batch_resend_in_instance = BatchResendIn.from_json(json)
# print the JSON string representation of the object
print(BatchResendIn.to_json())

# convert the object into a dict
batch_resend_in_dict = batch_resend_in_instance.to_dict()
# create an instance of BatchResendIn from a dict
batch_resend_in_from_dict = BatchResendIn.from_dict(batch_resend_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


