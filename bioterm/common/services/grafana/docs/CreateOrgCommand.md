# CreateOrgCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_org_command import CreateOrgCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrgCommand from a JSON string
create_org_command_instance = CreateOrgCommand.from_json(json)
# print the JSON string representation of the object
print CreateOrgCommand.to_json()

# convert the object into a dict
create_org_command_dict = create_org_command_instance.to_dict()
# create an instance of CreateOrgCommand from a dict
create_org_command_form_dict = create_org_command.from_dict(create_org_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


