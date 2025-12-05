# PortalSessionResponse

Response with portal session URL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Customer portal URL | 

## Example

```python
from spatialflow_generated.models.portal_session_response import PortalSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PortalSessionResponse from a JSON string
portal_session_response_instance = PortalSessionResponse.from_json(json)
# print the JSON string representation of the object
print(PortalSessionResponse.to_json())

# convert the object into a dict
portal_session_response_dict = portal_session_response_instance.to_dict()
# create an instance of PortalSessionResponse from a dict
portal_session_response_from_dict = PortalSessionResponse.from_dict(portal_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


