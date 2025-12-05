# UpdateOnboardingProgressRequest

Request schema for updating onboarding progress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step** | **str** | Step to mark as complete: created_workflow, created_geofence, tested_simulator, added_device | 

## Example

```python
from spatialflow_generated.models.update_onboarding_progress_request import UpdateOnboardingProgressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOnboardingProgressRequest from a JSON string
update_onboarding_progress_request_instance = UpdateOnboardingProgressRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOnboardingProgressRequest.to_json())

# convert the object into a dict
update_onboarding_progress_request_dict = update_onboarding_progress_request_instance.to_dict()
# create an instance of UpdateOnboardingProgressRequest from a dict
update_onboarding_progress_request_from_dict = UpdateOnboardingProgressRequest.from_dict(update_onboarding_progress_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


