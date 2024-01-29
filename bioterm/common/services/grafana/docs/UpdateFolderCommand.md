# UpdateFolderCommand

UpdateFolderCommand captures the information required by the folder service to update a folder. Use Move to update a folder's parent folder.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | NewDescription it&#39;s an optional parameter used for overriding the existing folder description | [optional] 
**overwrite** | **bool** | Overwrite only used by the legacy folder implementation | [optional] 
**title** | **str** | NewTitle it&#39;s an optional parameter used for overriding the existing folder title | [optional] 
**version** | **int** | Version only used by the legacy folder implementation | [optional] 

## Example

```python
from grafanaApiClient.models.update_folder_command import UpdateFolderCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFolderCommand from a JSON string
update_folder_command_instance = UpdateFolderCommand.from_json(json)
# print the JSON string representation of the object
print UpdateFolderCommand.to_json()

# convert the object into a dict
update_folder_command_dict = update_folder_command_instance.to_dict()
# create an instance of UpdateFolderCommand from a dict
update_folder_command_form_dict = update_folder_command.from_dict(update_folder_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


