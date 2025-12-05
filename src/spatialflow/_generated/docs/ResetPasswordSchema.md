# ResetPasswordSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | 
**token** | **str** |  | 
**new_password** | **str** |  | 

## Example

```python
from spatialflow_generated.models.reset_password_schema import ResetPasswordSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ResetPasswordSchema from a JSON string
reset_password_schema_instance = ResetPasswordSchema.from_json(json)
# print the JSON string representation of the object
print(ResetPasswordSchema.to_json())

# convert the object into a dict
reset_password_schema_dict = reset_password_schema_instance.to_dict()
# create an instance of ResetPasswordSchema from a dict
reset_password_schema_from_dict = ResetPasswordSchema.from_dict(reset_password_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


