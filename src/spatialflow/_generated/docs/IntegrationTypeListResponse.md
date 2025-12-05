# IntegrationTypeListResponse

Response schema for paginated list of integration types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[IntegrationTypeResponse]**](IntegrationTypeResponse.md) |  | 
**total** | **int** |  | 
**page** | **int** |  | 
**page_size** | **int** |  | 
**pages** | **int** |  | 

## Example

```python
from spatialflow_generated.models.integration_type_list_response import IntegrationTypeListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationTypeListResponse from a JSON string
integration_type_list_response_instance = IntegrationTypeListResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationTypeListResponse.to_json())

# convert the object into a dict
integration_type_list_response_dict = integration_type_list_response_instance.to_dict()
# create an instance of IntegrationTypeListResponse from a dict
integration_type_list_response_from_dict = IntegrationTypeListResponse.from_dict(integration_type_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


