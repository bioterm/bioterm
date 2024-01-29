# DeleteTokenCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.delete_token_command import DeleteTokenCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteTokenCommand from a JSON string
delete_token_command_instance = DeleteTokenCommand.from_json(json)
# print the JSON string representation of the object
print DeleteTokenCommand.to_json()

# convert the object into a dict
delete_token_command_dict = delete_token_command_instance.to_dict()
# create an instance of DeleteTokenCommand from a dict
delete_token_command_form_dict = delete_token_command.from_dict(delete_token_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


