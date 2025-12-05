# ChangePasswordSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** |  | 
**new_password** | **str** |  | 

## Example

```python
from spatialflow_generated.models.change_password_schema import ChangePasswordSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePasswordSchema from a JSON string
change_password_schema_instance = ChangePasswordSchema.from_json(json)
# print the JSON string representation of the object
print(ChangePasswordSchema.to_json())

# convert the object into a dict
change_password_schema_dict = change_password_schema_instance.to_dict()
# create an instance of ChangePasswordSchema from a dict
change_password_schema_from_dict = ChangePasswordSchema.from_dict(change_password_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


