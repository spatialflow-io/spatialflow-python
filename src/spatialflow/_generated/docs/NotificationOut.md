# NotificationOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**message** | **str** |  | 
**type** | **str** |  | 
**is_read** | **bool** |  | 
**read_at** | **datetime** |  | [optional] 
**action_url** | **str** |  | [optional] 
**action_label** | **str** |  | [optional] 
**created_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.notification_out import NotificationOut

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationOut from a JSON string
notification_out_instance = NotificationOut.from_json(json)
# print the JSON string representation of the object
print(NotificationOut.to_json())

# convert the object into a dict
notification_out_dict = notification_out_instance.to_dict()
# create an instance of NotificationOut from a dict
notification_out_from_dict = NotificationOut.from_dict(notification_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


