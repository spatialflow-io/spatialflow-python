# BatchLocationUpdateIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** |  | 
**locations** | [**List[LocationUpdateIn]**](LocationUpdateIn.md) |  | 

## Example

```python
from spatialflow_generated.models.batch_location_update_in import BatchLocationUpdateIn

# TODO update the JSON string below
json = "{}"
# create an instance of BatchLocationUpdateIn from a JSON string
batch_location_update_in_instance = BatchLocationUpdateIn.from_json(json)
# print the JSON string representation of the object
print(BatchLocationUpdateIn.to_json())

# convert the object into a dict
batch_location_update_in_dict = batch_location_update_in_instance.to_dict()
# create an instance of BatchLocationUpdateIn from a dict
batch_location_update_in_from_dict = BatchLocationUpdateIn.from_dict(batch_location_update_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


