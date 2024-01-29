# SearchOrgUsersQueryResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_users** | [**List[OrgUserDTO]**](OrgUserDTO.md) |  | [optional] 
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.search_org_users_query_result import SearchOrgUsersQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchOrgUsersQueryResult from a JSON string
search_org_users_query_result_instance = SearchOrgUsersQueryResult.from_json(json)
# print the JSON string representation of the object
print SearchOrgUsersQueryResult.to_json()

# convert the object into a dict
search_org_users_query_result_dict = search_org_users_query_result_instance.to_dict()
# create an instance of SearchOrgUsersQueryResult from a dict
search_org_users_query_result_form_dict = search_org_users_query_result.from_dict(search_org_users_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


