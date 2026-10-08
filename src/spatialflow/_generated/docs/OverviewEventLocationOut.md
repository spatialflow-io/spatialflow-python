# OverviewEventLocationOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**accuracy** | **float** |  | [optional] 
**speed** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.overview_event_location_out import OverviewEventLocationOut

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewEventLocationOut from a JSON string
overview_event_location_out_instance = OverviewEventLocationOut.from_json(json)
# print the JSON string representation of the object
print(OverviewEventLocationOut.to_json())

# convert the object into a dict
overview_event_location_out_dict = overview_event_location_out_instance.to_dict()
# create an instance of OverviewEventLocationOut from a dict
overview_event_location_out_from_dict = OverviewEventLocationOut.from_dict(overview_event_location_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


