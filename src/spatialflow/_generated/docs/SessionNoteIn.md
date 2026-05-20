# SessionNoteIn

Request body for the manager POST /devices/{uuid}/sessions/{session_id}/notes (D-04).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 

## Example

```python
from spatialflow_generated.models.session_note_in import SessionNoteIn

# TODO update the JSON string below
json = "{}"
# create an instance of SessionNoteIn from a JSON string
session_note_in_instance = SessionNoteIn.from_json(json)
# print the JSON string representation of the object
print(SessionNoteIn.to_json())

# convert the object into a dict
session_note_in_dict = session_note_in_instance.to_dict()
# create an instance of SessionNoteIn from a dict
session_note_in_from_dict = SessionNoteIn.from_dict(session_note_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


