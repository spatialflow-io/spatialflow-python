# UserRejectionRequest

Request schema for rejecting a pending user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 

## Example

```python
from spatialflow_generated.models.user_rejection_request import UserRejectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRejectionRequest from a JSON string
user_rejection_request_instance = UserRejectionRequest.from_json(json)
# print the JSON string representation of the object
print(UserRejectionRequest.to_json())

# convert the object into a dict
user_rejection_request_dict = user_rejection_request_instance.to_dict()
# create an instance of UserRejectionRequest from a dict
user_rejection_request_from_dict = UserRejectionRequest.from_dict(user_rejection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


