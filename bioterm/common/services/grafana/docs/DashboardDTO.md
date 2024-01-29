# DashboardDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | [**DashboardReportDTO**](DashboardReportDTO.md) |  | [optional] 
**report_variables** | **object** |  | [optional] 
**time_range** | [**TimeRangeDTO**](TimeRangeDTO.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.dashboard_dto import DashboardDTO

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardDTO from a JSON string
dashboard_dto_instance = DashboardDTO.from_json(json)
# print the JSON string representation of the object
print DashboardDTO.to_json()

# convert the object into a dict
dashboard_dto_dict = dashboard_dto_instance.to_dict()
# create an instance of DashboardDTO from a dict
dashboard_dto_form_dict = dashboard_dto.from_dict(dashboard_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


