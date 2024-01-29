# LibraryElementDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**folder_id** | **int** | Deprecated: use FolderUID instead | [optional] 
**folder_uid** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**kind** | **int** |  | [optional] 
**meta** | [**LibraryElementDTOMeta**](LibraryElementDTOMeta.md) |  | [optional] 
**model** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**schema_version** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.library_element_dto import LibraryElementDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryElementDTO from a JSON string
library_element_dto_instance = LibraryElementDTO.from_json(json)
# print the JSON string representation of the object
print LibraryElementDTO.to_json()

# convert the object into a dict
library_element_dto_dict = library_element_dto_instance.to_dict()
# create an instance of LibraryElementDTO from a dict
library_element_dto_form_dict = library_element_dto.from_dict(library_element_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


