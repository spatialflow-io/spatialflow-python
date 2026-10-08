# IssueReportResponse

Response after creating a private issue report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reference_id** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from spatialflow_generated.models.issue_report_response import IssueReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IssueReportResponse from a JSON string
issue_report_response_instance = IssueReportResponse.from_json(json)
# print the JSON string representation of the object
print(IssueReportResponse.to_json())

# convert the object into a dict
issue_report_response_dict = issue_report_response_instance.to_dict()
# create an instance of IssueReportResponse from a dict
issue_report_response_from_dict = IssueReportResponse.from_dict(issue_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


