# BadgeCountsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incidents_open** | **int** |  | 
**dlq_pending** | **int** |  | [optional] 
**integrations_degraded** | **int** |  | 

## Example

```python
from spatialflow_generated.models.badge_counts_out import BadgeCountsOut

# TODO update the JSON string below
json = "{}"
# create an instance of BadgeCountsOut from a JSON string
badge_counts_out_instance = BadgeCountsOut.from_json(json)
# print the JSON string representation of the object
print(BadgeCountsOut.to_json())

# convert the object into a dict
badge_counts_out_dict = badge_counts_out_instance.to_dict()
# create an instance of BadgeCountsOut from a dict
badge_counts_out_from_dict = BadgeCountsOut.from_dict(badge_counts_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


