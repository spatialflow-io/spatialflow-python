# BatchResendOut

Response for POST /invitations/resend-missing.  `remaining_count` is the number of pending rows after this page inside the keyset window as observed while the page is selected. Concurrent accepts, revocations, and expirations can reduce a later page's count.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BatchResendItemOut]**](BatchResendItemOut.md) |  | 
**resent_count** | **int** |  | 
**skipped_count** | **int** |  | 
**next_cursor** | **str** |  | [optional] 
**remaining_count** | **int** |  | [optional] [default to 0]

## Example

```python
from spatialflow_generated.models.batch_resend_out import BatchResendOut

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResendOut from a JSON string
batch_resend_out_instance = BatchResendOut.from_json(json)
# print the JSON string representation of the object
print(BatchResendOut.to_json())

# convert the object into a dict
batch_resend_out_dict = batch_resend_out_instance.to_dict()
# create an instance of BatchResendOut from a dict
batch_resend_out_from_dict = BatchResendOut.from_dict(batch_resend_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


