# SessionNoteOut

Response item for GET/POST /devices/{uuid}/sessions/{session_id}/notes (D-19).  ``author_id`` is None when the author user was deleted (FK on_delete=SET_NULL). ``author_name`` falls back to \"Unknown\" in that case. ``author_role`` is the live workspace role (\"field_worker\" | \"manager\" | \"owner\"); \"unknown\" when the author is None or no longer in the workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**session_id** | **str** |  | 
**author_id** | **str** |  | [optional] 
**author_name** | **str** |  | 
**author_role** | **str** |  | 
**body** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.session_note_out import SessionNoteOut

# TODO update the JSON string below
json = "{}"
# create an instance of SessionNoteOut from a JSON string
session_note_out_instance = SessionNoteOut.from_json(json)
# print the JSON string representation of the object
print(SessionNoteOut.to_json())

# convert the object into a dict
session_note_out_dict = session_note_out_instance.to_dict()
# create an instance of SessionNoteOut from a dict
session_note_out_from_dict = SessionNoteOut.from_dict(session_note_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


