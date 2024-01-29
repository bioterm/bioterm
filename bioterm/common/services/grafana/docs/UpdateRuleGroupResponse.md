# UpdateRuleGroupResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **List[str]** |  | [optional] 
**deleted** | **List[str]** |  | [optional] 
**message** | **str** |  | [optional] 
**updated** | **List[str]** |  | [optional] 

## Example

```python
from grafanaApiClient.models.update_rule_group_response import UpdateRuleGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRuleGroupResponse from a JSON string
update_rule_group_response_instance = UpdateRuleGroupResponse.from_json(json)
# print the JSON string representation of the object
print UpdateRuleGroupResponse.to_json()

# convert the object into a dict
update_rule_group_response_dict = update_rule_group_response_instance.to_dict()
# create an instance of UpdateRuleGroupResponse from a dict
update_rule_group_response_form_dict = update_rule_group_response.from_dict(update_rule_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


