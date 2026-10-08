# EmailPreviewErrorResponse

Standard error fields plus the preview route's published context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**error_code** | **str** |  | [optional] 
**details** | [**Details**](Details.md) |  | [optional] 
**template** | **str** |  | [optional] 
**format** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.email_preview_error_response import EmailPreviewErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailPreviewErrorResponse from a JSON string
email_preview_error_response_instance = EmailPreviewErrorResponse.from_json(json)
# print the JSON string representation of the object
print(EmailPreviewErrorResponse.to_json())

# convert the object into a dict
email_preview_error_response_dict = email_preview_error_response_instance.to_dict()
# create an instance of EmailPreviewErrorResponse from a dict
email_preview_error_response_from_dict = EmailPreviewErrorResponse.from_dict(email_preview_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


