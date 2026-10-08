# IncidentGroupOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signal_type** | **str** |  | 
**title** | **str** |  | 
**severity** | **str** |  | 
**count** | **int** |  | 
**unacknowledged_count** | **int** |  | 
**latest_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.incident_group_out import IncidentGroupOut

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentGroupOut from a JSON string
incident_group_out_instance = IncidentGroupOut.from_json(json)
# print the JSON string representation of the object
print(IncidentGroupOut.to_json())

# convert the object into a dict
incident_group_out_dict = incident_group_out_instance.to_dict()
# create an instance of IncidentGroupOut from a dict
incident_group_out_from_dict = IncidentGroupOut.from_dict(incident_group_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


