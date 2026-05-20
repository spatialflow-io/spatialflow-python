# TrendSeries

Named trend series with data points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**data** | [**List[TrendDataPoint]**](TrendDataPoint.md) |  | 

## Example

```python
from spatialflow_generated.models.trend_series import TrendSeries

# TODO update the JSON string below
json = "{}"
# create an instance of TrendSeries from a JSON string
trend_series_instance = TrendSeries.from_json(json)
# print the JSON string representation of the object
print(TrendSeries.to_json())

# convert the object into a dict
trend_series_dict = trend_series_instance.to_dict()
# create an instance of TrendSeries from a dict
trend_series_from_dict = TrendSeries.from_dict(trend_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


