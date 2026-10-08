# MessageResponse

Standard success message response.  Used for operations that don't return data (e.g., delete, logout).  Attributes:     message: Success message  Example:     {\"message\": \"Resource deleted successfully\"}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from spatialflow_generated.models.message_response import MessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageResponse from a JSON string
message_response_instance = MessageResponse.from_json(json)
# print the JSON string representation of the object
print(MessageResponse.to_json())

# convert the object into a dict
message_response_dict = message_response_instance.to_dict()
# create an instance of MessageResponse from a dict
message_response_from_dict = MessageResponse.from_dict(message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


