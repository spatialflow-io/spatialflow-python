# MarketingSubscriberExportResponse

Response for marketing subscriber export (JSON format).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscribers** | [**List[MarketingSubscriber]**](MarketingSubscriber.md) |  | 
**count** | **int** |  | 
**exported_at** | **str** |  | 

## Example

```python
from spatialflow_generated.models.marketing_subscriber_export_response import MarketingSubscriberExportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketingSubscriberExportResponse from a JSON string
marketing_subscriber_export_response_instance = MarketingSubscriberExportResponse.from_json(json)
# print the JSON string representation of the object
print(MarketingSubscriberExportResponse.to_json())

# convert the object into a dict
marketing_subscriber_export_response_dict = marketing_subscriber_export_response_instance.to_dict()
# create an instance of MarketingSubscriberExportResponse from a dict
marketing_subscriber_export_response_from_dict = MarketingSubscriberExportResponse.from_dict(marketing_subscriber_export_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


