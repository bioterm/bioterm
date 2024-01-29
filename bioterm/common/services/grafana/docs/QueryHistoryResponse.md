# QueryHistoryResponse

QueryHistoryResponse is a response struct for QueryHistoryDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**QueryHistoryDTO**](QueryHistoryDTO.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.query_history_response import QueryHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHistoryResponse from a JSON string
query_history_response_instance = QueryHistoryResponse.from_json(json)
# print the JSON string representation of the object
print QueryHistoryResponse.to_json()

# convert the object into a dict
query_history_response_dict = query_history_response_instance.to_dict()
# create an instance of QueryHistoryResponse from a dict
query_history_response_form_dict = query_history_response.from_dict(query_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


