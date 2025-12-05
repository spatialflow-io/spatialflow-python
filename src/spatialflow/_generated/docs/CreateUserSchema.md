# CreateUserSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**first_name** | **str** |  | [optional] [default to 'Test']
**last_name** | **str** |  | [optional] [default to 'User']
**email_verified** | **bool** |  | [optional] [default to True]
**is_staff** | **bool** |  | [optional] [default to False]
**is_superuser** | **bool** |  | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.create_user_schema import CreateUserSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserSchema from a JSON string
create_user_schema_instance = CreateUserSchema.from_json(json)
# print the JSON string representation of the object
print(CreateUserSchema.to_json())

# convert the object into a dict
create_user_schema_dict = create_user_schema_instance.to_dict()
# create an instance of CreateUserSchema from a dict
create_user_schema_from_dict = CreateUserSchema.from_dict(create_user_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


