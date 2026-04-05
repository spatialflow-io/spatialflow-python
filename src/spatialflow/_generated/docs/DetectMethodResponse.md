# DetectMethodResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | 
**workspace_slug** | **str** |  | [optional] 
**idp_name** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.detect_method_response import DetectMethodResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DetectMethodResponse from a JSON string
detect_method_response_instance = DetectMethodResponse.from_json(json)
# print the JSON string representation of the object
print(DetectMethodResponse.to_json())

# convert the object into a dict
detect_method_response_dict = detect_method_response_instance.to_dict()
# create an instance of DetectMethodResponse from a dict
detect_method_response_from_dict = DetectMethodResponse.from_dict(detect_method_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


