# ReportEmailDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**emails** | **str** | Comma-separated list of emails to which to send the report to. | [optional] 
**id** | **str** | Send the report to the emails specified in the report. Required if emails is not present. | [optional] 
**use_emails_from_report** | **bool** | Send the report to the emails specified in the report. Required if emails is not present. | [optional] 

## Example

```python
from grafanaApiClient.models.report_email_dto import ReportEmailDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ReportEmailDTO from a JSON string
report_email_dto_instance = ReportEmailDTO.from_json(json)
# print the JSON string representation of the object
print ReportEmailDTO.to_json()

# convert the object into a dict
report_email_dto_dict = report_email_dto_instance.to_dict()
# create an instance of ReportEmailDTO from a dict
report_email_dto_form_dict = report_email_dto.from_dict(report_email_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


