# CreateOrUpdateConfigCmd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard_id** | **int** |  | [optional] 
**dashboard_uid** | **str** |  | [optional] 
**dashboards** | [**List[DashboardDTO]**](DashboardDTO.md) |  | [optional] 
**enable_csv** | **bool** |  | [optional] 
**enable_dashboard_url** | **bool** |  | [optional] 
**formats** | **List[str]** |  | [optional] 
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**options** | [**ReportOptionsDTO**](ReportOptionsDTO.md) |  | [optional] 
**recipients** | **str** |  | [optional] 
**reply_to** | **str** |  | [optional] 
**scale_factor** | **int** |  | [optional] 
**schedule** | [**ScheduleDTO**](ScheduleDTO.md) |  | [optional] 
**state** | **str** |  | [optional] 
**template_vars** | **object** |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_or_update_config_cmd import CreateOrUpdateConfigCmd

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateConfigCmd from a JSON string
create_or_update_config_cmd_instance = CreateOrUpdateConfigCmd.from_json(json)
# print the JSON string representation of the object
print CreateOrUpdateConfigCmd.to_json()

# convert the object into a dict
create_or_update_config_cmd_dict = create_or_update_config_cmd_instance.to_dict()
# create an instance of CreateOrUpdateConfigCmd from a dict
create_or_update_config_cmd_form_dict = create_or_update_config_cmd.from_dict(create_or_update_config_cmd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


