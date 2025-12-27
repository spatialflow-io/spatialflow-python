# TemplateWarnings

Template validation warnings with actionable suggestions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | **List[str]** |  | 
**suggestions** | **Dict[str, str]** |  | 

## Example

```python
from spatialflow_generated.models.template_warnings import TemplateWarnings

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateWarnings from a JSON string
template_warnings_instance = TemplateWarnings.from_json(json)
# print the JSON string representation of the object
print(TemplateWarnings.to_json())

# convert the object into a dict
template_warnings_dict = template_warnings_instance.to_dict()
# create an instance of TemplateWarnings from a dict
template_warnings_from_dict = TemplateWarnings.from_dict(template_warnings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


