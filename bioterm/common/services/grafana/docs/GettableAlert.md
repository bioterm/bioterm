# GettableAlert

GettableAlert gettable alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** | LabelSet label set | 
**ends_at** | **datetime** | ends at | 
**fingerprint** | **str** | fingerprint | 
**generator_url** | **str** | generator URL Format: uri | [optional] 
**labels** | **Dict[str, str]** | LabelSet label set | 
**receivers** | [**List[Receiver]**](Receiver.md) | receivers | 
**starts_at** | **datetime** | starts at | 
**status** | [**AlertStatus**](AlertStatus.md) |  | 
**updated_at** | **datetime** | updated at | 

## Example

```python
from grafanaApiClient.models.gettable_alert import GettableAlert

# TODO update the JSON string below
json = "{}"
# create an instance of GettableAlert from a JSON string
gettable_alert_instance = GettableAlert.from_json(json)
# print the JSON string representation of the object
print GettableAlert.to_json()

# convert the object into a dict
gettable_alert_dict = gettable_alert_instance.to_dict()
# create an instance of GettableAlert from a dict
gettable_alert_form_dict = gettable_alert.from_dict(gettable_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


