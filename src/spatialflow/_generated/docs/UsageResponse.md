# UsageResponse

Response schema for workspace usage metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_events** | **int** |  | 
**action_deliveries** | **int** |  | 
**event_units** | **float** |  | 
**tier** | **str** |  | 
**tier_limit** | **int** |  | 
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.usage_response import UsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageResponse from a JSON string
usage_response_instance = UsageResponse.from_json(json)
# print the JSON string representation of the object
print(UsageResponse.to_json())

# convert the object into a dict
usage_response_dict = usage_response_instance.to_dict()
# create an instance of UsageResponse from a dict
usage_response_from_dict = UsageResponse.from_dict(usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


