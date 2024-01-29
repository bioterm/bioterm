# ApiRuleNode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **str** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**expr** | **str** |  | [optional] 
**var_for** | **str** |  | [optional] 
**keep_firing_for** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**record** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.api_rule_node import ApiRuleNode

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRuleNode from a JSON string
api_rule_node_instance = ApiRuleNode.from_json(json)
# print the JSON string representation of the object
print ApiRuleNode.to_json()

# convert the object into a dict
api_rule_node_dict = api_rule_node_instance.to_dict()
# create an instance of ApiRuleNode from a dict
api_rule_node_form_dict = api_rule_node.from_dict(api_rule_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


