# PaginatedScopeMappingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedApplicationListPagination**](PaginatedApplicationListPagination.md) |  | 
**results** | [**List[ScopeMapping]**](ScopeMapping.md) |  | 

## Example

```python
from authentikApiClient.models.paginated_scope_mapping_list import PaginatedScopeMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedScopeMappingList from a JSON string
paginated_scope_mapping_list_instance = PaginatedScopeMappingList.from_json(json)
# print the JSON string representation of the object
print PaginatedScopeMappingList.to_json()

# convert the object into a dict
paginated_scope_mapping_list_dict = paginated_scope_mapping_list_instance.to_dict()
# create an instance of PaginatedScopeMappingList from a dict
paginated_scope_mapping_list_form_dict = paginated_scope_mapping_list.from_dict(paginated_scope_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


