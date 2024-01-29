# PatchPrefsCmd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookies** | **List[str]** |  | [optional] 
**home_dashboard_id** | **int** | The numerical :id of a favorited dashboard | [optional] [default to 0]
**home_dashboard_uid** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**query_history** | [**QueryHistoryPreference**](QueryHistoryPreference.md) |  | [optional] 
**theme** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**week_start** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.patch_prefs_cmd import PatchPrefsCmd

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPrefsCmd from a JSON string
patch_prefs_cmd_instance = PatchPrefsCmd.from_json(json)
# print the JSON string representation of the object
print PatchPrefsCmd.to_json()

# convert the object into a dict
patch_prefs_cmd_dict = patch_prefs_cmd_instance.to_dict()
# create an instance of PatchPrefsCmd from a dict
patch_prefs_cmd_form_dict = patch_prefs_cmd.from_dict(patch_prefs_cmd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


