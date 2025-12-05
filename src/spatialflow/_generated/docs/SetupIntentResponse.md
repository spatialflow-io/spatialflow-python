# SetupIntentResponse

Stripe setup intent response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** |  | 

## Example

```python
from spatialflow_generated.models.setup_intent_response import SetupIntentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetupIntentResponse from a JSON string
setup_intent_response_instance = SetupIntentResponse.from_json(json)
# print the JSON string representation of the object
print(SetupIntentResponse.to_json())

# convert the object into a dict
setup_intent_response_dict = setup_intent_response_instance.to_dict()
# create an instance of SetupIntentResponse from a dict
setup_intent_response_from_dict = SetupIntentResponse.from_dict(setup_intent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


