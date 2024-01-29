# AlertRuleGroupMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** |  | [optional] 

## Example

```python
from grafanaApiClient.models.alert_rule_group_metadata import AlertRuleGroupMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AlertRuleGroupMetadata from a JSON string
alert_rule_group_metadata_instance = AlertRuleGroupMetadata.from_json(json)
# print the JSON string representation of the object
print AlertRuleGroupMetadata.to_json()

# convert the object into a dict
alert_rule_group_metadata_dict = alert_rule_group_metadata_instance.to_dict()
# create an instance of AlertRuleGroupMetadata from a dict
alert_rule_group_metadata_form_dict = alert_rule_group_metadata.from_dict(alert_rule_group_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


