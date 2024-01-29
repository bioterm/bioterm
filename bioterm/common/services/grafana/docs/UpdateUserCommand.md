# UpdateUserCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**theme** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_user_command import UpdateUserCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserCommand from a JSON string
update_user_command_instance = UpdateUserCommand.from_json(json)
# print the JSON string representation of the object
print UpdateUserCommand.to_json()

# convert the object into a dict
update_user_command_dict = update_user_command_instance.to_dict()
# create an instance of UpdateUserCommand from a dict
update_user_command_form_dict = update_user_command.from_dict(update_user_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


