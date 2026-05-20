# DashboardStatsTimelineOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_range** | **str** |  | 
**buckets** | [**List[TimelineBucketOut]**](TimelineBucketOut.md) |  | 
**previous** | [**TimelinePreviousOut**](TimelinePreviousOut.md) |  | 

## Example

```python
from spatialflow_generated.models.dashboard_stats_timeline_out import DashboardStatsTimelineOut

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardStatsTimelineOut from a JSON string
dashboard_stats_timeline_out_instance = DashboardStatsTimelineOut.from_json(json)
# print the JSON string representation of the object
print(DashboardStatsTimelineOut.to_json())

# convert the object into a dict
dashboard_stats_timeline_out_dict = dashboard_stats_timeline_out_instance.to_dict()
# create an instance of DashboardStatsTimelineOut from a dict
dashboard_stats_timeline_out_from_dict = DashboardStatsTimelineOut.from_dict(dashboard_stats_timeline_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


