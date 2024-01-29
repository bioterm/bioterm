# Rule

adapted from cortex

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation_time** | **float** |  | [optional] 
**health** | **str** |  | 
**labels** | **Dict[str, str]** | The custom marshaling for labels.Labels ends up doing this anyways. | [optional] 
**last_error** | **str** |  | [optional] 
**last_evaluation** | **datetime** |  | [optional] 
**name** | **str** |  | 
**query** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from grafanaApiClient.models.rule import Rule

# TODO update the JSON string below
json = "{}"
# create an instance of Rule from a JSON string
rule_instance = Rule.from_json(json)
# print the JSON string representation of the object
print Rule.to_json()

# convert the object into a dict
rule_dict = rule_instance.to_dict()
# create an instance of Rule from a dict
rule_form_dict = rule.from_dict(rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


