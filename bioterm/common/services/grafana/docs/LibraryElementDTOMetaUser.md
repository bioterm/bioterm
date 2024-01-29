# LibraryElementDTOMetaUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_url** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.library_element_dto_meta_user import LibraryElementDTOMetaUser

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryElementDTOMetaUser from a JSON string
library_element_dto_meta_user_instance = LibraryElementDTOMetaUser.from_json(json)
# print the JSON string representation of the object
print LibraryElementDTOMetaUser.to_json()

# convert the object into a dict
library_element_dto_meta_user_dict = library_element_dto_meta_user_instance.to_dict()
# create an instance of LibraryElementDTOMetaUser from a dict
library_element_dto_meta_user_form_dict = library_element_dto_meta_user.from_dict(library_element_dto_meta_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


