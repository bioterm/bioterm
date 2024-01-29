# CreatePlaylistCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** |  | [optional] 
**items** | [**List[PlaylistItem]**](PlaylistItem.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.create_playlist_command import CreatePlaylistCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlaylistCommand from a JSON string
create_playlist_command_instance = CreatePlaylistCommand.from_json(json)
# print the JSON string representation of the object
print CreatePlaylistCommand.to_json()

# convert the object into a dict
create_playlist_command_dict = create_playlist_command_instance.to_dict()
# create an instance of CreatePlaylistCommand from a dict
create_playlist_command_form_dict = create_playlist_command.from_dict(create_playlist_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


