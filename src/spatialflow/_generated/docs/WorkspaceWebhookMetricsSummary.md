# WorkspaceWebhookMetricsSummary

Delivery counts for the caller's workspace over the reported window

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_attempts** | **int** |  | 
**successful_deliveries** | **int** |  | 
**failed_deliveries** | **int** |  | 
**pending_deliveries** | **int** |  | 
**total_retries** | **int** |  | 
**success_rate** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.workspace_webhook_metrics_summary import WorkspaceWebhookMetricsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceWebhookMetricsSummary from a JSON string
workspace_webhook_metrics_summary_instance = WorkspaceWebhookMetricsSummary.from_json(json)
# print the JSON string representation of the object
print(WorkspaceWebhookMetricsSummary.to_json())

# convert the object into a dict
workspace_webhook_metrics_summary_dict = workspace_webhook_metrics_summary_instance.to_dict()
# create an instance of WorkspaceWebhookMetricsSummary from a dict
workspace_webhook_metrics_summary_from_dict = WorkspaceWebhookMetricsSummary.from_dict(workspace_webhook_metrics_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


