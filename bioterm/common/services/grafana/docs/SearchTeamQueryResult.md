# SearchTeamQueryResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**teams** | [**List[TeamDTO]**](TeamDTO.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.search_team_query_result import SearchTeamQueryResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTeamQueryResult from a JSON string
search_team_query_result_instance = SearchTeamQueryResult.from_json(json)
# print the JSON string representation of the object
print SearchTeamQueryResult.to_json()

# convert the object into a dict
search_team_query_result_dict = search_team_query_result_instance.to_dict()
# create an instance of SearchTeamQueryResult from a dict
search_team_query_result_form_dict = search_team_query_result.from_dict(search_team_query_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


