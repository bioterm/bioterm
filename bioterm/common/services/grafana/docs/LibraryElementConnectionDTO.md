# LibraryElementConnectionDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **int** |  | [optional] 
**connection_uid** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**created_by** | [**LibraryElementDTOMetaUser**](LibraryElementDTOMetaUser.md) |  | [optional] 
**element_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**kind** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.library_element_connection_dto import LibraryElementConnectionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryElementConnectionDTO from a JSON string
library_element_connection_dto_instance = LibraryElementConnectionDTO.from_json(json)
# print the JSON string representation of the object
print LibraryElementConnectionDTO.to_json()

# convert the object into a dict
library_element_connection_dto_dict = library_element_connection_dto_instance.to_dict()
# create an instance of LibraryElementConnectionDTO from a dict
library_element_connection_dto_form_dict = library_element_connection_dto.from_dict(library_element_connection_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


