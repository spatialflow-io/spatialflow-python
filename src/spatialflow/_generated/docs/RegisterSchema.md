# RegisterSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 
**name** | **str** |  | 
**company** | **str** |  | [optional] 
**signup_type** | **str** |  | [optional] 
**use_case** | **str** |  | [optional] 
**utm_source** | **str** |  | [optional] 
**utm_medium** | **str** |  | [optional] 
**utm_campaign** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.register_schema import RegisterSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterSchema from a JSON string
register_schema_instance = RegisterSchema.from_json(json)
# print the JSON string representation of the object
print(RegisterSchema.to_json())

# convert the object into a dict
register_schema_dict = register_schema_instance.to_dict()
# create an instance of RegisterSchema from a dict
register_schema_from_dict = RegisterSchema.from_dict(register_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


