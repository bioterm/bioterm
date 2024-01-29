# QueryHistorySearchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**QueryHistorySearchResult**](QueryHistorySearchResult.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.query_history_search_response import QueryHistorySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHistorySearchResponse from a JSON string
query_history_search_response_instance = QueryHistorySearchResponse.from_json(json)
# print the JSON string representation of the object
print QueryHistorySearchResponse.to_json()

# convert the object into a dict
query_history_search_response_dict = query_history_search_response_instance.to_dict()
# create an instance of QueryHistorySearchResponse from a dict
query_history_search_response_form_dict = query_history_search_response.from_dict(query_history_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


