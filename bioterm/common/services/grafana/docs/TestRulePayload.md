# TestRulePayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expr** | **str** |  | [optional] 
**grafana_condition** | [**EvalAlertConditionCommand**](EvalAlertConditionCommand.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.test_rule_payload import TestRulePayload

# TODO update the JSON string below
json = "{}"
# create an instance of TestRulePayload from a JSON string
test_rule_payload_instance = TestRulePayload.from_json(json)
# print the JSON string representation of the object
print TestRulePayload.to_json()

# convert the object into a dict
test_rule_payload_dict = test_rule_payload_instance.to_dict()
# create an instance of TestRulePayload from a dict
test_rule_payload_form_dict = test_rule_payload.from_dict(test_rule_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


