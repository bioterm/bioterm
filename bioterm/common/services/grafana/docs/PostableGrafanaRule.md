# PostableGrafanaRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** |  | [optional] 
**data** | [**List[AlertQuery]**](AlertQuery.md) |  | [optional] 
**exec_err_state** | **str** |  | [optional] 
**is_paused** | **bool** |  | [optional] 
**no_data_state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from grafanaApiClient.models.postable_grafana_rule import PostableGrafanaRule

# TODO update the JSON string below
json = "{}"
# create an instance of PostableGrafanaRule from a JSON string
postable_grafana_rule_instance = PostableGrafanaRule.from_json(json)
# print the JSON string representation of the object
print PostableGrafanaRule.to_json()

# convert the object into a dict
postable_grafana_rule_dict = postable_grafana_rule_instance.to_dict()
# create an instance of PostableGrafanaRule from a dict
postable_grafana_rule_form_dict = postable_grafana_rule.from_dict(postable_grafana_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


