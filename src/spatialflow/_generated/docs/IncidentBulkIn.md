# IncidentBulkIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**signal_type** | **str** |  | [optional] 
**ids** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] [default to 'open']
**severity** | **str** |  | [optional] 
**as_of** | **datetime** |  | 
**expected_count** | **int** |  | [optional] 

## Example

```python
from spatialflow_generated.models.incident_bulk_in import IncidentBulkIn

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentBulkIn from a JSON string
incident_bulk_in_instance = IncidentBulkIn.from_json(json)
# print the JSON string representation of the object
print(IncidentBulkIn.to_json())

# convert the object into a dict
incident_bulk_in_dict = incident_bulk_in_instance.to_dict()
# create an instance of IncidentBulkIn from a dict
incident_bulk_in_from_dict = IncidentBulkIn.from_dict(incident_bulk_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


