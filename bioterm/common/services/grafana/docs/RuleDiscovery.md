# RuleDiscovery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[RuleGroup]**](RuleGroup.md) |  | 
**totals** | **Dict[str, int]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.rule_discovery import RuleDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of RuleDiscovery from a JSON string
rule_discovery_instance = RuleDiscovery.from_json(json)
# print the JSON string representation of the object
print RuleDiscovery.to_json()

# convert the object into a dict
rule_discovery_dict = rule_discovery_instance.to_dict()
# create an instance of RuleDiscovery from a dict
rule_discovery_form_dict = rule_discovery.from_dict(rule_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


