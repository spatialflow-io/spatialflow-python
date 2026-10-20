# GroupWorkflowsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflows** | [**List[GroupWorkflowItemOut]**](GroupWorkflowItemOut.md) |  | 
**destination_group_id** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.group_workflows_out import GroupWorkflowsOut

# TODO update the JSON string below
json = "{}"
# create an instance of GroupWorkflowsOut from a JSON string
group_workflows_out_instance = GroupWorkflowsOut.from_json(json)
# print the JSON string representation of the object
print(GroupWorkflowsOut.to_json())

# convert the object into a dict
group_workflows_out_dict = group_workflows_out_instance.to_dict()
# create an instance of GroupWorkflowsOut from a dict
group_workflows_out_from_dict = GroupWorkflowsOut.from_dict(group_workflows_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


