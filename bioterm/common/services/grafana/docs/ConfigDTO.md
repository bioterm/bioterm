# ConfigDTO

ConfigDTO is model representation in transfer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**dashboard_id** | **int** |  | [optional] 
**dashboard_name** | **str** |  | [optional] 
**dashboard_uid** | **str** |  | [optional] 
**dashboards** | [**List[DashboardDTO]**](DashboardDTO.md) |  | [optional] 
**enable_csv** | **bool** |  | [optional] 
**enable_dashboard_url** | **bool** |  | [optional] 
**formats** | **List[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**ReportOptionsDTO**](ReportOptionsDTO.md) |  | [optional] 
**org_id** | **int** |  | [optional] 
**recipients** | **str** |  | [optional] 
**reply_to** | **str** |  | [optional] 
**scale_factor** | **int** |  | [optional] 
**schedule** | [**ScheduleDTO**](ScheduleDTO.md) |  | [optional] 
**state** | **str** |  | [optional] 
**template_vars** | **object** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.config_dto import ConfigDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigDTO from a JSON string
config_dto_instance = ConfigDTO.from_json(json)
# print the JSON string representation of the object
print ConfigDTO.to_json()

# convert the object into a dict
config_dto_dict = config_dto_instance.to_dict()
# create an instance of ConfigDTO from a dict
config_dto_form_dict = config_dto.from_dict(config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


