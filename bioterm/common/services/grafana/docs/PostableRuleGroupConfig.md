# PostableRuleGroupConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**name** | **str** |  | [optional] 
**rules** | [**List[PostableExtendedRuleNode]**](PostableExtendedRuleNode.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.postable_rule_group_config import PostableRuleGroupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PostableRuleGroupConfig from a JSON string
postable_rule_group_config_instance = PostableRuleGroupConfig.from_json(json)
# print the JSON string representation of the object
print PostableRuleGroupConfig.to_json()

# convert the object into a dict
postable_rule_group_config_dict = postable_rule_group_config_instance.to_dict()
# create an instance of PostableRuleGroupConfig from a dict
postable_rule_group_config_form_dict = postable_rule_group_config.from_dict(postable_rule_group_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


