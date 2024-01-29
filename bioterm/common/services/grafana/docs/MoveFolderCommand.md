# MoveFolderCommand

MoveFolderCommand captures the information required by the folder service to move a folder.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.move_folder_command import MoveFolderCommand

# TODO update the JSON string below
json = "{}"
# create an instance of MoveFolderCommand from a JSON string
move_folder_command_instance = MoveFolderCommand.from_json(json)
# print the JSON string representation of the object
print MoveFolderCommand.to_json()

# convert the object into a dict
move_folder_command_dict = move_folder_command_instance.to_dict()
# create an instance of MoveFolderCommand from a dict
move_folder_command_form_dict = move_folder_command.from_dict(move_folder_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


