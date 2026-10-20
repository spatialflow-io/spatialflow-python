# RetryFailedRunsPreviewOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **int** | Failed runs that can be retried now. | 
**batch_size** | **int** | How many of them the next batch would queue. | 
**batch_limit** | **int** | The most runs one batch queues. | 
**blocked_reason** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.retry_failed_runs_preview_out import RetryFailedRunsPreviewOut

# TODO update the JSON string below
json = "{}"
# create an instance of RetryFailedRunsPreviewOut from a JSON string
retry_failed_runs_preview_out_instance = RetryFailedRunsPreviewOut.from_json(json)
# print the JSON string representation of the object
print(RetryFailedRunsPreviewOut.to_json())

# convert the object into a dict
retry_failed_runs_preview_out_dict = retry_failed_runs_preview_out_instance.to_dict()
# create an instance of RetryFailedRunsPreviewOut from a dict
retry_failed_runs_preview_out_from_dict = RetryFailedRunsPreviewOut.from_dict(retry_failed_runs_preview_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


