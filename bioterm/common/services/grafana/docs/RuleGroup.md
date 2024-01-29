# RuleGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation_time** | **float** |  | [optional] 
**file** | **str** |  | 
**interval** | **float** |  | 
**last_evaluation** | **datetime** |  | [optional] 
**name** | **str** |  | 
**rules** | [**List[AlertingRule]**](AlertingRule.md) | In order to preserve rule ordering, while exposing type (alerting or recording) specific properties, both alerting and recording rules are exposed in the same array. | 
**totals** | **Dict[str, int]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.rule_group import RuleGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RuleGroup from a JSON string
rule_group_instance = RuleGroup.from_json(json)
# print the JSON string representation of the object
print RuleGroup.to_json()

# convert the object into a dict
rule_group_dict = rule_group_instance.to_dict()
# create an instance of RuleGroup from a dict
rule_group_form_dict = rule_group.from_dict(rule_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


