# GroupWorkflowItemOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**group_ids** | **List[str]** |  | 
**geofence_ids** | **List[str]** |  | 

## Example

```python
from spatialflow_generated.models.group_workflow_item_out import GroupWorkflowItemOut

# TODO update the JSON string below
json = "{}"
# create an instance of GroupWorkflowItemOut from a JSON string
group_workflow_item_out_instance = GroupWorkflowItemOut.from_json(json)
# print the JSON string representation of the object
print(GroupWorkflowItemOut.to_json())

# convert the object into a dict
group_workflow_item_out_dict = group_workflow_item_out_instance.to_dict()
# create an instance of GroupWorkflowItemOut from a dict
group_workflow_item_out_from_dict = GroupWorkflowItemOut.from_dict(group_workflow_item_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


