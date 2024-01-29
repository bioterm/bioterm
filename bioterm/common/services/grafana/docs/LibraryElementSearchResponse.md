# LibraryElementSearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**LibraryElementSearchResult**](LibraryElementSearchResult.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.library_element_search_response import LibraryElementSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryElementSearchResponse from a JSON string
library_element_search_response_instance = LibraryElementSearchResponse.from_json(json)
# print the JSON string representation of the object
print LibraryElementSearchResponse.to_json()

# convert the object into a dict
library_element_search_response_dict = library_element_search_response_instance.to_dict()
# create an instance of LibraryElementSearchResponse from a dict
library_element_search_response_form_dict = library_element_search_response.from_dict(library_element_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


