# AppleFullName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**given_name** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.apple_full_name import AppleFullName

# TODO update the JSON string below
json = "{}"
# create an instance of AppleFullName from a JSON string
apple_full_name_instance = AppleFullName.from_json(json)
# print the JSON string representation of the object
print(AppleFullName.to_json())

# convert the object into a dict
apple_full_name_dict = apple_full_name_instance.to_dict()
# create an instance of AppleFullName from a dict
apple_full_name_from_dict = AppleFullName.from_dict(apple_full_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


