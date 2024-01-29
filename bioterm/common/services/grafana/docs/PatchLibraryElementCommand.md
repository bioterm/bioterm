# PatchLibraryElementCommand

PatchLibraryElementCommand is the command for patching a LibraryElement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **int** | ID of the folder where the library element is stored.  Deprecated: use FolderUID instead | [optional] 
**folder_uid** | **str** | UID of the folder where the library element is stored. | [optional] 
**kind** | **int** | Kind of element to create, Use 1 for library panels or 2 for c. Description: 1 - library panels 2 - library variables | [optional] 
**model** | **object** | The JSON model for the library element. | [optional] 
**name** | **str** | Name of the library element. | [optional] 
**uid** | **str** |  | [optional] 
**version** | **int** | Version of the library element you are updating. | [optional] 

## Example

```python
from grafanaApiClient.models.patch_library_element_command import PatchLibraryElementCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PatchLibraryElementCommand from a JSON string
patch_library_element_command_instance = PatchLibraryElementCommand.from_json(json)
# print the JSON string representation of the object
print PatchLibraryElementCommand.to_json()

# convert the object into a dict
patch_library_element_command_dict = patch_library_element_command_instance.to_dict()
# create an instance of PatchLibraryElementCommand from a dict
patch_library_element_command_form_dict = patch_library_element_command.from_dict(patch_library_element_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


