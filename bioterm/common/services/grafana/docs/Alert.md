# Alert

Alert alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generator_url** | **str** | generator URL Format: uri | [optional] 
**labels** | **Dict[str, str]** | LabelSet label set | 

## Example

```python
from grafanaApiClient.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print Alert.to_json()

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_form_dict = alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


