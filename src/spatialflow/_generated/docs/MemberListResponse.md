# MemberListResponse

Response for workspace members list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[MemberOut]**](MemberOut.md) |  | 
**total** | **int** |  | 
**truncated** | **bool** |  | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.member_list_response import MemberListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberListResponse from a JSON string
member_list_response_instance = MemberListResponse.from_json(json)
# print the JSON string representation of the object
print(MemberListResponse.to_json())

# convert the object into a dict
member_list_response_dict = member_list_response_instance.to_dict()
# create an instance of MemberListResponse from a dict
member_list_response_from_dict = MemberListResponse.from_dict(member_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


