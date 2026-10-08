# WorkspaceWebhookMetricsPerformance

Latency and retry outcomes for the caller's workspace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_response_time_ms** | **float** |  | [optional] 
**retry_success_rate** | **float** |  | [optional] 
**retried_terminal_count** | **int** |  | [optional] [default to 0]

## Example

```python
from spatialflow_generated.models.workspace_webhook_metrics_performance import WorkspaceWebhookMetricsPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceWebhookMetricsPerformance from a JSON string
workspace_webhook_metrics_performance_instance = WorkspaceWebhookMetricsPerformance.from_json(json)
# print the JSON string representation of the object
print(WorkspaceWebhookMetricsPerformance.to_json())

# convert the object into a dict
workspace_webhook_metrics_performance_dict = workspace_webhook_metrics_performance_instance.to_dict()
# create an instance of WorkspaceWebhookMetricsPerformance from a dict
workspace_webhook_metrics_performance_from_dict = WorkspaceWebhookMetricsPerformance.from_dict(workspace_webhook_metrics_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


