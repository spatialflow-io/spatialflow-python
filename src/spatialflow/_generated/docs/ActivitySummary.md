# ActivitySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_type** | **str** |  | 
**count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.activity_summary import ActivitySummary

# TODO update the JSON string below
json = "{}"
# create an instance of ActivitySummary from a JSON string
activity_summary_instance = ActivitySummary.from_json(json)
# print the JSON string representation of the object
print(ActivitySummary.to_json())

# convert the object into a dict
activity_summary_dict = activity_summary_instance.to_dict()
# create an instance of ActivitySummary from a dict
activity_summary_from_dict = ActivitySummary.from_dict(activity_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


