# EmailHealthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**checks** | **Dict[str, object]** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.email_health_response import EmailHealthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailHealthResponse from a JSON string
email_health_response_instance = EmailHealthResponse.from_json(json)
# print the JSON string representation of the object
print(EmailHealthResponse.to_json())

# convert the object into a dict
email_health_response_dict = email_health_response_instance.to_dict()
# create an instance of EmailHealthResponse from a dict
email_health_response_from_dict = EmailHealthResponse.from_dict(email_health_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


