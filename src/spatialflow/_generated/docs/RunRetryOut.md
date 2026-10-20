# RunRetryOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **str** | The new run. | 
**retry_of** | **str** | The failed run it retries. | 
**status** | **str** |  | 

## Example

```python
from spatialflow_generated.models.run_retry_out import RunRetryOut

# TODO update the JSON string below
json = "{}"
# create an instance of RunRetryOut from a JSON string
run_retry_out_instance = RunRetryOut.from_json(json)
# print the JSON string representation of the object
print(RunRetryOut.to_json())

# convert the object into a dict
run_retry_out_dict = run_retry_out_instance.to_dict()
# create an instance of RunRetryOut from a dict
run_retry_out_from_dict = RunRetryOut.from_dict(run_retry_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


