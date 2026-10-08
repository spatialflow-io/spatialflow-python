# OverviewEventOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**event_type** | **str** |  | 
**device** | [**OverviewEventDeviceOut**](OverviewEventDeviceOut.md) |  | 
**geofence** | [**OverviewEventGeofenceOut**](OverviewEventGeofenceOut.md) |  | 
**timestamp** | **datetime** |  | 
**location** | [**OverviewEventLocationOut**](OverviewEventLocationOut.md) |  | 
**workflows_triggered** | **List[str]** |  | 
**workflow_runs** | [**List[OverviewEventWorkflowRunOut]**](OverviewEventWorkflowRunOut.md) |  | 
**webhooks_triggered** | **List[str]** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.overview_event_out import OverviewEventOut

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewEventOut from a JSON string
overview_event_out_instance = OverviewEventOut.from_json(json)
# print the JSON string representation of the object
print(OverviewEventOut.to_json())

# convert the object into a dict
overview_event_out_dict = overview_event_out_instance.to_dict()
# create an instance of OverviewEventOut from a dict
overview_event_out_from_dict = OverviewEventOut.from_dict(overview_event_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


