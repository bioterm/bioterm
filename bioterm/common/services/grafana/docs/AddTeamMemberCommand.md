# AddTeamMemberCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.add_team_member_command import AddTeamMemberCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AddTeamMemberCommand from a JSON string
add_team_member_command_instance = AddTeamMemberCommand.from_json(json)
# print the JSON string representation of the object
print AddTeamMemberCommand.to_json()

# convert the object into a dict
add_team_member_command_dict = add_team_member_command_instance.to_dict()
# create an instance of AddTeamMemberCommand from a dict
add_team_member_command_form_dict = add_team_member_command.from_dict(add_team_member_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


