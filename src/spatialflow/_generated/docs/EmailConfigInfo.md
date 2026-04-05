# EmailConfigInfo

Email configuration info for debugging.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend** | **str** |  | 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from spatialflow_generated.models.email_config_info import EmailConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConfigInfo from a JSON string
email_config_info_instance = EmailConfigInfo.from_json(json)
# print the JSON string representation of the object
print(EmailConfigInfo.to_json())

# convert the object into a dict
email_config_info_dict = email_config_info_instance.to_dict()
# create an instance of EmailConfigInfo from a dict
email_config_info_from_dict = EmailConfigInfo.from_dict(email_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


