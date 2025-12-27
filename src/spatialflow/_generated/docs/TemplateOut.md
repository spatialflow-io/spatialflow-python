# TemplateOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**category** | **str** |  | 
**tags** | **List[str]** |  | 
**is_featured** | **bool** |  | 
**usage_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.template_out import TemplateOut

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateOut from a JSON string
template_out_instance = TemplateOut.from_json(json)
# print the JSON string representation of the object
print(TemplateOut.to_json())

# convert the object into a dict
template_out_dict = template_out_instance.to_dict()
# create an instance of TemplateOut from a dict
template_out_from_dict = TemplateOut.from_dict(template_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


