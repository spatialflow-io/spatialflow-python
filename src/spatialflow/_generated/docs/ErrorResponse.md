# ErrorResponse

Standard error response schema for all API endpoints.  Follows Django Ninja standard format and aligns with validation errors. Compatible with frontend apiClient.ts error handling.  Attributes:     detail: Human-readable error message or machine-readable error code     error_code: Optional machine-readable error identifier     details: Optional additional context (field errors, validation details, etc.)  Examples:     Simple error:         {\"detail\": \"Resource not found\"}      Error with code:         {\"detail\": \"FORBIDDEN\", \"error_code\": \"INSUFFICIENT_PERMISSIONS\"}      Validation error:         {             \"detail\": \"Validation failed\",             \"details\": {                 \"name\": [\"This field is required\"],                 \"email\": [\"Invalid email format\"]             }         }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**error_code** | **str** |  | [optional] 
**details** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.error_response import ErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse from a JSON string
error_response_instance = ErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse.to_json())

# convert the object into a dict
error_response_dict = error_response_instance.to_dict()
# create an instance of ErrorResponse from a dict
error_response_from_dict = ErrorResponse.from_dict(error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


