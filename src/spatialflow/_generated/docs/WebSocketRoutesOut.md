# WebSocketRoutesOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**websocket_base_url** | **str** |  | 
**authentication** | **Dict[str, object]** |  | 
**endpoints** | **Dict[str, object]** |  | 
**message_formats** | **Dict[str, object]** |  | 
**response_formats** | **Dict[str, object]** |  | 

## Example

```python
from spatialflow_generated.models.web_socket_routes_out import WebSocketRoutesOut

# TODO update the JSON string below
json = "{}"
# create an instance of WebSocketRoutesOut from a JSON string
web_socket_routes_out_instance = WebSocketRoutesOut.from_json(json)
# print the JSON string representation of the object
print(WebSocketRoutesOut.to_json())

# convert the object into a dict
web_socket_routes_out_dict = web_socket_routes_out_instance.to_dict()
# create an instance of WebSocketRoutesOut from a dict
web_socket_routes_out_from_dict = WebSocketRoutesOut.from_dict(web_socket_routes_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


