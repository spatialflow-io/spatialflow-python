# LoginSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from spatialflow_generated.models.login_schema import LoginSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LoginSchema from a JSON string
login_schema_instance = LoginSchema.from_json(json)
# print the JSON string representation of the object
print(LoginSchema.to_json())

# convert the object into a dict
login_schema_dict = login_schema_instance.to_dict()
# create an instance of LoginSchema from a dict
login_schema_from_dict = LoginSchema.from_dict(login_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


