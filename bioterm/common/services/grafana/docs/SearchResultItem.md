# SearchResultItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**basic_role** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**role_name** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**team_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.search_result_item import SearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResultItem from a JSON string
search_result_item_instance = SearchResultItem.from_json(json)
# print the JSON string representation of the object
print SearchResultItem.to_json()

# convert the object into a dict
search_result_item_dict = search_result_item_instance.to_dict()
# create an instance of SearchResultItem from a dict
search_result_item_form_dict = search_result_item.from_dict(search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


