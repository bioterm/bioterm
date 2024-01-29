# SetUserRolesCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_global** | **bool** |  | [optional] 
**include_hidden** | **bool** |  | [optional] 
**role_uids** | **List[str]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.set_user_roles_command import SetUserRolesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserRolesCommand from a JSON string
set_user_roles_command_instance = SetUserRolesCommand.from_json(json)
# print the JSON string representation of the object
print SetUserRolesCommand.to_json()

# convert the object into a dict
set_user_roles_command_dict = set_user_roles_command_instance.to_dict()
# create an instance of SetUserRolesCommand from a dict
set_user_roles_command_form_dict = set_user_roles_command.from_dict(set_user_roles_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


