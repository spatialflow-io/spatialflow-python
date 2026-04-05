# ContributingLocationOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**timestamp** | **datetime** |  | 
**accuracy** | **float** |  | [optional] 
**speed** | **float** |  | [optional] 
**heading** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.contributing_location_out import ContributingLocationOut

# TODO update the JSON string below
json = "{}"
# create an instance of ContributingLocationOut from a JSON string
contributing_location_out_instance = ContributingLocationOut.from_json(json)
# print the JSON string representation of the object
print(ContributingLocationOut.to_json())

# convert the object into a dict
contributing_location_out_dict = contributing_location_out_instance.to_dict()
# create an instance of ContributingLocationOut from a dict
contributing_location_out_from_dict = ContributingLocationOut.from_dict(contributing_location_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


