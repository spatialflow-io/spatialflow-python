# IssueReportRequest

Private in-app issue report submission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**area** | **str** |  | [optional] [default to 'Other']
**title** | **str** |  | [optional] 
**description** | **str** |  | 
**steps** | **str** |  | [optional] 
**expected** | **str** |  | [optional] 
**include_diagnostics** | **bool** |  | [optional] [default to True]
**include_page** | **bool** |  | [optional] [default to True]
**include_browser** | **bool** |  | [optional] [default to True]
**include_version** | **bool** |  | [optional] [default to True]
**diagnostics** | **Dict[str, object]** |  | [optional] 
**page_url** | **str** |  | [optional] 
**browser** | **Dict[str, object]** |  | [optional] 
**app_version** | **str** |  | [optional] 

## Example

```python
from spatialflow_generated.models.issue_report_request import IssueReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssueReportRequest from a JSON string
issue_report_request_instance = IssueReportRequest.from_json(json)
# print the JSON string representation of the object
print(IssueReportRequest.to_json())

# convert the object into a dict
issue_report_request_dict = issue_report_request_instance.to_dict()
# create an instance of IssueReportRequest from a dict
issue_report_request_from_dict = IssueReportRequest.from_dict(issue_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


