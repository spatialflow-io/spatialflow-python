# MobileTrackingConsentOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_version** | **str** |  | 
**consented_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.mobile_tracking_consent_out import MobileTrackingConsentOut

# TODO update the JSON string below
json = "{}"
# create an instance of MobileTrackingConsentOut from a JSON string
mobile_tracking_consent_out_instance = MobileTrackingConsentOut.from_json(json)
# print the JSON string representation of the object
print(MobileTrackingConsentOut.to_json())

# convert the object into a dict
mobile_tracking_consent_out_dict = mobile_tracking_consent_out_instance.to_dict()
# create an instance of MobileTrackingConsentOut from a dict
mobile_tracking_consent_out_from_dict = MobileTrackingConsentOut.from_dict(mobile_tracking_consent_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


