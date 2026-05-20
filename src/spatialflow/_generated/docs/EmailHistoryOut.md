# EmailHistoryOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EmailHistoryItemOut]**](EmailHistoryItemOut.md) |  | 
**total** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from spatialflow_generated.models.email_history_out import EmailHistoryOut

# TODO update the JSON string below
json = "{}"
# create an instance of EmailHistoryOut from a JSON string
email_history_out_instance = EmailHistoryOut.from_json(json)
# print the JSON string representation of the object
print(EmailHistoryOut.to_json())

# convert the object into a dict
email_history_out_dict = email_history_out_instance.to_dict()
# create an instance of EmailHistoryOut from a dict
email_history_out_from_dict = EmailHistoryOut.from_dict(email_history_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


