# WorkspaceWebhookCounts

How many webhooks the workspace has configured

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**active** | **int** |  | 

## Example

```python
from spatialflow_generated.models.workspace_webhook_counts import WorkspaceWebhookCounts

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceWebhookCounts from a JSON string
workspace_webhook_counts_instance = WorkspaceWebhookCounts.from_json(json)
# print the JSON string representation of the object
print(WorkspaceWebhookCounts.to_json())

# convert the object into a dict
workspace_webhook_counts_dict = workspace_webhook_counts_instance.to_dict()
# create an instance of WorkspaceWebhookCounts from a dict
workspace_webhook_counts_from_dict = WorkspaceWebhookCounts.from_dict(workspace_webhook_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


