# ActionResponse

Generic action response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**id** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.action_response import ActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActionResponse from a JSON string
action_response_instance = ActionResponse.from_json(json)
# print the JSON string representation of the object
print(ActionResponse.to_json())

# convert the object into a dict
action_response_dict = action_response_instance.to_dict()
# create an instance of ActionResponse from a dict
action_response_from_dict = ActionResponse.from_dict(action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


