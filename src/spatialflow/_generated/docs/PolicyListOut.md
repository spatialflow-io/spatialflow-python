# PolicyListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyOut]**](PolicyOut.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.policy_list_out import PolicyListOut

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyListOut from a JSON string
policy_list_out_instance = PolicyListOut.from_json(json)
# print the JSON string representation of the object
print(PolicyListOut.to_json())

# convert the object into a dict
policy_list_out_dict = policy_list_out_instance.to_dict()
# create an instance of PolicyListOut from a dict
policy_list_out_from_dict = PolicyListOut.from_dict(policy_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


