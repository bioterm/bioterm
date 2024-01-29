# PlaylistDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** | Interval sets the time between switching views in a playlist. | [optional] 
**items** | [**List[PlaylistItemDTO]**](PlaylistItemDTO.md) | The ordered list of items that the playlist will iterate over. | [optional] 
**name** | **str** | Name of the playlist. | [optional] 
**uid** | **str** | Unique playlist identifier. Generated on creation, either by the creator of the playlist of by the application. | [optional] 

## Example

```python
from grafanaApiClient.models.playlist_dto import PlaylistDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistDTO from a JSON string
playlist_dto_instance = PlaylistDTO.from_json(json)
# print the JSON string representation of the object
print PlaylistDTO.to_json()

# convert the object into a dict
playlist_dto_dict = playlist_dto_instance.to_dict()
# create an instance of PlaylistDTO from a dict
playlist_dto_form_dict = playlist_dto.from_dict(playlist_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


