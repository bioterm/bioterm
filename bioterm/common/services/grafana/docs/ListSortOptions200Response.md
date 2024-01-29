# ListSortOptions200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**meta** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.list_sort_options200_response import ListSortOptions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSortOptions200Response from a JSON string
list_sort_options200_response_instance = ListSortOptions200Response.from_json(json)
# print the JSON string representation of the object
print ListSortOptions200Response.to_json()

# convert the object into a dict
list_sort_options200_response_dict = list_sort_options200_response_instance.to_dict()
# create an instance of ListSortOptions200Response from a dict
list_sort_options200_response_form_dict = list_sort_options200_response.from_dict(list_sort_options200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


