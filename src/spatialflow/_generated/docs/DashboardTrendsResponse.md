# DashboardTrendsResponse

Response for dashboard trends endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** |  | 
**series** | [**List[TrendSeries]**](TrendSeries.md) |  | 

## Example

```python
from spatialflow_generated.models.dashboard_trends_response import DashboardTrendsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardTrendsResponse from a JSON string
dashboard_trends_response_instance = DashboardTrendsResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardTrendsResponse.to_json())

# convert the object into a dict
dashboard_trends_response_dict = dashboard_trends_response_instance.to_dict()
# create an instance of DashboardTrendsResponse from a dict
dashboard_trends_response_from_dict = DashboardTrendsResponse.from_dict(dashboard_trends_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


