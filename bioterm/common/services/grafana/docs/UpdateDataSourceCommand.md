# UpdateDataSourceCommand

Also acts as api DTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** |  | [optional] 
**basic_auth** | **bool** |  | [optional] 
**basic_auth_user** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**json_data** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**secure_json_data** | **Dict[str, str]** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**with_credentials** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_data_source_command import UpdateDataSourceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDataSourceCommand from a JSON string
update_data_source_command_instance = UpdateDataSourceCommand.from_json(json)
# print the JSON string representation of the object
print UpdateDataSourceCommand.to_json()

# convert the object into a dict
update_data_source_command_dict = update_data_source_command_instance.to_dict()
# create an instance of UpdateDataSourceCommand from a dict
update_data_source_command_form_dict = update_data_source_command.from_dict(update_data_source_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


