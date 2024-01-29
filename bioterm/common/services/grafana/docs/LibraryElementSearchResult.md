# LibraryElementSearchResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**List[LibraryElementDTO]**](LibraryElementDTO.md) |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.library_element_search_result import LibraryElementSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryElementSearchResult from a JSON string
library_element_search_result_instance = LibraryElementSearchResult.from_json(json)
# print the JSON string representation of the object
print LibraryElementSearchResult.to_json()

# convert the object into a dict
library_element_search_result_dict = library_element_search_result_instance.to_dict()
# create an instance of LibraryElementSearchResult from a dict
library_element_search_result_form_dict = library_element_search_result.from_dict(library_element_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


