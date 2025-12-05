# LocationUpdateIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**timestamp** | **datetime** |  | [optional] 
**accuracy** | **float** |  | [optional] 
**speed** | **float** |  | [optional] 
**heading** | **float** |  | [optional] 
**altitude** | **float** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from spatialflow_generated.models.location_update_in import LocationUpdateIn

# TODO update the JSON string below
json = "{}"
# create an instance of LocationUpdateIn from a JSON string
location_update_in_instance = LocationUpdateIn.from_json(json)
# print the JSON string representation of the object
print(LocationUpdateIn.to_json())

# convert the object into a dict
location_update_in_dict = location_update_in_instance.to_dict()
# create an instance of LocationUpdateIn from a dict
location_update_in_from_dict = LocationUpdateIn.from_dict(location_update_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


