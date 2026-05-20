# FileTypeConfigOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_size** | **int** |  | 
**max_size_mb** | **float** |  | 
**allowed_extensions** | **List[str]** |  | 

## Example

```python
from spatialflow_generated.models.file_type_config_out import FileTypeConfigOut

# TODO update the JSON string below
json = "{}"
# create an instance of FileTypeConfigOut from a JSON string
file_type_config_out_instance = FileTypeConfigOut.from_json(json)
# print the JSON string representation of the object
print(FileTypeConfigOut.to_json())

# convert the object into a dict
file_type_config_out_dict = file_type_config_out_instance.to_dict()
# create an instance of FileTypeConfigOut from a dict
file_type_config_out_from_dict = FileTypeConfigOut.from_dict(file_type_config_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


