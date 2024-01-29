# AddAPIKeyCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**seconds_to_live** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.add_api_key_command import AddAPIKeyCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AddAPIKeyCommand from a JSON string
add_api_key_command_instance = AddAPIKeyCommand.from_json(json)
# print the JSON string representation of the object
print AddAPIKeyCommand.to_json()

# convert the object into a dict
add_api_key_command_dict = add_api_key_command_instance.to_dict()
# create an instance of AddAPIKeyCommand from a dict
add_api_key_command_form_dict = add_api_key_command.from_dict(add_api_key_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


