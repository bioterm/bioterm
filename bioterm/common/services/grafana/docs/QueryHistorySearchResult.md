# QueryHistorySearchResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**query_history** | [**List[QueryHistoryDTO]**](QueryHistoryDTO.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.query_history_search_result import QueryHistorySearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHistorySearchResult from a JSON string
query_history_search_result_instance = QueryHistorySearchResult.from_json(json)
# print the JSON string representation of the object
print QueryHistorySearchResult.to_json()

# convert the object into a dict
query_history_search_result_dict = query_history_search_result_instance.to_dict()
# create an instance of QueryHistorySearchResult from a dict
query_history_search_result_form_dict = query_history_search_result.from_dict(query_history_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


