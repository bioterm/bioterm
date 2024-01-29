# UpdateDashboardACLCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DashboardACLUpdateItem]**](DashboardACLUpdateItem.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_dashboard_acl_command import UpdateDashboardACLCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDashboardACLCommand from a JSON string
update_dashboard_acl_command_instance = UpdateDashboardACLCommand.from_json(json)
# print the JSON string representation of the object
print UpdateDashboardACLCommand.to_json()

# convert the object into a dict
update_dashboard_acl_command_dict = update_dashboard_acl_command_instance.to_dict()
# create an instance of UpdateDashboardACLCommand from a dict
update_dashboard_acl_command_form_dict = update_dashboard_acl_command.from_dict(update_dashboard_acl_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


