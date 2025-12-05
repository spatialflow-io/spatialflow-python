# ActionDeliverySuccessMetrics

Action delivery success metrics schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate** | **float** |  | [optional] 
**successful** | **int** | Number of successful action deliveries | 
**total** | **int** | Total number of action attempts | 

## Example

```python
from spatialflow_generated.models.action_delivery_success_metrics import ActionDeliverySuccessMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDeliverySuccessMetrics from a JSON string
action_delivery_success_metrics_instance = ActionDeliverySuccessMetrics.from_json(json)
# print the JSON string representation of the object
print(ActionDeliverySuccessMetrics.to_json())

# convert the object into a dict
action_delivery_success_metrics_dict = action_delivery_success_metrics_instance.to_dict()
# create an instance of ActionDeliverySuccessMetrics from a dict
action_delivery_success_metrics_from_dict = ActionDeliverySuccessMetrics.from_dict(action_delivery_success_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


