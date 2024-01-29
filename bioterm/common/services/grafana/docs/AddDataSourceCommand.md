# AddDataSourceCommand

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
**with_credentials** | **bool** |  | [optional] 

## Example

```python
from grafanaApiClient.models.add_data_source_command import AddDataSourceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AddDataSourceCommand from a JSON string
add_data_source_command_instance = AddDataSourceCommand.from_json(json)
# print the JSON string representation of the object
print AddDataSourceCommand.to_json()

# convert the object into a dict
add_data_source_command_dict = add_data_source_command_instance.to_dict()
# create an instance of AddDataSourceCommand from a dict
add_data_source_command_form_dict = add_data_source_command.from_dict(add_data_source_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


