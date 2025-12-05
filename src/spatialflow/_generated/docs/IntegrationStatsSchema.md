# IntegrationStatsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_uses** | **int** |  | 
**successful_uses** | **int** |  | 
**success_rate** | **float** |  | 
**average_duration_ms** | **float** |  | 
**health_status** | **str** |  | 
**last_used_at** | **str** |  | 
**last_health_check_at** | **str** |  | 
**recent_errors** | **List[Optional[Dict[str, object]]]** |  | 

## Example

```python
from spatialflow_generated.models.integration_stats_schema import IntegrationStatsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationStatsSchema from a JSON string
integration_stats_schema_instance = IntegrationStatsSchema.from_json(json)
# print the JSON string representation of the object
print(IntegrationStatsSchema.to_json())

# convert the object into a dict
integration_stats_schema_dict = integration_stats_schema_instance.to_dict()
# create an instance of IntegrationStatsSchema from a dict
integration_stats_schema_from_dict = IntegrationStatsSchema.from_dict(integration_stats_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


