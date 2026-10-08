# ReportOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rows** | **List[Dict[str, object]]** |  | 
**summary** | **Dict[str, object]** |  | 
**total_count** | **int** |  | 

## Example

```python
from spatialflow_generated.models.report_out import ReportOut

# TODO update the JSON string below
json = "{}"
# create an instance of ReportOut from a JSON string
report_out_instance = ReportOut.from_json(json)
# print the JSON string representation of the object
print(ReportOut.to_json())

# convert the object into a dict
report_out_dict = report_out_instance.to_dict()
# create an instance of ReportOut from a dict
report_out_from_dict = ReportOut.from_dict(report_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


