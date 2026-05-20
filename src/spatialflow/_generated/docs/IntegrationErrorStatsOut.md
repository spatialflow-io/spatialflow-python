# IntegrationErrorStatsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_count_24h** | **int** |  | 
**last_error_at** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.integration_error_stats_out import IntegrationErrorStatsOut

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationErrorStatsOut from a JSON string
integration_error_stats_out_instance = IntegrationErrorStatsOut.from_json(json)
# print the JSON string representation of the object
print(IntegrationErrorStatsOut.to_json())

# convert the object into a dict
integration_error_stats_out_dict = integration_error_stats_out_instance.to_dict()
# create an instance of IntegrationErrorStatsOut from a dict
integration_error_stats_out_from_dict = IntegrationErrorStatsOut.from_dict(integration_error_stats_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


