# SetRoleAssignmentsCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_accounts** | **List[int]** |  | [optional] 
**teams** | **List[int]** |  | [optional] 
**users** | **List[int]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.set_role_assignments_command import SetRoleAssignmentsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SetRoleAssignmentsCommand from a JSON string
set_role_assignments_command_instance = SetRoleAssignmentsCommand.from_json(json)
# print the JSON string representation of the object
print SetRoleAssignmentsCommand.to_json()

# convert the object into a dict
set_role_assignments_command_dict = set_role_assignments_command_instance.to_dict()
# create an instance of SetRoleAssignmentsCommand from a dict
set_role_assignments_command_form_dict = set_role_assignments_command.from_dict(set_role_assignments_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


