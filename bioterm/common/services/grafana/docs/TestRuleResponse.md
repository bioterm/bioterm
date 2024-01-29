# TestRuleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[Sample]**](Sample.md) | Vector is basically only an alias for model.Samples, but the contract is that in a Vector, all Samples have the same timestamp. | [optional] 
**grafana_alert_instances** | [**AlertInstancesResponse**](AlertInstancesResponse.md) |  | [optional] 

## Example

```python
from grafanaApiClient.models.test_rule_response import TestRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestRuleResponse from a JSON string
test_rule_response_instance = TestRuleResponse.from_json(json)
# print the JSON string representation of the object
print TestRuleResponse.to_json()

# convert the object into a dict
test_rule_response_dict = test_rule_response_instance.to_dict()
# create an instance of TestRuleResponse from a dict
test_rule_response_form_dict = test_rule_response.from_dict(test_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


