# IntegrationTypeRequest

Request schema for creating/updating integration types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Unique identifier for this integration type | 
**name** | **str** | Display name for this integration type | 
**description** | **str** | User-friendly description | 
**icon** | **str** | Icon identifier for UI display | [optional] [default to 'default']
**category** | **str** | Category: general, communication, cloud, analytics, automation, custom | [optional] [default to 'general']
**handler_class** | **str** | Python path to the action handler class | 
**validator_class** | **str** |  | [optional] 
**oauth_enabled** | **bool** | Whether this integration supports OAuth authentication | [optional] [default to False]
**oauth_config** | **Dict[str, object]** | OAuth configuration | [optional] 
**documentation_url** | **str** |  | [optional] 
**is_active** | **bool** | Whether this integration type is available for use | [optional] [default to True]

## Example

```python
from spatialflow_generated.models.integration_type_request import IntegrationTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationTypeRequest from a JSON string
integration_type_request_instance = IntegrationTypeRequest.from_json(json)
# print the JSON string representation of the object
print(IntegrationTypeRequest.to_json())

# convert the object into a dict
integration_type_request_dict = integration_type_request_instance.to_dict()
# create an instance of IntegrationTypeRequest from a dict
integration_type_request_from_dict = IntegrationTypeRequest.from_dict(integration_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


