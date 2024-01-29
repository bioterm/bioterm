# RuleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RuleDiscovery**](RuleDiscovery.md) |  | [optional] 
**error** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from grafanaApiClient.models.rule_response import RuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RuleResponse from a JSON string
rule_response_instance = RuleResponse.from_json(json)
# print the JSON string representation of the object
print RuleResponse.to_json()

# convert the object into a dict
rule_response_dict = rule_response_instance.to_dict()
# create an instance of RuleResponse from a dict
rule_response_form_dict = rule_response.from_dict(rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


