# ForgotPasswordSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from spatialflow_generated.models.forgot_password_schema import ForgotPasswordSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ForgotPasswordSchema from a JSON string
forgot_password_schema_instance = ForgotPasswordSchema.from_json(json)
# print the JSON string representation of the object
print(ForgotPasswordSchema.to_json())

# convert the object into a dict
forgot_password_schema_dict = forgot_password_schema_instance.to_dict()
# create an instance of ForgotPasswordSchema from a dict
forgot_password_schema_from_dict = ForgotPasswordSchema.from_dict(forgot_password_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


