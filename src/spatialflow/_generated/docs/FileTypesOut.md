# FileTypesOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_types** | [**Dict[str, FileTypeConfigOut]**](FileTypeConfigOut.md) |  | 

## Example

```python
from spatialflow_generated.models.file_types_out import FileTypesOut

# TODO update the JSON string below
json = "{}"
# create an instance of FileTypesOut from a JSON string
file_types_out_instance = FileTypesOut.from_json(json)
# print the JSON string representation of the object
print(FileTypesOut.to_json())

# convert the object into a dict
file_types_out_dict = file_types_out_instance.to_dict()
# create an instance of FileTypesOut from a dict
file_types_out_from_dict = FileTypesOut.from_dict(file_types_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


