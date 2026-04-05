# PolicyUpdateIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**time_window** | **Dict[str, object]** |  | [optional] 
**device_filter** | **Dict[str, object]** |  | [optional] 
**role_filter** | **List[str]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.policy_update_in import PolicyUpdateIn

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyUpdateIn from a JSON string
policy_update_in_instance = PolicyUpdateIn.from_json(json)
# print the JSON string representation of the object
print(PolicyUpdateIn.to_json())

# convert the object into a dict
policy_update_in_dict = policy_update_in_instance.to_dict()
# create an instance of PolicyUpdateIn from a dict
policy_update_in_from_dict = PolicyUpdateIn.from_dict(policy_update_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


