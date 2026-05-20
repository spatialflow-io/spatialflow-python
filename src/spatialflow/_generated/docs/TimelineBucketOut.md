# TimelineBucketOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | 
**live_count** | **int** |  | 
**offline_stale_count** | **int** |  | 
**in_geofence_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.timeline_bucket_out import TimelineBucketOut

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineBucketOut from a JSON string
timeline_bucket_out_instance = TimelineBucketOut.from_json(json)
# print the JSON string representation of the object
print(TimelineBucketOut.to_json())

# convert the object into a dict
timeline_bucket_out_dict = timeline_bucket_out_instance.to_dict()
# create an instance of TimelineBucketOut from a dict
timeline_bucket_out_from_dict = TimelineBucketOut.from_dict(timeline_bucket_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


