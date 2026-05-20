# PerformanceSummaryOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_executions_24h** | **int** |  | 
**average_latency** | **float** |  | 
**under_target_percentage** | **float** |  | 
**workflows_meeting_target** | **int** |  | 
**workflows_missing_target** | **int** |  | 

## Example

```python
from spatialflow_generated.models.performance_summary_out import PerformanceSummaryOut

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceSummaryOut from a JSON string
performance_summary_out_instance = PerformanceSummaryOut.from_json(json)
# print the JSON string representation of the object
print(PerformanceSummaryOut.to_json())

# convert the object into a dict
performance_summary_out_dict = performance_summary_out_instance.to_dict()
# create an instance of PerformanceSummaryOut from a dict
performance_summary_out_from_dict = PerformanceSummaryOut.from_dict(performance_summary_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


