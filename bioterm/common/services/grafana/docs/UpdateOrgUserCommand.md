# UpdateOrgUserCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_org_user_command import UpdateOrgUserCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrgUserCommand from a JSON string
update_org_user_command_instance = UpdateOrgUserCommand.from_json(json)
# print the JSON string representation of the object
print UpdateOrgUserCommand.to_json()

# convert the object into a dict
update_org_user_command_dict = update_org_user_command_instance.to_dict()
# create an instance of UpdateOrgUserCommand from a dict
update_org_user_command_form_dict = update_org_user_command.from_dict(update_org_user_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


