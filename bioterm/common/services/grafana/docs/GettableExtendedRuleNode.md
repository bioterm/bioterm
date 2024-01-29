# GettableExtendedRuleNode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **str** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**expr** | **str** |  | [optional] 
**var_for** | **str** |  | [optional] 
**grafana_alert** | [**GettableGrafanaRule**](GettableGrafanaRule.md) |  | [optional] 
**keep_firing_for** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**record** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_extended_rule_node import GettableExtendedRuleNode

# TODO update the JSON string below
json = "{}"
# create an instance of GettableExtendedRuleNode from a JSON string
gettable_extended_rule_node_instance = GettableExtendedRuleNode.from_json(json)
# print the JSON string representation of the object
print GettableExtendedRuleNode.to_json()

# convert the object into a dict
gettable_extended_rule_node_dict = gettable_extended_rule_node_instance.to_dict()
# create an instance of GettableExtendedRuleNode from a dict
gettable_extended_rule_node_form_dict = gettable_extended_rule_node.from_dict(gettable_extended_rule_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


