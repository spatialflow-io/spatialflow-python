# EmailHistoryItemOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**to_email** | **str** |  | 
**subject** | **str** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 
**delivered_at** | **str** |  | [optional] 
**template** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.email_history_item_out import EmailHistoryItemOut

# TODO update the JSON string below
json = "{}"
# create an instance of EmailHistoryItemOut from a JSON string
email_history_item_out_instance = EmailHistoryItemOut.from_json(json)
# print the JSON string representation of the object
print(EmailHistoryItemOut.to_json())

# convert the object into a dict
email_history_item_out_dict = email_history_item_out_instance.to_dict()
# create an instance of EmailHistoryItemOut from a dict
email_history_item_out_from_dict = EmailHistoryItemOut.from_dict(email_history_item_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


