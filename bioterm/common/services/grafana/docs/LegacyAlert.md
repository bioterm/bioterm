# LegacyAlert


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**dashboard_id** | **int** |  | [optional] 
**eval_data** | **object** |  | [optional] 
**execution_error** | **str** |  | [optional] 
**var_for** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**frequency** | **int** |  | [optional] 
**handler** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**new_state_date** | **datetime** |  | [optional] 
**org_id** | **int** |  | [optional] 
**panel_id** | **int** |  | [optional] 
**settings** | **object** |  | [optional] 
**severity** | **str** |  | [optional] 
**silenced** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**state_changes** | **int** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.legacy_alert import LegacyAlert

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyAlert from a JSON string
legacy_alert_instance = LegacyAlert.from_json(json)
# print the JSON string representation of the object
print LegacyAlert.to_json()

# convert the object into a dict
legacy_alert_dict = legacy_alert_instance.to_dict()
# create an instance of LegacyAlert from a dict
legacy_alert_form_dict = legacy_alert.from_dict(legacy_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


