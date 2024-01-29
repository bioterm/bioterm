# CreateTeamCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_team_command import CreateTeamCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTeamCommand from a JSON string
create_team_command_instance = CreateTeamCommand.from_json(json)
# print the JSON string representation of the object
print CreateTeamCommand.to_json()

# convert the object into a dict
create_team_command_dict = create_team_command_instance.to_dict()
# create an instance of CreateTeamCommand from a dict
create_team_command_form_dict = create_team_command.from_dict(create_team_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


