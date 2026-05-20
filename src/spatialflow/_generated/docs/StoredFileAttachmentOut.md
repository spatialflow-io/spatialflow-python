# StoredFileAttachmentOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**file_key** | **str** |  | 
**original_name** | **str** |  | 
**content_type** | **str** |  | 
**size_bytes** | **int** |  | 
**created_at** | **datetime** |  | 
**related_object_id** | **str** |  | 

## Example

```python
from spatialflow_generated.models.stored_file_attachment_out import StoredFileAttachmentOut

# TODO update the JSON string below
json = "{}"
# create an instance of StoredFileAttachmentOut from a JSON string
stored_file_attachment_out_instance = StoredFileAttachmentOut.from_json(json)
# print the JSON string representation of the object
print(StoredFileAttachmentOut.to_json())

# convert the object into a dict
stored_file_attachment_out_dict = stored_file_attachment_out_instance.to_dict()
# create an instance of StoredFileAttachmentOut from a dict
stored_file_attachment_out_from_dict = StoredFileAttachmentOut.from_dict(stored_file_attachment_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


