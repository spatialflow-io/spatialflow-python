# EmailStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**to_email** | **str** |  | 
**subject** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**delivered_at** | **datetime** |  | 
**retry_count** | **int** |  | 
**error_message** | **str** |  | 

## Example

```python
from spatialflow_generated.models.email_status_response import EmailStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailStatusResponse from a JSON string
email_status_response_instance = EmailStatusResponse.from_json(json)
# print the JSON string representation of the object
print(EmailStatusResponse.to_json())

# convert the object into a dict
email_status_response_dict = email_status_response_instance.to_dict()
# create an instance of EmailStatusResponse from a dict
email_status_response_from_dict = EmailStatusResponse.from_dict(email_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


