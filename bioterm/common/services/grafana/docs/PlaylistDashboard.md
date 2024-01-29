# PlaylistDashboard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**order** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.playlist_dashboard import PlaylistDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of PlaylistDashboard from a JSON string
playlist_dashboard_instance = PlaylistDashboard.from_json(json)
# print the JSON string representation of the object
print PlaylistDashboard.to_json()

# convert the object into a dict
playlist_dashboard_dict = playlist_dashboard_instance.to_dict()
# create an instance of PlaylistDashboard from a dict
playlist_dashboard_form_dict = playlist_dashboard.from_dict(playlist_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


