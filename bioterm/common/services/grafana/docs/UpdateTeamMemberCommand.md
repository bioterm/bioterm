# UpdateTeamMemberCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_team_member_command import UpdateTeamMemberCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamMemberCommand from a JSON string
update_team_member_command_instance = UpdateTeamMemberCommand.from_json(json)
# print the JSON string representation of the object
print UpdateTeamMemberCommand.to_json()

# convert the object into a dict
update_team_member_command_dict = update_team_member_command_instance.to_dict()
# create an instance of UpdateTeamMemberCommand from a dict
update_team_member_command_form_dict = update_team_member_command.from_dict(update_team_member_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


