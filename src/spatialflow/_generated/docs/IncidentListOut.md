# IncidentListOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[IncidentOut]**](IncidentOut.md) |  | 
**total** | **int** |  | 
**next_cursor** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.incident_list_out import IncidentListOut

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentListOut from a JSON string
incident_list_out_instance = IncidentListOut.from_json(json)
# print the JSON string representation of the object
print(IncidentListOut.to_json())

# convert the object into a dict
incident_list_out_dict = incident_list_out_instance.to_dict()
# create an instance of IncidentListOut from a dict
incident_list_out_from_dict = IncidentListOut.from_dict(incident_list_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


