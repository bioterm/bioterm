# AddTeamRoleCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.add_team_role_command import AddTeamRoleCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AddTeamRoleCommand from a JSON string
add_team_role_command_instance = AddTeamRoleCommand.from_json(json)
# print the JSON string representation of the object
print AddTeamRoleCommand.to_json()

# convert the object into a dict
add_team_role_command_dict = add_team_role_command_instance.to_dict()
# create an instance of AddTeamRoleCommand from a dict
add_team_role_command_form_dict = add_team_role_command.from_dict(add_team_role_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


