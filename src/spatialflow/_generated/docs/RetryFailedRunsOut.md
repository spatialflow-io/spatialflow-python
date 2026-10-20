# RetryFailedRunsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queued** | **int** |  | 
**remaining** | **int** | Failed runs left to retry in a later batch. | 
**runs** | [**List[RunRetryOut]**](RunRetryOut.md) | The queued retries, oldest run first. | 
**not_queued** | **List[str]** | Runs whose retries couldn&#39;t be queued. They can be retried again. | [optional] 

## Example

```python
from spatialflow_generated.models.retry_failed_runs_out import RetryFailedRunsOut

# TODO update the JSON string below
json = "{}"
# create an instance of RetryFailedRunsOut from a JSON string
retry_failed_runs_out_instance = RetryFailedRunsOut.from_json(json)
# print the JSON string representation of the object
print(RetryFailedRunsOut.to_json())

# convert the object into a dict
retry_failed_runs_out_dict = retry_failed_runs_out_instance.to_dict()
# create an instance of RetryFailedRunsOut from a dict
retry_failed_runs_out_from_dict = RetryFailedRunsOut.from_dict(retry_failed_runs_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


