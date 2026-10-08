# AnomalyStatusOut

Response envelope for GET /devices/anomaly-status.  Always returns a (possibly empty) ``devices`` array — never 404 for an empty workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[AnomalyDeviceOut]**](AnomalyDeviceOut.md) |  | 

## Example

```python
from spatialflow_generated.models.anomaly_status_out import AnomalyStatusOut

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyStatusOut from a JSON string
anomaly_status_out_instance = AnomalyStatusOut.from_json(json)
# print the JSON string representation of the object
print(AnomalyStatusOut.to_json())

# convert the object into a dict
anomaly_status_out_dict = anomaly_status_out_instance.to_dict()
# create an instance of AnomalyStatusOut from a dict
anomaly_status_out_from_dict = AnomalyStatusOut.from_dict(anomaly_status_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


