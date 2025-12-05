# ConfirmPasswordResetSchema

Schema for simpler password reset confirmation (backwards compatibility).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from spatialflow_generated.models.confirm_password_reset_schema import ConfirmPasswordResetSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmPasswordResetSchema from a JSON string
confirm_password_reset_schema_instance = ConfirmPasswordResetSchema.from_json(json)
# print the JSON string representation of the object
print(ConfirmPasswordResetSchema.to_json())

# convert the object into a dict
confirm_password_reset_schema_dict = confirm_password_reset_schema_instance.to_dict()
# create an instance of ConfirmPasswordResetSchema from a dict
confirm_password_reset_schema_from_dict = ConfirmPasswordResetSchema.from_dict(confirm_password_reset_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


