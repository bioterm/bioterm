# PostableExtendedRuleNode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **str** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**expr** | **str** |  | [optional] 
**var_for** | **str** |  | [optional] 
**grafana_alert** | [**PostableGrafanaRule**](PostableGrafanaRule.md) |  | [optional] 
**keep_firing_for** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**record** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.postable_extended_rule_node import PostableExtendedRuleNode

# TODO update the JSON string below
json = "{}"
# create an instance of PostableExtendedRuleNode from a JSON string
postable_extended_rule_node_instance = PostableExtendedRuleNode.from_json(json)
# print the JSON string representation of the object
print PostableExtendedRuleNode.to_json()

# convert the object into a dict
postable_extended_rule_node_dict = postable_extended_rule_node_instance.to_dict()
# create an instance of PostableExtendedRuleNode from a dict
postable_extended_rule_node_form_dict = postable_extended_rule_node.from_dict(postable_extended_rule_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


