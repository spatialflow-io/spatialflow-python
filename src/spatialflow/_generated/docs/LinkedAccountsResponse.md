# LinkedAccountsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_accounts** | [**List[LinkedAccountOut]**](LinkedAccountOut.md) |  | 
**has_password** | **bool** |  | 

## Example

```python
from spatialflow_generated.models.linked_accounts_response import LinkedAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedAccountsResponse from a JSON string
linked_accounts_response_instance = LinkedAccountsResponse.from_json(json)
# print the JSON string representation of the object
print(LinkedAccountsResponse.to_json())

# convert the object into a dict
linked_accounts_response_dict = linked_accounts_response_instance.to_dict()
# create an instance of LinkedAccountsResponse from a dict
linked_accounts_response_from_dict = LinkedAccountsResponse.from_dict(linked_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


