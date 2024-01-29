# AlertGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[GettableAlert]**](GettableAlert.md) | alerts | 
**labels** | **Dict[str, str]** | LabelSet label set | 
**receiver** | [**Receiver**](Receiver.md) |  | 

## Example

```python
from grafanaApiClient.models.alert_group import AlertGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AlertGroup from a JSON string
alert_group_instance = AlertGroup.from_json(json)
# print the JSON string representation of the object
print AlertGroup.to_json()

# convert the object into a dict
alert_group_dict = alert_group_instance.to_dict()
# create an instance of AlertGroup from a dict
alert_group_form_dict = alert_group.from_dict(alert_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


