# ApiDocsOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openapi** | **str** |  | 
**info** | **Dict[str, object]** |  | 
**servers** | **List[Dict[str, object]]** |  | 

## Example

```python
from spatialflow_generated.models.api_docs_out import ApiDocsOut

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDocsOut from a JSON string
api_docs_out_instance = ApiDocsOut.from_json(json)
# print the JSON string representation of the object
print(ApiDocsOut.to_json())

# convert the object into a dict
api_docs_out_dict = api_docs_out_instance.to_dict()
# create an instance of ApiDocsOut from a dict
api_docs_out_from_dict = ApiDocsOut.from_dict(api_docs_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


