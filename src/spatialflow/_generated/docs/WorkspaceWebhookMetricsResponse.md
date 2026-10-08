# WorkspaceWebhookMetricsResponse

Customer-facing webhook metrics, scoped to one workspace.  Deliberately carries no CloudWatch dashboard link and no cross-workspace aggregate — that data belongs to the staff-only /metrics endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**WorkspaceWebhookMetricsSummary**](WorkspaceWebhookMetricsSummary.md) |  | 
**performance** | [**WorkspaceWebhookMetricsPerformance**](WorkspaceWebhookMetricsPerformance.md) |  | 
**webhooks** | [**WorkspaceWebhookCounts**](WorkspaceWebhookCounts.md) |  | 
**window_hours** | **int** |  | 
**generated_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.workspace_webhook_metrics_response import WorkspaceWebhookMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceWebhookMetricsResponse from a JSON string
workspace_webhook_metrics_response_instance = WorkspaceWebhookMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceWebhookMetricsResponse.to_json())

# convert the object into a dict
workspace_webhook_metrics_response_dict = workspace_webhook_metrics_response_instance.to_dict()
# create an instance of WorkspaceWebhookMetricsResponse from a dict
workspace_webhook_metrics_response_from_dict = WorkspaceWebhookMetricsResponse.from_dict(workspace_webhook_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


