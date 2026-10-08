# GeofenceWorkflowReferenceOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**references** | **List[str]** |  | 

## Example

```python
from spatialflow_generated.models.geofence_workflow_reference_out import GeofenceWorkflowReferenceOut

# TODO update the JSON string below
json = "{}"
# create an instance of GeofenceWorkflowReferenceOut from a JSON string
geofence_workflow_reference_out_instance = GeofenceWorkflowReferenceOut.from_json(json)
# print the JSON string representation of the object
print(GeofenceWorkflowReferenceOut.to_json())

# convert the object into a dict
geofence_workflow_reference_out_dict = geofence_workflow_reference_out_instance.to_dict()
# create an instance of GeofenceWorkflowReferenceOut from a dict
geofence_workflow_reference_out_from_dict = GeofenceWorkflowReferenceOut.from_dict(geofence_workflow_reference_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


