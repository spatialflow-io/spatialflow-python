# AuditLogOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_email** | **str** |  | 
**action** | **str** |  | 
**resource_type** | **str** |  | 
**resource_id** | **str** |  | [optional] 
**description** | **str** |  | 
**changes** | **Dict[str, object]** |  | 
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**http_method** | **str** |  | 
**path** | **str** |  | 
**status_code** | **int** |  | [optional] 
**created_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.audit_log_out import AuditLogOut

# TODO update the JSON string below
json = "{}"
# create an instance of AuditLogOut from a JSON string
audit_log_out_instance = AuditLogOut.from_json(json)
# print the JSON string representation of the object
print(AuditLogOut.to_json())

# convert the object into a dict
audit_log_out_dict = audit_log_out_instance.to_dict()
# create an instance of AuditLogOut from a dict
audit_log_out_from_dict = AuditLogOut.from_dict(audit_log_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


