# AlertingRule

adapted from cortex

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_at** | **datetime** |  | 
**alerts** | [**List[Alert]**](Alert.md) |  | [optional] 
**annotations** | **Dict[str, str]** | The custom marshaling for labels.Labels ends up doing this anyways. | 
**duration** | **float** |  | [optional] 
**evaluation_time** | **float** |  | [optional] 
**health** | **str** |  | 
**labels** | **Dict[str, str]** | The custom marshaling for labels.Labels ends up doing this anyways. | [optional] 
**last_error** | **str** |  | [optional] 
**last_evaluation** | **datetime** |  | [optional] 
**name** | **str** |  | 
**query** | **str** |  | 
**state** | **str** | State can be \&quot;pending\&quot;, \&quot;firing\&quot;, \&quot;inactive\&quot;. | 
**totals** | **Dict[str, int]** |  | [optional] 
**totals_filtered** | **Dict[str, int]** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from grafanaApiClient.models.alerting_rule import AlertingRule

# TODO update the JSON string below
json = "{}"
# create an instance of AlertingRule from a JSON string
alerting_rule_instance = AlertingRule.from_json(json)
# print the JSON string representation of the object
print AlertingRule.to_json()

# convert the object into a dict
alerting_rule_dict = alerting_rule_instance.to_dict()
# create an instance of AlertingRule from a dict
alerting_rule_form_dict = alerting_rule.from_dict(alerting_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


