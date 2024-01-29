# CreateFolderCommand

CreateFolderCommand captures the information required by the folder service to create a folder.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**parent_uid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_folder_command import CreateFolderCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFolderCommand from a JSON string
create_folder_command_instance = CreateFolderCommand.from_json(json)
# print the JSON string representation of the object
print CreateFolderCommand.to_json()

# convert the object into a dict
create_folder_command_dict = create_folder_command_instance.to_dict()
# create an instance of CreateFolderCommand from a dict
create_folder_command_form_dict = create_folder_command.from_dict(create_folder_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


