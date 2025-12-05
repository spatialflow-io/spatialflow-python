# UnsubscribeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**email** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.unsubscribe_response import UnsubscribeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnsubscribeResponse from a JSON string
unsubscribe_response_instance = UnsubscribeResponse.from_json(json)
# print the JSON string representation of the object
print(UnsubscribeResponse.to_json())

# convert the object into a dict
unsubscribe_response_dict = unsubscribe_response_instance.to_dict()
# create an instance of UnsubscribeResponse from a dict
unsubscribe_response_from_dict = UnsubscribeResponse.from_dict(unsubscribe_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


