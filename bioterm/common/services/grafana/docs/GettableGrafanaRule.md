# GettableGrafanaRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** |  | [optional] 
**data** | [**List[AlertQuery]**](AlertQuery.md) |  | [optional] 
**exec_err_state** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**interval_seconds** | **int** |  | [optional] 
**is_paused** | **bool** |  | [optional] 
**namespace_id** | **int** |  | [optional] 
**namespace_uid** | **str** |  | [optional] 
**no_data_state** | **str** |  | [optional] 
**org_id** | **int** |  | [optional] 
**provenance** | **str** |  | [optional] 
**rule_group** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.gettable_grafana_rule import GettableGrafanaRule

# TODO update the JSON string below
json = "{}"
# create an instance of GettableGrafanaRule from a JSON string
gettable_grafana_rule_instance = GettableGrafanaRule.from_json(json)
# print the JSON string representation of the object
print GettableGrafanaRule.to_json()

# convert the object into a dict
gettable_grafana_rule_dict = gettable_grafana_rule_instance.to_dict()
# create an instance of GettableGrafanaRule from a dict
gettable_grafana_rule_form_dict = gettable_grafana_rule.from_dict(gettable_grafana_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


