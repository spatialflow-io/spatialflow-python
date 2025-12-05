# UserApprovalRequest

Request schema for approving a pending user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notes** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.user_approval_request import UserApprovalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserApprovalRequest from a JSON string
user_approval_request_instance = UserApprovalRequest.from_json(json)
# print the JSON string representation of the object
print(UserApprovalRequest.to_json())

# convert the object into a dict
user_approval_request_dict = user_approval_request_instance.to_dict()
# create an instance of UserApprovalRequest from a dict
user_approval_request_from_dict = UserApprovalRequest.from_dict(user_approval_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


