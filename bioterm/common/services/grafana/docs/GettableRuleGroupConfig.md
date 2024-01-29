# GettableRuleGroupConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**name** | **str** |  | [optional] 
**rules** | [**List[GettableExtendedRuleNode]**](GettableExtendedRuleNode.md) |  | [optional] 
**source_tenants** | **List[str]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_rule_group_config import GettableRuleGroupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GettableRuleGroupConfig from a JSON string
gettable_rule_group_config_instance = GettableRuleGroupConfig.from_json(json)
# print the JSON string representation of the object
print GettableRuleGroupConfig.to_json()

# convert the object into a dict
gettable_rule_group_config_dict = gettable_rule_group_config_instance.to_dict()
# create an instance of GettableRuleGroupConfig from a dict
gettable_rule_group_config_form_dict = gettable_rule_group_config.from_dict(gettable_rule_group_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


