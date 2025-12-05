# PortalSessionRequest

Request to create a Stripe customer portal session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** | URL to return to after portal session | 

## Example

```python
from spatialflow_generated.models.portal_session_request import PortalSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PortalSessionRequest from a JSON string
portal_session_request_instance = PortalSessionRequest.from_json(json)
# print the JSON string representation of the object
print(PortalSessionRequest.to_json())

# convert the object into a dict
portal_session_request_dict = portal_session_request_instance.to_dict()
# create an instance of PortalSessionRequest from a dict
portal_session_request_from_dict = PortalSessionRequest.from_dict(portal_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


