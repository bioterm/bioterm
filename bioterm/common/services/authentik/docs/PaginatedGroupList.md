# PaginatedGroupList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedApplicationListPagination**](PaginatedApplicationListPagination.md) |  | 
**results** | [**List[Group]**](Group.md) |  | 

## Example

```python
from authentikApiClient.models.paginated_group_list import PaginatedGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupList from a JSON string
paginated_group_list_instance = PaginatedGroupList.from_json(json)
# print the JSON string representation of the object
print PaginatedGroupList.to_json()

# convert the object into a dict
paginated_group_list_dict = paginated_group_list_instance.to_dict()
# create an instance of PaginatedGroupList from a dict
paginated_group_list_form_dict = paginated_group_list.from_dict(paginated_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


