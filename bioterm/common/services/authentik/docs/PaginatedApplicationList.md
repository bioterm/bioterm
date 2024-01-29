# PaginatedApplicationList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginatedApplicationListPagination**](PaginatedApplicationListPagination.md) |  | 
**results** | [**List[Application]**](Application.md) |  | 

## Example

```python
from authentikApiClient.models.paginated_application_list import PaginatedApplicationList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedApplicationList from a JSON string
paginated_application_list_instance = PaginatedApplicationList.from_json(json)
# print the JSON string representation of the object
print PaginatedApplicationList.to_json()

# convert the object into a dict
paginated_application_list_dict = paginated_application_list_instance.to_dict()
# create an instance of PaginatedApplicationList from a dict
paginated_application_list_form_dict = paginated_application_list.from_dict(paginated_application_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


