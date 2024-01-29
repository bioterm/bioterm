# AddUserRoleCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_global** | **bool** |  | [optional] 
**role_uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.add_user_role_command import AddUserRoleCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AddUserRoleCommand from a JSON string
add_user_role_command_instance = AddUserRoleCommand.from_json(json)
# print the JSON string representation of the object
print AddUserRoleCommand.to_json()

# convert the object into a dict
add_user_role_command_dict = add_user_role_command_instance.to_dict()
# create an instance of AddUserRoleCommand from a dict
add_user_role_command_form_dict = add_user_role_command.from_dict(add_user_role_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


