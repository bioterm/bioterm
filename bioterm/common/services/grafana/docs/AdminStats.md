# AdminStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_admins** | **int** |  | [optional] 
**active_devices** | **int** |  | [optional] 
**active_editors** | **int** |  | [optional] 
**active_sessions** | **int** |  | [optional] 
**active_users** | **int** |  | [optional] 
**active_viewers** | **int** |  | [optional] 
**admins** | **int** |  | [optional] 
**alerts** | **int** |  | [optional] 
**daily_active_admins** | **int** |  | [optional] 
**daily_active_editors** | **int** |  | [optional] 
**daily_active_sessions** | **int** |  | [optional] 
**daily_active_users** | **int** |  | [optional] 
**daily_active_viewers** | **int** |  | [optional] 
**dashboards** | **int** |  | [optional] 
**datasources** | **int** |  | [optional] 
**editors** | **int** |  | [optional] 
**monthly_active_users** | **int** |  | [optional] 
**orgs** | **int** |  | [optional] 
**playlists** | **int** |  | [optional] 
**snapshots** | **int** |  | [optional] 
**stars** | **int** |  | [optional] 
**tags** | **int** |  | [optional] 
**users** | **int** |  | [optional] 
**viewers** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.admin_stats import AdminStats

# TODO update the JSON string below
json = "{}"
# create an instance of AdminStats from a JSON string
admin_stats_instance = AdminStats.from_json(json)
# print the JSON string representation of the object
print AdminStats.to_json()

# convert the object into a dict
admin_stats_dict = admin_stats_instance.to_dict()
# create an instance of AdminStats from a dict
admin_stats_form_dict = admin_stats.from_dict(admin_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


