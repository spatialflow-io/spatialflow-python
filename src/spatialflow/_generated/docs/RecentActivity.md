# RecentActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** |  | 
**timestamp** | **str** |  | 
**metadata** | **Dict[str, object]** |  | 

## Example

```python
from spatialflow_generated.models.recent_activity import RecentActivity

# TODO update the JSON string below
json = "{}"
# create an instance of RecentActivity from a JSON string
recent_activity_instance = RecentActivity.from_json(json)
# print the JSON string representation of the object
print(RecentActivity.to_json())

# convert the object into a dict
recent_activity_dict = recent_activity_instance.to_dict()
# create an instance of RecentActivity from a dict
recent_activity_from_dict = RecentActivity.from_dict(recent_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


