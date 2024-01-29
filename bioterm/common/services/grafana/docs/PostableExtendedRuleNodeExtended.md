# PostableExtendedRuleNodeExtended


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_title** | **str** |  | [optional] 
**folder_uid** | **str** |  | [optional] 
**rule** | [**PostableExtendedRuleNode**](PostableExtendedRuleNode.md) |  | 
**rule_group** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.postable_extended_rule_node_extended import PostableExtendedRuleNodeExtended

# TODO update the JSON string below
json = "{}"
# create an instance of PostableExtendedRuleNodeExtended from a JSON string
postable_extended_rule_node_extended_instance = PostableExtendedRuleNodeExtended.from_json(json)
# print the JSON string representation of the object
print PostableExtendedRuleNodeExtended.to_json()

# convert the object into a dict
postable_extended_rule_node_extended_dict = postable_extended_rule_node_extended_instance.to_dict()
# create an instance of PostableExtendedRuleNodeExtended from a dict
postable_extended_rule_node_extended_form_dict = postable_extended_rule_node_extended.from_dict(postable_extended_rule_node_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


