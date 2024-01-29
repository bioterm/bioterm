# LibraryElementConnectionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**List[LibraryElementConnectionDTO]**](LibraryElementConnectionDTO.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.library_element_connections_response import LibraryElementConnectionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LibraryElementConnectionsResponse from a JSON string
library_element_connections_response_instance = LibraryElementConnectionsResponse.from_json(json)
# print the JSON string representation of the object
print LibraryElementConnectionsResponse.to_json()

# convert the object into a dict
library_element_connections_response_dict = library_element_connections_response_instance.to_dict()
# create an instance of LibraryElementConnectionsResponse from a dict
library_element_connections_response_form_dict = library_element_connections_response.from_dict(library_element_connections_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


