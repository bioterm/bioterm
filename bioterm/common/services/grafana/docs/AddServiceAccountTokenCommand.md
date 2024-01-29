# AddServiceAccountTokenCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**seconds_to_live** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.add_service_account_token_command import AddServiceAccountTokenCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AddServiceAccountTokenCommand from a JSON string
add_service_account_token_command_instance = AddServiceAccountTokenCommand.from_json(json)
# print the JSON string representation of the object
print AddServiceAccountTokenCommand.to_json()

# convert the object into a dict
add_service_account_token_command_dict = add_service_account_token_command_instance.to_dict()
# create an instance of AddServiceAccountTokenCommand from a dict
add_service_account_token_command_form_dict = add_service_account_token_command.from_dict(add_service_account_token_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


