# InhibitRule

InhibitRule defines an inhibition rule that mutes alerts that match the target labels if an alert matching the source labels exists. Both alerts have to have a set of labels being equal.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equal** | **List[str]** |  | [optional] 
**source_match** | **Dict[str, str]** | SourceMatch defines a set of labels that have to equal the given value for source alerts. Deprecated. Remove before v1.0 release. | [optional] 
**source_match_re** | **Dict[str, object]** |  | [optional] 
**source_matchers** | [**List[Matcher]**](Matcher.md) | Matchers is a slice of Matchers that is sortable, implements Stringer, and provides a Matches method to match a LabelSet against all Matchers in the slice. Note that some users of Matchers might require it to be sorted. | [optional] 
**target_match** | **Dict[str, str]** | TargetMatch defines a set of labels that have to equal the given value for target alerts. Deprecated. Remove before v1.0 release. | [optional] 
**target_match_re** | **Dict[str, object]** |  | [optional] 
**target_matchers** | [**List[Matcher]**](Matcher.md) | Matchers is a slice of Matchers that is sortable, implements Stringer, and provides a Matches method to match a LabelSet against all Matchers in the slice. Note that some users of Matchers might require it to be sorted. | [optional] 

## Example

```python
from grafanaApiClient.models.inhibit_rule import InhibitRule

# TODO update the JSON string below
json = "{}"
# create an instance of InhibitRule from a JSON string
inhibit_rule_instance = InhibitRule.from_json(json)
# print the JSON string representation of the object
print InhibitRule.to_json()

# convert the object into a dict
inhibit_rule_dict = inhibit_rule_instance.to_dict()
# create an instance of InhibitRule from a dict
inhibit_rule_form_dict = inhibit_rule.from_dict(inhibit_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


