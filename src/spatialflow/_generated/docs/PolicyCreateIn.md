# PolicyCreateIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**geofence_id** | **str** |  | 
**description** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] [default to True]
**time_window** | **Dict[str, object]** |  | [optional] 
**device_filter** | **Dict[str, object]** |  | [optional] 
**role_filter** | **List[str]** |  | [optional] 
**template_id** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.policy_create_in import PolicyCreateIn

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyCreateIn from a JSON string
policy_create_in_instance = PolicyCreateIn.from_json(json)
# print the JSON string representation of the object
print(PolicyCreateIn.to_json())

# convert the object into a dict
policy_create_in_dict = policy_create_in_instance.to_dict()
# create an instance of PolicyCreateIn from a dict
policy_create_in_from_dict = PolicyCreateIn.from_dict(policy_create_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


