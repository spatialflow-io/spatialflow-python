# AnomalyDeviceOut

One entry in the GET /devices/anomaly-status response.  ``id`` is the Device.id UUID (the primary key used across the device API), NOT the client-generated ``device_id`` string. This matches the rest of the device API surface (DeviceOut.id, /devices/:device_id route, etc.).  ``anomalies`` is a non-empty subset of [\"overdue\", \"stuck\"], ordered with \"overdue\" first when both are present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**anomalies** | **List[str]** |  | 

## Example

```python
from spatialflow_generated.models.anomaly_device_out import AnomalyDeviceOut

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyDeviceOut from a JSON string
anomaly_device_out_instance = AnomalyDeviceOut.from_json(json)
# print the JSON string representation of the object
print(AnomalyDeviceOut.to_json())

# convert the object into a dict
anomaly_device_out_dict = anomaly_device_out_instance.to_dict()
# create an instance of AnomalyDeviceOut from a dict
anomaly_device_out_from_dict = AnomalyDeviceOut.from_dict(anomaly_device_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


