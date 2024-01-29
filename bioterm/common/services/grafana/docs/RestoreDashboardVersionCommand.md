# RestoreDashboardVersionCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.restore_dashboard_version_command import RestoreDashboardVersionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RestoreDashboardVersionCommand from a JSON string
restore_dashboard_version_command_instance = RestoreDashboardVersionCommand.from_json(json)
# print the JSON string representation of the object
print RestoreDashboardVersionCommand.to_json()

# convert the object into a dict
restore_dashboard_version_command_dict = restore_dashboard_version_command_instance.to_dict()
# create an instance of RestoreDashboardVersionCommand from a dict
restore_dashboard_version_command_form_dict = restore_dashboard_version_command.from_dict(restore_dashboard_version_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


