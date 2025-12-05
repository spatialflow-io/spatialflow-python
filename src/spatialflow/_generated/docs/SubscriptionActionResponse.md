# SubscriptionActionResponse

Response for subscription actions (cancel/reactivate).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**subscription** | [**SubscriptionResponse**](SubscriptionResponse.md) |  | [optional] 

## Example

```python
from spatialflow_generated.models.subscription_action_response import SubscriptionActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionActionResponse from a JSON string
subscription_action_response_instance = SubscriptionActionResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionActionResponse.to_json())

# convert the object into a dict
subscription_action_response_dict = subscription_action_response_instance.to_dict()
# create an instance of SubscriptionActionResponse from a dict
subscription_action_response_from_dict = SubscriptionActionResponse.from_dict(subscription_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


