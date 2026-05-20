# RuntimeConfigAnalyticsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posthog_enabled** | **bool** |  | 
**posthog_host** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.runtime_config_analytics_out import RuntimeConfigAnalyticsOut

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeConfigAnalyticsOut from a JSON string
runtime_config_analytics_out_instance = RuntimeConfigAnalyticsOut.from_json(json)
# print the JSON string representation of the object
print(RuntimeConfigAnalyticsOut.to_json())

# convert the object into a dict
runtime_config_analytics_out_dict = runtime_config_analytics_out_instance.to_dict()
# create an instance of RuntimeConfigAnalyticsOut from a dict
runtime_config_analytics_out_from_dict = RuntimeConfigAnalyticsOut.from_dict(runtime_config_analytics_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


