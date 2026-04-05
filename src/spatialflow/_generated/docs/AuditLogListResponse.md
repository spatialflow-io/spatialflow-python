# AuditLogListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logs** | [**List[AuditLogOut]**](AuditLogOut.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 
**has_more** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.audit_log_list_response import AuditLogListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogListResponse from a JSON string
audit_log_list_response_instance = AuditLogListResponse.from_json(json)
# print the JSON string representation of the object
print(AuditLogListResponse.to_json())

# convert the object into a dict
audit_log_list_response_dict = audit_log_list_response_instance.to_dict()
# create an instance of AuditLogListResponse from a dict
audit_log_list_response_from_dict = AuditLogListResponse.from_dict(audit_log_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


