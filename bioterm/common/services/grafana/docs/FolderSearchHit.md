# FolderSearchHit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**parent_uid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.folder_search_hit import FolderSearchHit

# TODO update the JSON string below
json = "{}"
# create an instance of FolderSearchHit from a JSON string
folder_search_hit_instance = FolderSearchHit.from_json(json)
# print the JSON string representation of the object
print FolderSearchHit.to_json()

# convert the object into a dict
folder_search_hit_dict = folder_search_hit_instance.to_dict()
# create an instance of FolderSearchHit from a dict
folder_search_hit_form_dict = folder_search_hit.from_dict(folder_search_hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


