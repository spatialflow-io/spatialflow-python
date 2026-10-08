# OverviewComparisonOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events_change** | **int** |  | 
**workflows_change** | **int** |  | 
**success_rate_change** | **float** |  | [optional] 

## Example

```python
from spatialflow_generated.models.overview_comparison_out import OverviewComparisonOut

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewComparisonOut from a JSON string
overview_comparison_out_instance = OverviewComparisonOut.from_json(json)
# print the JSON string representation of the object
print(OverviewComparisonOut.to_json())

# convert the object into a dict
overview_comparison_out_dict = overview_comparison_out_instance.to_dict()
# create an instance of OverviewComparisonOut from a dict
overview_comparison_out_from_dict = OverviewComparisonOut.from_dict(overview_comparison_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


