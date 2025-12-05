# UserSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | 
**role** | **str** |  | 
**email_verified** | **bool** |  | 
**is_beta_user** | **bool** |  | [optional] [default to False]
**admin_approved** | **bool** |  | [optional] [default to False]
**admin_approved_at** | **str** |  | [optional] 
**created_at** | **str** |  | 
**last_login** | **str** |  | 
**subscription_tier** | **str** |  | [optional] [default to 'free']
**api_keys_count** | **int** |  | 
**workspace** | [**WorkspaceSummary**](WorkspaceSummary.md) |  | [optional] 

## Example

```python
from spatialflow_generated.models.user_summary import UserSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UserSummary from a JSON string
user_summary_instance = UserSummary.from_json(json)
# print the JSON string representation of the object
print(UserSummary.to_json())

# convert the object into a dict
user_summary_dict = user_summary_instance.to_dict()
# create an instance of UserSummary from a dict
user_summary_from_dict = UserSummary.from_dict(user_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


