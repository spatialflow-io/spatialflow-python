# OccupancySummaryOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_count** | **int** |  | 
**threshold** | **int** |  | 
**comparison** | **str** |  | 
**geofence_name** | **str** |  | 

## Example

```python
from spatialflow_generated.models.occupancy_summary_out import OccupancySummaryOut

# TODO update the JSON string below
json = "{}"
# create an instance of OccupancySummaryOut from a JSON string
occupancy_summary_out_instance = OccupancySummaryOut.from_json(json)
# print the JSON string representation of the object
print(OccupancySummaryOut.to_json())

# convert the object into a dict
occupancy_summary_out_dict = occupancy_summary_out_instance.to_dict()
# create an instance of OccupancySummaryOut from a dict
occupancy_summary_out_from_dict = OccupancySummaryOut.from_dict(occupancy_summary_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


