# AddOrgUserCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_or_email** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.add_org_user_command import AddOrgUserCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AddOrgUserCommand from a JSON string
add_org_user_command_instance = AddOrgUserCommand.from_json(json)
# print the JSON string representation of the object
print AddOrgUserCommand.to_json()

# convert the object into a dict
add_org_user_command_dict = add_org_user_command_instance.to_dict()
# create an instance of AddOrgUserCommand from a dict
add_org_user_command_form_dict = add_org_user_command.from_dict(add_org_user_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


