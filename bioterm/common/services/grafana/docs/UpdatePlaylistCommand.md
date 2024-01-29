# UpdatePlaylistCommand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** |  | [optional] 
**items** | [**List[PlaylistItem]**](PlaylistItem.md) |  | [optional] 
**name** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_playlist_command import UpdatePlaylistCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlaylistCommand from a JSON string
update_playlist_command_instance = UpdatePlaylistCommand.from_json(json)
# print the JSON string representation of the object
print UpdatePlaylistCommand.to_json()

# convert the object into a dict
update_playlist_command_dict = update_playlist_command_instance.to_dict()
# create an instance of UpdatePlaylistCommand from a dict
update_playlist_command_form_dict = update_playlist_command.from_dict(update_playlist_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


