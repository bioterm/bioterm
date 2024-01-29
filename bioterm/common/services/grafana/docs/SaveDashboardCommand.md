# SaveDashboardCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** |  | [optional] 
**dashboard** | **object** |  | [optional] 
**folder_id** | **int** | Deprecated: use FolderUID instead | [optional] 
**folder_uid** | **str** |  | [optional] 
**is_folder** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 
**overwrite** | **bool** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.save_dashboard_command import SaveDashboardCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SaveDashboardCommand from a JSON string
save_dashboard_command_instance = SaveDashboardCommand.from_json(json)
# print the JSON string representation of the object
print SaveDashboardCommand.to_json()

# convert the object into a dict
save_dashboard_command_dict = save_dashboard_command_instance.to_dict()
# create an instance of SaveDashboardCommand from a dict
save_dashboard_command_form_dict = save_dashboard_command.from_dict(save_dashboard_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


