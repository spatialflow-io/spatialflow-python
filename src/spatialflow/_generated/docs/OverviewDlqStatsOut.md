# OverviewDlqStatsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_entries** | **int** |  | 
**not_requeued** | **int** |  | 
**requeued** | **int** |  | 
**top_failed_webhooks** | [**List[OverviewFailedWebhookOut]**](OverviewFailedWebhookOut.md) |  | 
**workspace_id** | **str** |  | 

## Example

```python
from spatialflow_generated.models.overview_dlq_stats_out import OverviewDlqStatsOut

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewDlqStatsOut from a JSON string
overview_dlq_stats_out_instance = OverviewDlqStatsOut.from_json(json)
# print the JSON string representation of the object
print(OverviewDlqStatsOut.to_json())

# convert the object into a dict
overview_dlq_stats_out_dict = overview_dlq_stats_out_instance.to_dict()
# create an instance of OverviewDlqStatsOut from a dict
overview_dlq_stats_out_from_dict = OverviewDlqStatsOut.from_dict(overview_dlq_stats_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


