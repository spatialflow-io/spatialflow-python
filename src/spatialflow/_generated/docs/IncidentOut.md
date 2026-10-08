# IncidentOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**signal_type** | **str** |  | 
**source_ids** | **List[str]** |  | 
**severity** | **str** |  | 
**opened_at** | **datetime** |  | 
**acknowledged_at** | **datetime** |  | [optional] 
**acknowledged_by** | **str** |  | [optional] 
**muted_until** | **datetime** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**resolved_at** | **datetime** |  | [optional] 
**payload** | **Dict[str, object]** |  | 
**status** | **str** |  | 

## Example

```python
from spatialflow_generated.models.incident_out import IncidentOut

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentOut from a JSON string
incident_out_instance = IncidentOut.from_json(json)
# print the JSON string representation of the object
print(IncidentOut.to_json())

# convert the object into a dict
incident_out_dict = incident_out_instance.to_dict()
# create an instance of IncidentOut from a dict
incident_out_from_dict = IncidentOut.from_dict(incident_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


