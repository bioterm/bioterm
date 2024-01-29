# PostableAlert

PostableAlert postable alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | LabelSet label set | [optional] 
**ends_at** | **datetime** | ends at Format: date-time | [optional] 
**generator_url** | **str** | generator URL Format: uri | [optional] 
**labels** | **Dict[str, str]** | LabelSet label set | 
**starts_at** | **datetime** | starts at Format: date-time | [optional] 

## Example

```python
from grafanaApiClient.models.postable_alert import PostableAlert

# TODO update the JSON string below
json = "{}"
# create an instance of PostableAlert from a JSON string
postable_alert_instance = PostableAlert.from_json(json)
# print the JSON string representation of the object
print PostableAlert.to_json()

# convert the object into a dict
postable_alert_dict = postable_alert_instance.to_dict()
# create an instance of PostableAlert from a dict
postable_alert_form_dict = postable_alert.from_dict(postable_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


