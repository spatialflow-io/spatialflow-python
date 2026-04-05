# PolicyOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**is_enabled** | **bool** |  | 
**geofence_id** | **str** |  | 
**geofence_name** | **str** |  | 
**time_window** | **Dict[str, object]** |  | [optional] 
**device_filter** | **Dict[str, object]** |  | [optional] 
**role_filter** | **List[str]** |  | [optional] 
**template_id** | **str** |  | [optional] [default to '']
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.policy_out import PolicyOut

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyOut from a JSON string
policy_out_instance = PolicyOut.from_json(json)
# print the JSON string representation of the object
print(PolicyOut.to_json())

# convert the object into a dict
policy_out_dict = policy_out_instance.to_dict()
# create an instance of PolicyOut from a dict
policy_out_from_dict = PolicyOut.from_dict(policy_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


