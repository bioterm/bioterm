# ActiveUserStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_admins_and_editors** | **int** |  | [optional] 
**active_users** | **int** |  | [optional] 
**active_viewers** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.active_user_stats import ActiveUserStats

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveUserStats from a JSON string
active_user_stats_instance = ActiveUserStats.from_json(json)
# print the JSON string representation of the object
print ActiveUserStats.to_json()

# convert the object into a dict
active_user_stats_dict = active_user_stats_instance.to_dict()
# create an instance of ActiveUserStats from a dict
active_user_stats_form_dict = active_user_stats.from_dict(active_user_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


