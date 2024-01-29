# PaginatedApplicationListPagination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **float** |  | 
**previous** | **float** |  | 
**count** | **float** |  | 
**current** | **float** |  | 
**total_pages** | **float** |  | 
**start_index** | **float** |  | 
**end_index** | **float** |  | 

## Example

```python
from authentikApiClient.models.paginated_application_list_pagination import PaginatedApplicationListPagination

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedApplicationListPagination from a JSON string
paginated_application_list_pagination_instance = PaginatedApplicationListPagination.from_json(json)
# print the JSON string representation of the object
print PaginatedApplicationListPagination.to_json()

# convert the object into a dict
paginated_application_list_pagination_dict = paginated_application_list_pagination_instance.to_dict()
# create an instance of PaginatedApplicationListPagination from a dict
paginated_application_list_pagination_form_dict = paginated_application_list_pagination.from_dict(paginated_application_list_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


