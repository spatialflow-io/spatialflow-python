# MarketingSubscriber

Single marketing subscriber for export.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**subscribed_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.marketing_subscriber import MarketingSubscriber

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingSubscriber from a JSON string
marketing_subscriber_instance = MarketingSubscriber.from_json(json)
# print the JSON string representation of the object
print(MarketingSubscriber.to_json())

# convert the object into a dict
marketing_subscriber_dict = marketing_subscriber_instance.to_dict()
# create an instance of MarketingSubscriber from a dict
marketing_subscriber_from_dict = MarketingSubscriber.from_dict(marketing_subscriber_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


