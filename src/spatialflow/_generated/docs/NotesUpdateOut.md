# NotesUpdateOut

Response after updating session notes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**notes** | **str** |  | 

## Example

```python
from spatialflow_generated.models.notes_update_out import NotesUpdateOut

# TODO update the JSON string below
json = "{}"
# create an instance of NotesUpdateOut from a JSON string
notes_update_out_instance = NotesUpdateOut.from_json(json)
# print the JSON string representation of the object
print(NotesUpdateOut.to_json())

# convert the object into a dict
notes_update_out_dict = notes_update_out_instance.to_dict()
# create an instance of NotesUpdateOut from a dict
notes_update_out_from_dict = NotesUpdateOut.from_dict(notes_update_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


