# LibraryElementDTOMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_dashboards** | **int** |  | [optional] 
**created** | **datetime** |  | [optional] 
**created_by** | [**LibraryElementDTOMetaUser**](LibraryElementDTOMetaUser.md) |  | [optional] 
**folder_name** | **str** |  | [optional] 
**folder_uid** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**updated_by** | [**LibraryElementDTOMetaUser**](LibraryElementDTOMetaUser.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.library_element_dto_meta import LibraryElementDTOMeta

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryElementDTOMeta from a JSON string
library_element_dto_meta_instance = LibraryElementDTOMeta.from_json(json)
# print the JSON string representation of the object
print LibraryElementDTOMeta.to_json()

# convert the object into a dict
library_element_dto_meta_dict = library_element_dto_meta_instance.to_dict()
# create an instance of LibraryElementDTOMeta from a dict
library_element_dto_meta_form_dict = library_element_dto_meta.from_dict(library_element_dto_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


