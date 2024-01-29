# AlertRuleExport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**condition** | **str** |  | [optional] 
**dasboard_uid** | **str** |  | [optional] 
**data** | [**List[AlertQueryExport]**](AlertQueryExport.md) |  | [optional] 
**exec_err_state** | **str** |  | [optional] 
**var_for** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**is_paused** | **bool** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**no_data_state** | **str** |  | [optional] 
**panel_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_rule_export import AlertRuleExport

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRuleExport from a JSON string
alert_rule_export_instance = AlertRuleExport.from_json(json)
# print the JSON string representation of the object
print AlertRuleExport.to_json()

# convert the object into a dict
alert_rule_export_dict = alert_rule_export_instance.to_dict()
# create an instance of AlertRuleExport from a dict
alert_rule_export_form_dict = alert_rule_export.from_dict(alert_rule_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


