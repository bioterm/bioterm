# QueryHistoryDeleteQueryResponse

QueryHistoryDeleteQueryResponse is the response struct for deleting a query from query history

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.query_history_delete_query_response import QueryHistoryDeleteQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHistoryDeleteQueryResponse from a JSON string
query_history_delete_query_response_instance = QueryHistoryDeleteQueryResponse.from_json(json)
# print the JSON string representation of the object
print QueryHistoryDeleteQueryResponse.to_json()

# convert the object into a dict
query_history_delete_query_response_dict = query_history_delete_query_response_instance.to_dict()
# create an instance of QueryHistoryDeleteQueryResponse from a dict
query_history_delete_query_response_form_dict = query_history_delete_query_response.from_dict(query_history_delete_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


