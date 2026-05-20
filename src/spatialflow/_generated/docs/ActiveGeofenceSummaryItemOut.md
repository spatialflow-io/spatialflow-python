# ActiveGeofenceSummaryItemOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**geometry** | **Dict[str, object]** |  | 
**center** | **List[float]** |  | 
**event_count_today** | **int** |  | 

## Example

```python
from spatialflow_generated.models.active_geofence_summary_item_out import ActiveGeofenceSummaryItemOut

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveGeofenceSummaryItemOut from a JSON string
active_geofence_summary_item_out_instance = ActiveGeofenceSummaryItemOut.from_json(json)
# print the JSON string representation of the object
print(ActiveGeofenceSummaryItemOut.to_json())

# convert the object into a dict
active_geofence_summary_item_out_dict = active_geofence_summary_item_out_instance.to_dict()
# create an instance of ActiveGeofenceSummaryItemOut from a dict
active_geofence_summary_item_out_from_dict = ActiveGeofenceSummaryItemOut.from_dict(active_geofence_summary_item_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


