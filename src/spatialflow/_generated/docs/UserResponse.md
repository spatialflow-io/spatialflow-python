# UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**email_verified** | **bool** |  | 
**selected_plan** | **str** |  | 
**company** | **str** |  | 
**language_preference** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**is_superuser** | **bool** |  | 
**is_staff** | **bool** |  | 
**roles** | **List[str]** |  | 
**is_beta_user** | **bool** |  | [optional] 
**admin_approved** | **bool** |  | [optional] 
**admin_approved_at** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print(UserResponse.to_json())

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_from_dict = UserResponse.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


