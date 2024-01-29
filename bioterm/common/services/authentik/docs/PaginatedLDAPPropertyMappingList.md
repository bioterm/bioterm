# PaginatedLDAPPropertyMappingList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedApplicationListPagination**](PaginatedApplicationListPagination.md) |  | 
**results** | [**List[LDAPPropertyMapping]**](LDAPPropertyMapping.md) |  | 

## Example

```python
from authentikApiClient.models.paginated_ldap_property_mapping_list import PaginatedLDAPPropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLDAPPropertyMappingList from a JSON string
paginated_ldap_property_mapping_list_instance = PaginatedLDAPPropertyMappingList.from_json(json)
# print the JSON string representation of the object
print PaginatedLDAPPropertyMappingList.to_json()

# convert the object into a dict
paginated_ldap_property_mapping_list_dict = paginated_ldap_property_mapping_list_instance.to_dict()
# create an instance of PaginatedLDAPPropertyMappingList from a dict
paginated_ldap_property_mapping_list_form_dict = paginated_ldap_property_mapping_list.from_dict(paginated_ldap_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


