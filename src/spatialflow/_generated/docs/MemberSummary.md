# MemberSummary

Workspace member summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**email_verified** | **bool** |  | 
**created_at** | **str** |  | 
**last_login** | **str** |  | 

## Example

```python
from spatialflow_generated.models.member_summary import MemberSummary

# TODO update the JSON string below
json = "{}"
# create an instance of MemberSummary from a JSON string
member_summary_instance = MemberSummary.from_json(json)
# print the JSON string representation of the object
print(MemberSummary.to_json())

# convert the object into a dict
member_summary_dict = member_summary_instance.to_dict()
# create an instance of MemberSummary from a dict
member_summary_from_dict = MemberSummary.from_dict(member_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


