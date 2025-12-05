# APIUsageStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_api_keys** | **int** |  | 
**active_api_keys** | **int** |  | 
**total_api_calls** | **int** |  | 
**last_api_call** | **str** |  | 

## Example

```python
from spatialflow_generated.models.api_usage_stats import APIUsageStats

# TODO update the JSON string below
json = "{}"
# create an instance of APIUsageStats from a JSON string
api_usage_stats_instance = APIUsageStats.from_json(json)
# print the JSON string representation of the object
print(APIUsageStats.to_json())

# convert the object into a dict
api_usage_stats_dict = api_usage_stats_instance.to_dict()
# create an instance of APIUsageStats from a dict
api_usage_stats_from_dict = APIUsageStats.from_dict(api_usage_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


