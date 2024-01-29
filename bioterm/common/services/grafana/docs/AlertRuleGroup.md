# AlertRuleGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_uid** | **str** |  | [optional] 
**interval** | **int** |  | [optional] 
**rules** | [**List[ProvisionedAlertRule]**](ProvisionedAlertRule.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_rule_group import AlertRuleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRuleGroup from a JSON string
alert_rule_group_instance = AlertRuleGroup.from_json(json)
# print the JSON string representation of the object
print AlertRuleGroup.to_json()

# convert the object into a dict
alert_rule_group_dict = alert_rule_group_instance.to_dict()
# create an instance of AlertRuleGroup from a dict
alert_rule_group_form_dict = alert_rule_group.from_dict(alert_rule_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


