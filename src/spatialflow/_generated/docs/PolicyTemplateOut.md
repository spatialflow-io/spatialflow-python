# PolicyTemplateOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**default_time_window** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.policy_template_out import PolicyTemplateOut

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateOut from a JSON string
policy_template_out_instance = PolicyTemplateOut.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateOut.to_json())

# convert the object into a dict
policy_template_out_dict = policy_template_out_instance.to_dict()
# create an instance of PolicyTemplateOut from a dict
policy_template_out_from_dict = PolicyTemplateOut.from_dict(policy_template_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


