# ReportOptionsDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | **str** |  | [optional] 
**orientation** | **str** |  | [optional] 
**time_range** | [**TimeRangeDTO**](TimeRangeDTO.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.report_options_dto import ReportOptionsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ReportOptionsDTO from a JSON string
report_options_dto_instance = ReportOptionsDTO.from_json(json)
# print the JSON string representation of the object
print ReportOptionsDTO.to_json()

# convert the object into a dict
report_options_dto_dict = report_options_dto_instance.to_dict()
# create an instance of ReportOptionsDTO from a dict
report_options_dto_form_dict = report_options_dto.from_dict(report_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


