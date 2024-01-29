# QueryHistoryDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**created_by** | **int** |  | [optional] 
**datasource_uid** | **str** |  | [optional] 
**queries** | **object** |  | [optional] 
**starred** | **bool** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.query_history_dto import QueryHistoryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHistoryDTO from a JSON string
query_history_dto_instance = QueryHistoryDTO.from_json(json)
# print the JSON string representation of the object
print QueryHistoryDTO.to_json()

# convert the object into a dict
query_history_dto_dict = query_history_dto_instance.to_dict()
# create an instance of QueryHistoryDTO from a dict
query_history_dto_form_dict = query_history_dto.from_dict(query_history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


