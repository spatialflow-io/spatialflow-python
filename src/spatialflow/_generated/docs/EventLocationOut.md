# EventLocationOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**accuracy** | **float** |  | [optional] 
**speed** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.event_location_out import EventLocationOut

# TODO update the JSON string below
json = "{}"
# create an instance of EventLocationOut from a JSON string
event_location_out_instance = EventLocationOut.from_json(json)
# print the JSON string representation of the object
print(EventLocationOut.to_json())

# convert the object into a dict
event_location_out_dict = event_location_out_instance.to_dict()
# create an instance of EventLocationOut from a dict
event_location_out_from_dict = EventLocationOut.from_dict(event_location_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


