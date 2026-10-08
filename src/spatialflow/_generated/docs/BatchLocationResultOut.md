# BatchLocationResultOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | 
**client_location_id** | **str** |  | [optional] 
**status** | **str** |  | 
**error_code** | **str** |  | [optional] 
**retryable** | **bool** |  | [optional] [default to False]

## Example

```python
from spatialflow_generated.models.batch_location_result_out import BatchLocationResultOut

# TODO update the JSON string below
json = "{}"
# create an instance of BatchLocationResultOut from a JSON string
batch_location_result_out_instance = BatchLocationResultOut.from_json(json)
# print the JSON string representation of the object
print(BatchLocationResultOut.to_json())

# convert the object into a dict
batch_location_result_out_dict = batch_location_result_out_instance.to_dict()
# create an instance of BatchLocationResultOut from a dict
batch_location_result_out_from_dict = BatchLocationResultOut.from_dict(batch_location_result_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


