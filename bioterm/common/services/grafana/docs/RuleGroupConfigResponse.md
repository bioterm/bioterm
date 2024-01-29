# RuleGroupConfigResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** | A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years. | [optional] 
**name** | **str** |  | [optional] 
**rules** | [**List[GettableExtendedRuleNode]**](GettableExtendedRuleNode.md) |  | [optional] 
**source_tenants** | **List[str]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.rule_group_config_response import RuleGroupConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RuleGroupConfigResponse from a JSON string
rule_group_config_response_instance = RuleGroupConfigResponse.from_json(json)
# print the JSON string representation of the object
print RuleGroupConfigResponse.to_json()

# convert the object into a dict
rule_group_config_response_dict = rule_group_config_response_instance.to_dict()
# create an instance of RuleGroupConfigResponse from a dict
rule_group_config_response_form_dict = rule_group_config_response.from_dict(rule_group_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


