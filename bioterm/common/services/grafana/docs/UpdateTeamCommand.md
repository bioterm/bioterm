# UpdateTeamCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_team_command import UpdateTeamCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTeamCommand from a JSON string
update_team_command_instance = UpdateTeamCommand.from_json(json)
# print the JSON string representation of the object
print UpdateTeamCommand.to_json()

# convert the object into a dict
update_team_command_dict = update_team_command_instance.to_dict()
# create an instance of UpdateTeamCommand from a dict
update_team_command_form_dict = update_team_command.from_dict(update_team_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


