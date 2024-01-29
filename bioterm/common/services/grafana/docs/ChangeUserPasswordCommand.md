# ChangeUserPasswordCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** |  | [optional] 
**old_password** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.change_user_password_command import ChangeUserPasswordCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeUserPasswordCommand from a JSON string
change_user_password_command_instance = ChangeUserPasswordCommand.from_json(json)
# print the JSON string representation of the object
print ChangeUserPasswordCommand.to_json()

# convert the object into a dict
change_user_password_command_dict = change_user_password_command_instance.to_dict()
# create an instance of ChangeUserPasswordCommand from a dict
change_user_password_command_form_dict = change_user_password_command.from_dict(change_user_password_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


