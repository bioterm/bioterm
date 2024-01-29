# SearchUserQueryResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 
**users** | [**List[UserSearchHitDTO]**](UserSearchHitDTO.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.search_user_query_result import SearchUserQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchUserQueryResult from a JSON string
search_user_query_result_instance = SearchUserQueryResult.from_json(json)
# print the JSON string representation of the object
print SearchUserQueryResult.to_json()

# convert the object into a dict
search_user_query_result_dict = search_user_query_result_instance.to_dict()
# create an instance of SearchUserQueryResult from a dict
search_user_query_result_form_dict = search_user_query_result.from_dict(search_user_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


