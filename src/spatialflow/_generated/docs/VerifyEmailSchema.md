# VerifyEmailSchema

Schema for email verification (POST method with dual rate limiting).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from spatialflow_generated.models.verify_email_schema import VerifyEmailSchema

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyEmailSchema from a JSON string
verify_email_schema_instance = VerifyEmailSchema.from_json(json)
# print the JSON string representation of the object
print(VerifyEmailSchema.to_json())

# convert the object into a dict
verify_email_schema_dict = verify_email_schema_instance.to_dict()
# create an instance of VerifyEmailSchema from a dict
verify_email_schema_from_dict = VerifyEmailSchema.from_dict(verify_email_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


