# Geometry2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[List[float]]]** | Polygon rings with at most 1000 total positions, 64 rings, and 32 holes. | 

## Example

```python
from spatialflow_generated.models.geometry2 import Geometry2

# TODO update the JSON string below
json = "{}"
# create an instance of Geometry2 from a JSON string
geometry2_instance = Geometry2.from_json(json)
# print the JSON string representation of the object
print(Geometry2.to_json())

# convert the object into a dict
geometry2_dict = geometry2_instance.to_dict()
# create an instance of Geometry2 from a dict
geometry2_from_dict = Geometry2.from_dict(geometry2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


