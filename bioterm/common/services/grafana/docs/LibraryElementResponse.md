# LibraryElementResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**LibraryElementDTO**](LibraryElementDTO.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.library_element_response import LibraryElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryElementResponse from a JSON string
library_element_response_instance = LibraryElementResponse.from_json(json)
# print the JSON string representation of the object
print LibraryElementResponse.to_json()

# convert the object into a dict
library_element_response_dict = library_element_response_instance.to_dict()
# create an instance of LibraryElementResponse from a dict
library_element_response_form_dict = library_element_response.from_dict(library_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


