# EmailQueueStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | **int** |  | 
**queued** | **int** |  | 
**delivered** | **int** |  | 
**failed** | **int** |  | 
**total_today** | **int** |  | 
**total_this_hour** | **int** |  | 

## Example

```python
from spatialflow_generated.models.email_queue_stats import EmailQueueStats

# TODO update the JSON string below
json = "{}"
# create an instance of EmailQueueStats from a JSON string
email_queue_stats_instance = EmailQueueStats.from_json(json)
# print the JSON string representation of the object
print(EmailQueueStats.to_json())

# convert the object into a dict
email_queue_stats_dict = email_queue_stats_instance.to_dict()
# create an instance of EmailQueueStats from a dict
email_queue_stats_from_dict = EmailQueueStats.from_dict(email_queue_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


