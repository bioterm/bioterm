# UpdateRoleCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**var_global** | **bool** |  | [optional] 
**group** | **str** |  | [optional] 
**hidden** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_role_command import UpdateRoleCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoleCommand from a JSON string
update_role_command_instance = UpdateRoleCommand.from_json(json)
# print the JSON string representation of the object
print UpdateRoleCommand.to_json()

# convert the object into a dict
update_role_command_dict = update_role_command_instance.to_dict()
# create an instance of UpdateRoleCommand from a dict
update_role_command_form_dict = update_role_command.from_dict(update_role_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


