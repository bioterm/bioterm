# PaginatedPropertyMappingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedApplicationListPagination**](PaginatedApplicationListPagination.md) |  | 
**results** | [**List[PropertyMapping]**](PropertyMapping.md) |  | 

## Example

```python
from authentikApiClient.models.paginated_property_mapping_list import PaginatedPropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPropertyMappingList from a JSON string
paginated_property_mapping_list_instance = PaginatedPropertyMappingList.from_json(json)
# print the JSON string representation of the object
print PaginatedPropertyMappingList.to_json()

# convert the object into a dict
paginated_property_mapping_list_dict = paginated_property_mapping_list_instance.to_dict()
# create an instance of PaginatedPropertyMappingList from a dict
paginated_property_mapping_list_form_dict = paginated_property_mapping_list.from_dict(paginated_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


