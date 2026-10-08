# IncidentGroupListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[IncidentGroupOut]**](IncidentGroupOut.md) |  | 
**as_of** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.incident_group_list_out import IncidentGroupListOut

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentGroupListOut from a JSON string
incident_group_list_out_instance = IncidentGroupListOut.from_json(json)
# print the JSON string representation of the object
print(IncidentGroupListOut.to_json())

# convert the object into a dict
incident_group_list_out_dict = incident_group_list_out_instance.to_dict()
# create an instance of IncidentGroupListOut from a dict
incident_group_list_out_from_dict = IncidentGroupListOut.from_dict(incident_group_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


