# ProvisionedAlertRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**condition** | **str** |  | 
**data** | [**List[AlertQuery]**](AlertQuery.md) |  | 
**exec_err_state** | **str** |  | 
**folder_uid** | **str** |  | 
**var_for** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | 
**id** | **int** |  | [optional] 
**is_paused** | **bool** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**no_data_state** | **str** |  | 
**org_id** | **int** |  | 
**provenance** | **str** |  | [optional] 
**rule_group** | **str** |  | 
**title** | **str** |  | 
**uid** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] [readonly] 

## Example

```python
from grafanaApiClient.models.provisioned_alert_rule import ProvisionedAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionedAlertRule from a JSON string
provisioned_alert_rule_instance = ProvisionedAlertRule.from_json(json)
# print the JSON string representation of the object
print ProvisionedAlertRule.to_json()

# convert the object into a dict
provisioned_alert_rule_dict = provisioned_alert_rule_instance.to_dict()
# create an instance of ProvisionedAlertRule from a dict
provisioned_alert_rule_form_dict = provisioned_alert_rule.from_dict(provisioned_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


