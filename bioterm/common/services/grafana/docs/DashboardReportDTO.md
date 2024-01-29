# DashboardReportDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.dashboard_report_dto import DashboardReportDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardReportDTO from a JSON string
dashboard_report_dto_instance = DashboardReportDTO.from_json(json)
# print the JSON string representation of the object
print DashboardReportDTO.to_json()

# convert the object into a dict
dashboard_report_dto_dict = dashboard_report_dto_instance.to_dict()
# create an instance of DashboardReportDTO from a dict
dashboard_report_dto_form_dict = dashboard_report_dto.from_dict(dashboard_report_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


