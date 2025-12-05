# OnboardingProgressResponse

Response schema for onboarding progress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_workflow** | **bool** |  | 
**created_geofence** | **bool** |  | 
**tested_simulator** | **bool** |  | 
**added_device** | **bool** |  | 
**dismissed_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**is_complete** | **bool** |  | 
**completion_percentage** | **float** |  | 

## Example

```python
from spatialflow_generated.models.onboarding_progress_response import OnboardingProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingProgressResponse from a JSON string
onboarding_progress_response_instance = OnboardingProgressResponse.from_json(json)
# print the JSON string representation of the object
print(OnboardingProgressResponse.to_json())

# convert the object into a dict
onboarding_progress_response_dict = onboarding_progress_response_instance.to_dict()
# create an instance of OnboardingProgressResponse from a dict
onboarding_progress_response_from_dict = OnboardingProgressResponse.from_dict(onboarding_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


