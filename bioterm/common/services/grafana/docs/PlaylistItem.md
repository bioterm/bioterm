# PlaylistItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**playlist_id** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.playlist_item import PlaylistItem

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistItem from a JSON string
playlist_item_instance = PlaylistItem.from_json(json)
# print the JSON string representation of the object
print PlaylistItem.to_json()

# convert the object into a dict
playlist_item_dict = playlist_item_instance.to_dict()
# create an instance of PlaylistItem from a dict
playlist_item_form_dict = playlist_item.from_dict(playlist_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


