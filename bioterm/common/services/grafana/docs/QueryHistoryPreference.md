# QueryHistoryPreference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_tab** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.query_history_preference import QueryHistoryPreference

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHistoryPreference from a JSON string
query_history_preference_instance = QueryHistoryPreference.from_json(json)
# print the JSON string representation of the object
print QueryHistoryPreference.to_json()

# convert the object into a dict
query_history_preference_dict = query_history_preference_instance.to_dict()
# create an instance of QueryHistoryPreference from a dict
query_history_preference_form_dict = query_history_preference.from_dict(query_history_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


